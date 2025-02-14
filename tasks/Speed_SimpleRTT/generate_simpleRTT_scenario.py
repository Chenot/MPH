import pandas as pd
import numpy as np

# Define the square wait and prestim values and frames at 60 Hz
isi_values = [1, 1.2222, 1.4444, 1.6666, 1.8888, 2.111, 2.3332, 2.5554, 2.7776, 2.9998]
frame_rate = 60

# Number of trials for each block
num_trials_practice = 3
num_trials_per_test_block = 15

# Function to create a block of trials
def create_block(block_name, block_num, num_trials, isi_values):
    # Ensure isi_values are equally distributed
    num_repeats = num_trials // len(isi_values)
    isi_sec = np.tile(isi_values, num_repeats)
    remainder = num_trials % len(isi_values)
    if remainder > 0:
        isi_sec = np.concatenate((isi_sec, np.random.choice(isi_values, remainder, replace=False)))
    np.random.shuffle(isi_sec)
    
    isi_frame60hz = (isi_sec * frame_rate).round().astype(int)
    
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'isi_sec': isi_sec,
        'isi_frame60hz': isi_frame60hz,
    })

# Create the blocks
practice_block = create_block('practice', 1, num_trials_practice, isi_values)
block1 = create_block('test', 1, num_trials_per_test_block, isi_values)
block2 = create_block('test', 2, num_trials_per_test_block, isi_values)

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2])

# Calculate the total time to complete the experiment
reaction_time = 0.5  # Assumed reaction time per trial
total_trials = len(scenario_df)
isi_total_time = scenario_df['isi_sec'].sum()
total_time_sec = isi_total_time + reaction_time * total_trials
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'keyboard_reaction_time_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the experiment: {total_minutes} minutes and {total_seconds} seconds.')
