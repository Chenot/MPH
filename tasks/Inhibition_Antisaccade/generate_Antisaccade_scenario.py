import pandas as pd
import numpy as np

# Number of trials for each block
num_trials_practice = 6
num_trials_block = 30

# Function to create a block of trials
def create_block(block_name, block_num, num_trials):
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    
    # Create positions with equal distribution
    positions = np.tile(['left', 'right'], num_trials // 2)
    np.random.shuffle(positions)
    
    # Create stimuli with equal distribution
    stimuli = np.tile(['ressources/left.png', 'ressources/right.png', 'ressources/up.png'], num_trials // 3)
    remainder_stimuli = num_trials % 3
    if remainder_stimuli > 0:
        stimuli = np.concatenate((stimuli, np.random.choice(['ressources/left.png', 'ressources/right.png', 'ressources/up.png'], remainder_stimuli, replace=False)))
    np.random.shuffle(stimuli)
    
    # Determine the correct response based on the stimulus
    correct_resp = np.where(stimuli == 'ressources/left.png', 'left', 
                            np.where(stimuli == 'ressources/right.png', 'right', 'up'))
    
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'position': positions,
        'stimulus': stimuli,
        'correct_resp': correct_resp
    })

# Create the blocks
practice_block = create_block('practice', 1, num_trials_practice)
block1 = create_block('test', 1, num_trials_block)
block2 = create_block('test', 2, num_trials_block)

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2])

# Calculate the total time to complete the task
time_per_trial = 2  # 2 seconds per trial
total_trials = len(scenario_df)
total_time_sec = total_trials * time_per_trial
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'antisaccade_task_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
