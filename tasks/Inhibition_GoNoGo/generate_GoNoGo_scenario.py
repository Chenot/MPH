import pandas as pd
import numpy as np

# Number of trials for each block
num_trials_practice = 10
num_trials_block = 50
percentageNoGo = 0.2  # 20% of No-Go trials

# ISI values and their corresponding values in 60Hz (in frames)
isi_values = [0.4, 0.5, 0.6]
isi_60Hz_values = [int(0.3 * 60), int(0.5 * 60), int(0.7 * 60)]

# Function to create a block of trials with specified percentage of no-go trials
def create_block(block_name, block_num, num_trials, nogo_percentage):
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    
    # Calculate number of no-go trials based on percentage
    num_nogo_trials = int(num_trials * nogo_percentage)
    num_go_trials = num_trials - num_nogo_trials
    
    # Create stimuli with the specified distribution of go and no-go
    stimuli = ['ressources/go.png'] * num_go_trials + ['ressources/nogo.png'] * num_nogo_trials
    np.random.shuffle(stimuli)
    
    # Generate the correct responses
    correct_resp = ['space' if stim == 'ressources/go.png' else 'NA' for stim in stimuli]
    
    # Create ISI and ISI_60Hz with equal distribution
    num_repeats = num_trials // len(isi_values)
    remainder = num_trials % len(isi_values)
    
    # Generate equal distribution of ISI values
    isi = np.tile(isi_values, num_repeats)
    if remainder > 0:
        isi = np.concatenate((isi, np.random.choice(isi_values, remainder, replace=False)))
    np.random.shuffle(isi)
    
    # Convert ISI values to 60Hz equivalent
    isi_60Hz = [int(i * 60) for i in isi]
    
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'stimulus': stimuli,
        'correct_resp': correct_resp,
        'ISI': isi,
        'ISI_60Hz': isi_60Hz
    })

# Create the blocks with 20% no-go trials for practice and test blocks
practice_block = create_block('practice', 1, num_trials_practice, nogo_percentage=percentageNoGo)
block1 = create_block('test', 1, num_trials_block, nogo_percentage=percentageNoGo)
block2 = create_block('test', 2, num_trials_block, nogo_percentage=percentageNoGo)
block3 = create_block('test', 3, num_trials_block, nogo_percentage=percentageNoGo)
block4 = create_block('test', 4, num_trials_block, nogo_percentage=percentageNoGo)

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2, block3, block4])

# Calculate the total time to complete the task
time_per_trial = 1  # 2 seconds per trial
total_trials = len(scenario_df)
total_time_sec = total_trials * time_per_trial
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'gonogo_task_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
