import pandas as pd
import numpy as np

# Parameters
num_practice_living_trials = 12
num_practice_size_trials = 12
num_practice_both_trials = 24
num_test_blocks = 4
num_test_trials_per_block = 48  # Can be adjusted to any even number
iti_min = 0.5  # minimum intertrial interval in seconds
iti_max = 0.7  # maximum intertrial interval in seconds
soa_min = 0.4  # minimum stimulus onset asynchrony in seconds
soa_max = 0.6  # maximum stimulus onset asynchrony in seconds

# Define the words
words = [
    ("cheval", "horse"), ("éléphant", "elephant"), ("girafe", "giraffe"), ("dauphin", "dolphin"), ("tigre", "tiger"), ("cerf", "deer"),
    ("fourmi", "ant"), ("lapin", "rabbit"), ("frelon", "hornet"), ("souris", "mouse"), ("papillon", "butterfly"), ("écureuil", "squirrel"),
    ("camion", "truck"), ("armoire", "wardrobe"), ("maison", "house"), ("piano", "piano"), ("table", "table"), ("canapé", "sofa"),
    ("bouteille", "bottle"), ("tasse", "cup"), ("clé", "key"), ("éponge", "sponge"), ("stylo", "stylo"), ("chaise", "chair")
]

# Define categories
living_words = [word for word, _ in words if word in {'cheval', 'éléphant', 'girafe', 'dauphin', 'tigre', 'cerf', 'fourmi', 'lapin', 'frelon', 'souris', 'papillon', 'écureuil'}]
non_living_words = [word for word, _ in words if word not in living_words]
larger_than_basketball_words = {'cheval', 'éléphant', 'girafe', 'dauphin', 'tigre', 'cerf', 'camion', 'armoire', 'maison', 'piano', 'table', 'canapé'}
non_larger_than_basketball = [word for word, _ in words if word not in larger_than_basketball_words]

# Define the stimuli
stimuli = {'living': 'images/heart.png', 'size': 'images/arrowcross.png'}

