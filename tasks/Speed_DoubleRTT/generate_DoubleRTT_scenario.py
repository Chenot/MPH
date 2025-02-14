import pandas as pd
import numpy as np

# Define the ISI values and corresponding frame counts
isi_values = [1, 1.2222, 1.4444, 1.6666, 1.8888, 2.111, 2.3332, 2.5554, 2.7776, 3]
frames = [60, 73, 87, 100, 113, 127, 140, 153, 166, 180]

# Define the stimuli and corresponding correct responses
stimuli = ['left_arrow.png', 'right_arrow.png']
correct_responses = {'left_arrow.png': 'left', 'right_arrow.png': 'right'}

# Number of trials for each block
num_trials_practice = 4
num_trials_test = 20

# Function to enforce no more than 3 consecutive stimuli
def create_constrained_stimulus_sequence(num_trials, stimuli, max_repeats=3):
    half_trials = num_trials // 2
    stimulus_list = ['left_arrow.png'] * half_trials + ['right_arrow.png'] * half_trials
    
    np.random.shuffle(stimulus_list)
    
    # Enforce no more than `max_repeats` consecutive identical stimuli
    while any(stimulus_list[i:i + max_repeats + 1] == [stimulus_list[i]] * (max_repeats + 1) for i in range(len(stimulus_list) - max_repeats)):
        np.random.shuffle(stimulus_list)
        
    return stimulus_list

# Function to create a block of trials
def create_block(block_name, block_num, num_trials, stimuli, correct_responses, isi_values, frames):
    # Get constrained stimulus sequence
    stimulus_column = create_constrained_stimulus_sequence(num_trials, stimuli)
    
    correct_resp_column = [correct_responses[stim] for stim in stimulus_column]
    
    # Shuffle the ISI values to distribute them across trials
    num_repeats = num_trials // len(isi_values)
    isi = np.tile(isi_values, num_repeats)
    remainder = num_trials % len(isi_values)
    if remainder > 0:
        isi = np.concatenate((isi, np.random.choice(isi_values, remainder, replace=False)))
    np.random.shuffle(isi)
    
    isi_frame = [frames[isi_values.index(val)] for val in isi]
    block_type = 'practice' if block_name == 'practice' else 'test'
    trial = list(range(1, num_trials + 1))
    
    return pd.DataFrame({
        'block': block_type,
        'block_n': block_num,
        'trial': trial,
        'stimulus': stimulus_column,
        'correct_resp': correct_resp_column,
        'isi': isi,
        'isi_frame60hz': isi_frame
    })

# Create the blocks
practice_block = create_block('practice', 1, num_trials_practice, stimuli, correct_responses, isi_values, frames)
block1 = create_block('block1', 1, num_trials_test, stimuli, correct_responses, isi_values, frames)
block2 = create_block('block2', 2, num_trials_test, stimuli, correct_responses, isi_values, frames)

# Concatenate all blocks
double_rtt_df = pd.concat([practice_block, block1, block2])

# Calculate the mean time to finish the task
reaction_time_per_trial = 0.5  # 500 ms in seconds
total_isi_time = double_rtt_df['isi'].sum()
total_reaction_time = reaction_time_per_trial * len(double_rtt_df)
total_time_seconds = total_isi_time + total_reaction_time
mean_time_minutes = total_time_seconds / 60  # convert seconds to minutes

# Save to a CSV file in the current directory
file_path = 'double_rtt_scenario.csv'
double_rtt_df.to_csv(file_path, index=False)

print("Double RTT scenario file created successfully!")
print(double_rtt_df.head())  # Display the first few rows of the DataFrame
print(f"Estimated mean time to complete the task: {mean_time_minutes:.2f} minutes")
