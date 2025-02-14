import pandas as pd
import numpy as np

# Parameters
num_trials_practice = 10  # Number of trials in each practice block
num_trials_block = 20  # Number of trials in each test block
block_type_init = [1, 2, 3]  # Types of n-back blocks (1-back, 2-back, 3-back)
number_per_block_type = 2  # Number of blocks of each n-back type
number_of_practice_blocks = 4  # Number of practice blocks
percentage_visual_target_only = 20  # Percentage of trials with visual-only target
percentage_auditory_target_only = 20  # Percentage of trials with auditory-only target
percentage_both_target = 10  # Percentage of trials with both targets

def create_block(block_name, block_num, block_type, num_trials, percentage_visual_target_only, percentage_auditory_target_only, percentage_both_target):
    while True:
        positions = ["pos_1", "pos_2", "pos_3", "pos_4", "pos_5", "pos_6", "pos_7", "pos_8", "pos_9"]
        auditory_stimuli = [f"ressources/{i}.wav" for i in range(1, 9)]
        
        square_positions = np.random.choice(positions, num_trials, replace=True).tolist()
        auditory_paths = np.random.choice(auditory_stimuli, num_trials, replace=True).tolist()
        visual_correct = ['NA'] * num_trials
        auditory_correct = ['NA'] * num_trials
        trial_type = ['none'] * num_trials

        num_both_target = int(num_trials * percentage_both_target / 100)
        num_visual_target_only = int(num_trials * percentage_visual_target_only / 100)
        num_auditory_target_only = int(num_trials * percentage_auditory_target_only / 100)

        available_trials = list(range(block_type, num_trials))
        
        # Assign "both" target trials
        both_target_trials = np.random.choice(available_trials, size=num_both_target, replace=False)
        for i in both_target_trials:
            square_positions[i] = square_positions[i - block_type]
            auditory_paths[i] = auditory_paths[i - block_type]
            visual_correct[i] = 'k'
            auditory_correct[i] = 'd'
            trial_type[i] = 'both'
            available_trials.remove(i)

        # Assign "visual_only" target trials
        visual_target_only_trials = np.random.choice(available_trials, size=num_visual_target_only, replace=False)
        for i in visual_target_only_trials:
            square_positions[i] = square_positions[i - block_type]
            while auditory_paths[i] == auditory_paths[i - block_type]:
                auditory_paths[i] = np.random.choice(auditory_stimuli)  # Re-select to avoid conflict
            visual_correct[i] = 'k'
            trial_type[i] = 'visual_only'
            available_trials.remove(i)

        # Assign "auditory_only" target trials
        auditory_target_only_trials = np.random.choice(available_trials, size=num_auditory_target_only, replace=False)
        for i in auditory_target_only_trials:
            auditory_paths[i] = auditory_paths[i - block_type]
            while square_positions[i] == square_positions[i - block_type]:
                square_positions[i] = np.random.choice(positions)  # Re-select to avoid conflict
            auditory_correct[i] = 'd'
            trial_type[i] = 'auditory_only'
            available_trials.remove(i)

        # Check the block for validity
        valid_block = True
        for i in range(block_type, num_trials):
            if trial_type[i] == 'both':
                if square_positions[i] != square_positions[i - block_type] or auditory_paths[i] != auditory_paths[i - block_type]:
                    valid_block = False
                    break
            elif trial_type[i] == 'visual_only':
                if square_positions[i] != square_positions[i - block_type] or auditory_paths[i] == auditory_paths[i - block_type]:
                    valid_block = False
                    break
            elif trial_type[i] == 'auditory_only':
                if square_positions[i] == square_positions[i - block_type] or auditory_paths[i] != auditory_paths[i - block_type]:
                    valid_block = False
                    break

            # Additional check to ensure no repetition in a "none" trial
            if trial_type[i] == 'none':
                if square_positions[i] == square_positions[i - block_type] or auditory_paths[i] == auditory_paths[i - block_type]:
                    valid_block = False
                    break

            # Check for more than two consecutive identical stimuli
            if i >= block_type and square_positions[i] == square_positions[i - 1] == square_positions[i - 2]:
                valid_block = False
                break
            if i >= block_type and auditory_paths[i] == auditory_paths[i - 1] == auditory_paths[i - 2]:
                valid_block = False
                break

        # If the block is valid, return it; otherwise, regenerate the entire block
        if valid_block:
            block = [block_name] * num_trials
            block_n = [block_num] * num_trials
            trial = list(range(1, num_trials + 1))
            block_type_list = [f"{block_type}-back"] * num_trials

            return pd.DataFrame({
                'block': block,
                'block_n': block_n,
                'block_type': block_type_list,
                'trial': trial,
                'square_position': square_positions,
                'visual_correct': visual_correct,
                'auditory_path': auditory_paths,
                'auditory_correct': auditory_correct,
                'trial_type': trial_type
            })

# Create all blocks and concatenate them into a single DataFrame
all_blocks = []

# Create practice blocks
for i in range(number_of_practice_blocks):
    if i < 3:
        practice_block = create_block('practice', i + 1, 1, num_trials_practice, percentage_visual_target_only, percentage_auditory_target_only, percentage_both_target)
    else:
        practice_block = create_block('practice', i + 1, 2, num_trials_practice, percentage_visual_target_only, percentage_auditory_target_only, percentage_both_target)
    all_blocks.append(practice_block)

# Create test blocks
block_num = 1
for _ in range(number_per_block_type):  # Repeat for each cycle
    for block_type in block_type_init:  # Cycle through 1-back, 2-back, 3-back
        test_block = create_block('test', block_num, block_type, num_trials_block, 
                                  percentage_visual_target_only, 
                                  percentage_auditory_target_only, 
                                  percentage_both_target)
        all_blocks.append(test_block)
        block_num += 1

# Concatenate all blocks into a single DataFrame
scenario_df = pd.concat(all_blocks)

# Calculate the total time to complete the task
seconds_per_trial = 3  
total_trials = len(scenario_df)
total_time_sec = total_trials * seconds_per_trial
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save the DataFrame to a CSV file
file_path = 'DualNback_scenario.csv'
scenario_df.to_csv(file_path, index=False)

# Print success message and display the first few rows of the DataFrame
print("Scenario file created successfully!")
print(scenario_df.head())
print(f'Approximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