# Function to get the correct response based on instruction
def get_correct_response(word, instruction):
    if instruction == 'living':
        return 'k' if word in living_words else 'd'
    elif instruction == 'size':
        return 'k' if word in larger_than_basketball_words else 'd'
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
def create_block(block_name, block_num, block_type, num_trials, words, stimuli, iti_min, iti_max, soa_min, soa_max, instruction=None):
    half_trials = num_trials // 2
    trials = []
    
    # Prepare word lists based on instruction
    if instruction == 'living':
        living_sample = np.random.choice(living_words, half_trials, replace=False)
        non_living_sample = np.random.choice(non_living_words, half_trials, replace=False)
        word_list = np.concatenate([living_sample, non_living_sample])
        np.random.shuffle(word_list)
        instruction_sequence = [instruction] * num_trials
    elif instruction == 'size':
        larger_sample = np.random.choice(list(larger_than_basketball_words), half_trials, replace=False)
        non_larger_sample = np.random.choice(non_larger_than_basketball, half_trials, replace=False)
        word_list = np.concatenate([larger_sample, non_larger_sample])
        np.random.shuffle(word_list)
        instruction_sequence = [instruction] * num_trials
    else:
        # For block_type "both", use 50% switch and 50% repeat trials
        living_sample = np.random.choice(living_words, half_trials, replace=False)
        non_living_sample = np.random.choice(non_living_words, half_trials, replace=False)
        larger_sample = np.random.choice(list(larger_than_basketball_words), half_trials, replace=False)
        non_larger_sample = np.random.choice(non_larger_than_basketball, half_trials, replace=False)
        word_list = np.concatenate([living_sample, non_living_sample, larger_sample, non_larger_sample])
        
        instruction_sequence = np.concatenate([['living'] * half_trials, ['size'] * half_trials])
        np.random.shuffle(word_list)
        np.random.shuffle(instruction_sequence)
        
        # Generate 50% switch and 50% repeat trial types
        trial_types = np.concatenate([['repeat'] * (half_trials // 2), ['switch'] * (half_trials // 2),
                                      ['repeat'] * (half_trials // 2), ['switch'] * (half_trials // 2)])
        np.random.shuffle(trial_types)

    # Create each trial with constraints
    for trial in range(num_trials):
        instr = instruction_sequence[trial]
        word_fr = word_list[trial]
        word_eng = dict(words)[word_fr]
        
        correct_resp = get_correct_response(word_fr, instr)
        stimulus = stimuli[instr]
        iti = round(np.random.uniform(iti_min, iti_max), 3)
        soa = round(np.random.uniform(soa_min, soa_max), 3)
        iti_60hz = round(iti * 60)
        soa_60hz = round(soa * 60)
        trial_type = trial_types[trial] if block_type == 'both' else 'undefined'
        
        trial_info = {
            'block': block_name,
            'block_n': block_num,
            'block_type': block_type,
            'trial': trial + 1,
            'instruction': instr,
            'word_fr': word_fr,
            'word_eng': word_eng,
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

# Generate practice blocks with 50/50% repartition and apply constraints
practice_living_block = create_block('practice', 1, 'living', num_practice_living_trials, words, stimuli, iti_min, iti_max, soa_min, soa_max, instruction='living')
practice_size_block = create_block('practice', 2, 'size', num_practice_size_trials, words, stimuli, iti_min, iti_max, soa_min, soa_max, instruction='size')
practice_both_block = create_block('practice', 3, 'both', num_practice_both_trials, words, stimuli, iti_min, iti_max, soa_min, soa_max)

# Generate the test blocks with each word appearing twice and applying constraints
test_blocks = []
for block_num in range(1, num_test_blocks + 1):
    test_block_words = np.concatenate([living_words, non_living_words])
    test_word_list = np.tile(test_block_words, 2)  # Each word appears twice if num_test_trials_per_block is 48
    np.random.shuffle(test_word_list)
    
    instruction_sequence = np.random.choice(['living', 'size'], num_test_trials_per_block)
    trial_types = np.concatenate([['repeat'] * (num_test_trials_per_block // 2), ['switch'] * (num_test_trials_per_block // 2)])
    np.random.shuffle(trial_types)
    
    block_trials = []
    for trial in range(num_test_trials_per_block):
        instr = instruction_sequence[trial]
        word_fr = test_word_list[trial]
        word_eng = dict(words)[word_fr]
        
        correct_resp = get_correct_response(word_fr, instr)
        stimulus = stimuli[instr]
        iti = round(np.random.uniform(iti_min, iti_max), 3)
        soa = round(np.random.uniform(soa_min, soa_max), 3)
        iti_60hz = round(iti * 60)
        soa_60hz = round(soa * 60)
        trial_type = trial_types[trial]
        
        trial_info = {
            'block': 'test',
            'block_n': block_num,
            'block_type': 'both',
            'trial': trial + 1,
            'instruction': instr,
            'word_fr': word_fr,
            'word_eng': word_eng,
            'trial_type': trial_type,
            'stimulus': stimulus,
            'correct_resp': correct_resp,
            'iti': iti,
            'soa': soa,
            'iti_60hz': iti_60hz,
            'soa_60hz': soa_60hz
        }
        block_trials.append(trial_info)
    
    # Apply constraints on consecutive trial types and correct responses
    block_trials = enforce_constraints(block_trials, 'trial_type', max_repeats=3)
    block_trials = enforce_constraints(block_trials, 'correct_resp', max_repeats=3)
    
    test_blocks.append(pd.DataFrame(block_trials))

# Combine all blocks into a single DataFrame
scenario_df = pd.concat([practice_living_block, practice_size_block, practice_both_block] + test_blocks, ignore_index=True)

# Calculate the average time to complete the experiment
response_time = 0.5  # 500 ms response time in seconds
total_time = scenario_df['iti'].sum() + scenario_df['soa'].sum() + response_time * len(scenario_df)
average_time_minutes = total_time / 60  # convert seconds to minutes

# Save to a CSV file in the current directory with commas as the delimiter
file_path = 'category_switch_task_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Category-Switch Task scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f"Estimated average time to complete the experiment: {average_time_minutes:.2f} minutes")
