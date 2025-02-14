import pandas as pd
import numpy as np

# Define the square wait and prestim values and frames at 60 Hz
square_wait_values = [0.8, 1, 1.2]
prestim_values = [1, 1.2222, 1.4444, 1.6666, 1.8888, 2.111, 2.3332, 2.5554, 2.7776, 2.9998]
frame_rate = 60

# Number of trials for each block
num_trials_practice = 10
num_trials_per_test_block = 20

# Circle degrees in steps of 18 degrees
circle_degrees = list(range(0, 360, 18))

# Function to create a block of trials
def create_block(block_name, block_num, num_trials, square_wait_values, prestim_values, circle_degrees):
    square_wait_sec = np.random.choice(square_wait_values, num_trials)
    square_wait_frame60hz = (square_wait_sec * frame_rate).round().astype(int)
    
    # Ensure prestim_values are equally distributed
    num_repeats = num_trials // len(prestim_values)
    prestim_sec = np.tile(prestim_values, num_repeats)
    remainder = num_trials % len(prestim_values)
    if remainder > 0:
        prestim_sec = np.concatenate((prestim_sec, np.random.choice(prestim_values, remainder, replace=False)))
    np.random.shuffle(prestim_sec)
    
    prestim_frame60hz = (prestim_sec * frame_rate).round().astype(int)
    np.random.shuffle(circle_degrees)
    if len(circle_degrees) < num_trials:
        circle_degree = np.random.choice(circle_degrees, num_trials, replace=True)
    else:
        circle_degree = circle_degrees[:num_trials]
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    trial = list(range(1, num_trials + 1))
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'trial': trial,
        'square_sec': square_wait_sec,
        'square_frame60hz': square_wait_frame60hz,
        'prestim_sec': prestim_sec,
        'prestim_frame60hz': prestim_frame60hz,
        'circle_degree': circle_degree
    })

# Create the blocks
practice_block = create_block('practice', 1, num_trials_practice, square_wait_values, prestim_values, circle_degrees)
block1 = create_block('test', 1, num_trials_per_test_block, square_wait_values, prestim_values, circle_degrees)
block2 = create_block('test', 2, num_trials_per_test_block, square_wait_values, prestim_values, circle_degrees)

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2])

# Calculate the total time to complete the experiment
reaction_time = 0.5
total_trials = len(scenario_df)
square_wait_total_time = scenario_df['square_sec'].sum()
prestim_total_time = scenario_df['prestim_sec'].sum()
total_time_sec = square_wait_total_time + prestim_total_time + reaction_time * total_trials
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'simpleRTTmouse_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the experiment: {total_minutes} minutes and {total_seconds} seconds.')
