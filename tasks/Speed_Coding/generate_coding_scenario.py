import pandas as pd
import numpy as np

# Number of trials for each block
num_trials_practice = 9  # Adjusted for demonstration purposes
num_trials_block = 27  # You can set this to any multiple of 9

# Function to generate shuffled stimuli, ensuring each symbol appears once in every set of 9 trials
def generate_stimuli(num_trials, block_num=0):
    if num_trials % 9 != 0:
        raise ValueError("Number of trials must be a multiple of 9 to ensure each symbol appears exactly once per set.")

    # Create the base set of symbols (1 to 9)
    symbols = list(range(1, 10))
    
    # Determine how many complete sets of symbols we need
    num_sets = num_trials // 9
    
    # Create stimuli by shuffling the symbols for each set
    stimuli = []
    for _ in range(num_sets):
        shuffled_symbols = np.random.permutation(symbols).tolist()
        stimuli.extend(shuffled_symbols)
    
    # Convert the symbol numbers into their corresponding file paths
    stimulus_files = [f'ressources/symbol{stim}_{block_num}.png' for stim in stimuli]
    
    return stimulus_files

# Function to create a block of trials
def create_block(block_name, block_num, num_trials, response_type):
    block = [f"{block_name}_{response_type}"] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    
    # Generate shuffled stimuli
    stimulus_files = generate_stimuli(num_trials, block_num)
    correct_resp = [f'num_{stim.split("symbol")[1].split("_")[0]}' for stim in stimulus_files]  # Correct response based on number in symbol
    
    grid = [f'ressources/symbolAndDigit{block_num}.png'] * num_trials  # Grid image path

    # Combine all columns into a DataFrame
    data = {
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'stimulus': stimulus_files,
        'correct_resp': correct_resp,
        'grid': grid
    }
    
    return pd.DataFrame(data)

# Create the practice and test blocks
practice_block = create_block('practice', 0, num_trials_practice, 'keyboard')
block1 = create_block('test', 1, num_trials_block, 'keyboard')
block2 = create_block('test', 2, num_trials_block, 'keyboard')
block3 = create_block('test', 3, num_trials_block, 'keyboard')
block4 = create_block('test', 4, num_trials_block, 'keyboard')

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2, block3, block4])

# Calculate the total time to complete the task
reaction_time = 2  # 1000 ms
total_trials = len(scenario_df)
total_time_sec = reaction_time * total_trials
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'coding_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
