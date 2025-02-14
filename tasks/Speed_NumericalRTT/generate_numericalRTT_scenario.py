import pandas as pd
import numpy as np

# ------------------------------
# Task Configuration Parameters
# ------------------------------

# Number of trials
num_trials_practice = 9   # One trial for each number (1-9)
num_trials_block = 36     # Each test block has 36 trials (each number appears 4 times)
num_test_blocks = 2       # Total number of test blocks

# ISI values and their corresponding values in 60Hz (in frames)
isi_values = [0.4, 0.5, 0.6]  # in seconds
isi_60Hz_values = [int(0.3 * 60), int(0.5 * 60), int(0.7 * 60)]  # [18, 30, 42] frames

# Time per trial in seconds
time_per_trial = 1  # Adjust as needed

# ------------------------------
# Function to Shuffle Stimuli Without Consecutive Duplicates
# ------------------------------

def shuffle_with_no_consecutive_duplicates(stimuli, max_attempts=1000):
    """
    Shuffles a list of stimuli ensuring that no two identical stimuli are consecutive.

    Parameters:
    - stimuli (list of str): The list of stimuli to shuffle.
    - max_attempts (int): Maximum number of shuffle attempts before raising an error.

    Returns:
    - list of str: Shuffled stimuli with no consecutive duplicates.

    Raises:
    - ValueError: If a valid shuffle is not found within the maximum number of attempts.
    """
    for attempt in range(max_attempts):
        shuffled = stimuli.copy()
        np.random.shuffle(shuffled)
        # Check for consecutive duplicates
        duplicates = any(shuffled[i] == shuffled[i+1] for i in range(len(shuffled)-1))
        if not duplicates:
            return shuffled
    raise ValueError(f"Unable to shuffle stimuli without consecutive duplicates after {max_attempts} attempts.")

# ------------------------------
# Function to Create a Numerical Task Block
# ------------------------------

def create_block(block_name, block_num, num_trials, stimuli):
    """
    Creates a block of trials for the RT_numerical task.

    Parameters:
    - block_name (str): Name of the block (e.g., 'practice', 'test').
    - block_num (int): Block number identifier.
    - num_trials (int): Number of trials in the block.
    - stimuli (list of str): List of numerical stimuli as strings.

    Returns:
    - pd.DataFrame: DataFrame containing the block's trial information.
    """
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    
    # Shuffle stimuli ensuring no consecutive duplicates in test blocks
    if block_name == 'test':
        try:
            shuffled_stimuli = shuffle_with_no_consecutive_duplicates(stimuli)
        except ValueError as e:
            print(f"Error in block '{block_name}' number {block_num}: {e}")
            print("Proceeding with a regular shuffle (may contain consecutive duplicates).")
            shuffled_stimuli = stimuli.copy()
            np.random.shuffle(shuffled_stimuli)
    else:
        # For practice blocks, simply shuffle since all stimuli are unique
        shuffled_stimuli = stimuli.copy()
        np.random.shuffle(shuffled_stimuli)
    
    # Define correct responses as 'num_X' corresponding to stimuli
    correct_resp = [f'num_{stim}' for stim in shuffled_stimuli]
    
    # Generate ISI with equal distribution
    num_repeats = num_trials // len(isi_values)
    remainder = num_trials % len(isi_values)
    
    # Create a balanced ISI list
    isi = np.tile(isi_values, num_repeats)
    if remainder > 0:
        # Randomly select remaining ISI values without replacement
        isi = np.concatenate((isi, np.random.choice(isi_values, remainder, replace=False)))
    np.random.shuffle(isi)
    
    # Convert ISI values to 60Hz equivalent
    isi_60Hz = [int(i * 60) for i in isi]
    
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'stimulus': shuffled_stimuli,
        'correct_resp': correct_resp,
        'ISI': isi,
        'ISI_60Hz': isi_60Hz
    })

# ------------------------------
# Creating Practice and Test Blocks
# ------------------------------

# Define numerical stimuli as strings for consistency with keyboard responses
numbers = [str(i) for i in range(1, 10)]  # ['1', '2', ..., '9']

# ------------------------------
# Create Practice Block
# ------------------------------
# Each number from 1 to 9 appears once in practice
practice_stimuli = numbers.copy()
practice_block = create_block('practice', 1, num_trials_practice, practice_stimuli)

# ------------------------------
# Create Test Blocks
# ------------------------------
test_blocks = []
for block_num in range(1, num_test_blocks + 1):
    # Each number appears four times in each test block (36 trials)
    test_stimuli = numbers * 4  # ['1', '2', ..., '9', '1', '2', ..., '9', ..., '1', '2', ..., '9']
    test_block = create_block('test', block_num, num_trials_block, test_stimuli)
    test_blocks.append(test_block)

# ------------------------------
# Concatenate All Blocks
# ------------------------------
scenario_df = pd.concat([practice_block] + test_blocks, ignore_index=True)

# ------------------------------
# Calculate the Total Time to Complete the Task
# ------------------------------
total_trials = len(scenario_df)
total_time_sec = total_trials * time_per_trial
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# ------------------------------
# Save to CSV File
# ------------------------------
file_path = 'numericalRTT_scenario.csv'
scenario_df.to_csv(file_path, index=False)

# ------------------------------
# Output Confirmation and Sample Data
# ------------------------------
print("RT_numerical Task Scenario file created successfully!")
print("\nSample of the generated scenario:")
print(scenario_df.head(15))  # Display the first 15 rows of the DataFrame
print(f'\nApproximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
