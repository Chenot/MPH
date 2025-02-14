import pandas as pd
import numpy as np

# Parameters
num_practice_color_trials = 12
num_practice_shape_trials = 12
num_practice_both_trials = 24
num_test_blocks = 4
num_test_trials = 48  # Each block contains 48 trials, 24 repeat and 24 switch
iti_min = 0.5  # minimum intertrial interval in seconds
iti_max = 0.7  # maximum intertrial interval in seconds
soa_min = 0.4  # minimum stimulus onset asynchrony in seconds
soa_max = 0.6  # maximum stimulus onset asynchrony in seconds

# Define the stimuli
stimuli = ['images/redcircle.png', 'images/redtriangle.png', 'images/greencircle.png', 'images/greentriangle.png']

# Function to get the correct response based on instruction
def get_correct_response(stimulus, instruction):
    if instruction == 'color':
        return 'k' if 'red' in stimulus else 'd'
    elif instruction == 'shape':
        return 'd' if 'circle' in stimulus else 'k'
    return None

# Helper function to enforce constraints
def enforce_constraints(trials, key, max_repeats=3):
    count = 1
    for i in range(1, len(trials)):
        if trials[i][key] == trials[i - 1][key]:
            count += 1
            if count > max_repeats:
                # Swap with next different trial
                for j in range(i + 1, len(trials)):
                    if trials[j][key] != trials[i][key]:
                        trials[i], trials[j] = trials[j], trials[i]
                        break
                count = 1  # Reset count after a swap
        else:
            count = 1
    return trials

# Function to create a balanced block of trials
def create_block(block_name, block_num, block_type, num_trials, stimuli, iti_min, iti_max, soa_min, soa_max, instruction=None):
    half_trials = num_trials // 2
    trials = []

    # Prepare instruction sequence and trial types
    if instruction:
        instruction_sequence = [instruction] * num_trials
        trial_types = ['undefined'] * num_trials  # No switch/repeat logic in single-instruction blocks
    else:
        # Alternate between color and shape instructions with 50% switch and repeat
        instruction_sequence = np.random.choice(['color', 'shape'], num_trials)
        trial_types = np.concatenate([['repeat'] * (half_trials // 2), ['switch'] * (half_trials // 2),
                                      ['repeat'] * (half_trials // 2), ['switch'] * (half_trials // 2)])
        np.random.shuffle(trial_types)

    # Generate stimuli sequence with no repetitions
    stimuli_repeated = np.tile(stimuli, num_trials // len(stimuli))[:num_trials]
    np.random.shuffle(stimuli_repeated)

    # Create each trial
    for trial in range(num_trials):
        instr = instruction_sequence[trial]
        stimulus = stimuli_repeated[trial]
        correct_resp = get_correct_response(stimulus, instr)
        iti = round(np.random.uniform(iti_min, iti_max), 3)
        soa = round(np.random.uniform(soa_min, soa_max), 3)
        iti_60hz = round(iti * 60)
        soa_60hz = round(soa * 60)
        trial_type = trial_types[trial] if block_type == 'both' else 'undefined'
        
        # Determine French and English instruction codes
        instruction_fr = 'C' if instr == 'color' else 'F'
        instruction_eng = 'C' if instr == 'color' else 'S'

        trial_info = {
            'block': block_name,
            'block_n': block_num,
            'block_type': block_type,
            'trial': trial + 1,
            'instruction': instr,
            'instruction_fr': instruction_fr,
            'instruction_eng': instruction_eng,
            'trial_type': trial_type,
            'stimulus': stimulus,
            'correct_resp': correct_resp,
            'iti': iti,
            'soa': soa,
            'iti_60hz': iti_60hz,
            'soa_60hz': soa_60hz
        }
        trials.append(trial_info)
    
    # Apply constraints on consecutive trial types and correct responses
    trials = enforce_constraints(trials, 'trial_type', max_repeats=3)
    trials = enforce_constraints(trials, 'correct_resp', max_repeats=3)
    
    return pd.DataFrame(trials)

# Generate the practice blocks with constraints
practice_color_block = create_block('practice', 1, 'color', num_practice_color_trials, stimuli, iti_min, iti_max, soa_min, soa_max, instruction='color')
practice_shape_block = create_block('practice', 2, 'shape', num_practice_shape_trials, stimuli, iti_min, iti_max, soa_min, soa_max, instruction='shape')
practice_both_block = create_block('practice', 3, 'both', num_practice_both_trials, stimuli, iti_min, iti_max, soa_min, soa_max)

# Generate the test blocks with constraints
test_blocks = []
for block_num in range(1, num_test_blocks + 1):
    block = create_block('test', block_num, 'both', num_test_trials, stimuli, iti_min, iti_max, soa_min, soa_max)
    test_blocks.append(block)

# Combine all blocks into a single DataFrame
scenario_df = pd.concat([practice_color_block, practice_shape_block, practice_both_block] + test_blocks, ignore_index=True)

# Calculate the average time to complete the experiment
response_time = 0.5  # 500 ms response time in seconds
total_time = scenario_df['iti'].sum() + scenario_df['soa'].sum() + response_time * len(scenario_df)
average_time_minutes = total_time / 60  # convert seconds to minutes

# Save to a CSV file in the current directory with commas as the delimiter
file_path = 'color_shape_task_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Color-Shape Task scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f"Estimated average time to complete the experiment: {average_time_minutes:.2f} minutes")
