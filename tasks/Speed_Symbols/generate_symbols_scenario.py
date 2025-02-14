import pandas as pd
import numpy as np
import random

# Number of trials for each block
num_trials_practice = 10  # 10
num_trials_block = 48  # 25
num_test_blocks = 2

# Function to generate stimuli with no consecutive repetitions and from different categories
def generate_stimuli(num_trials, categories):
    stimuli1 = []
    stimuli2 = []
    for _ in range(num_trials):
        stim1_category = random.choice(categories)
        stim1 = f'ressources/symbol_{str(random.choice(range(stim1_category*10+1, stim1_category*10+9))).zfill(2)}.png'
        stim2_category = random.choice([cat for cat in categories if cat != stim1_category])
        stim2 = f'ressources/symbol_{str(random.choice(range(stim2_category*10+1, stim2_category*10+9))).zfill(2)}.png'
        stimuli1.append(stim1)
        stimuli2.append(stim2)
    return stimuli1, stimuli2

# Function to generate symbols ensuring the specified trial conditions
def generate_symbols(num_trials, categories, stimuli1, stimuli2, correct_resp):
    symbols = []
    for i in range(num_trials):
        block_symbols = set()
        used_categories = set()

        if correct_resp[i] == 'k':  # Trials where at least one symbol matches either stimulus1 or stimulus2
            stimulus = random.choice([stimuli1[i], stimuli2[i]])
            block_symbols.add(stimulus)
            used_categories.add(int(stimulus.split('_')[-1][:2]) // 10)

        while len(block_symbols) < 5:
            category = random.choice([cat for cat in categories if cat not in used_categories])
            used_categories.add(category)
            symbol = f'ressources/symbol_{str(random.choice(range(category*10+1, category*10+9))).zfill(2)}.png'
            if correct_resp[i] == 'd' and symbol not in {stimuli1[i], stimuli2[i]}:
                block_symbols.add(symbol)
            elif correct_resp[i] == 'k':
                block_symbols.add(symbol)
        
        symbols.append(list(block_symbols))
    
    # Shuffle symbols for each trial
    for trial in symbols:
        random.shuffle(trial)
    
    return symbols

# Function to create a block of trials
def create_block(block_name, block_num, num_trials):
    categories = list(range(8))  # Categories 0 to 7
    trials = list(range(1, num_trials + 1))
    
    stimuli1, stimuli2 = generate_stimuli(num_trials, categories)
    
    # Randomize correct responses ('k' and 'd') ensuring equal distribution
    correct_resp = ['k'] * (num_trials // 2) + ['d'] * (num_trials // 2)
    random.shuffle(correct_resp)
    
    symbols = generate_symbols(num_trials, categories, stimuli1, stimuli2, correct_resp)
    
    data = {
        'block': [block_name] * num_trials,
        'block_n': [block_num] * num_trials,
        'trial': trials,
        'stimulus1': stimuli1,
        'stimulus2': stimuli2,
        'correct_resp': correct_resp
    }
    
    for i in range(5):
        data[f'symbol{i+1}'] = [symbols[trial][i] for trial in range(num_trials)]
    
    return pd.DataFrame(data)

# Create practice and test blocks
practice_block = create_block('practice', 0, num_trials_practice)
test_blocks = [create_block('test', i+1, num_trials_block) for i in range(num_test_blocks)]

# Concatenate all blocks
scenario_df = pd.concat([practice_block] + test_blocks, ignore_index=True)

# Calculate the total time to complete the task
reaction_time = 2  # 2 seconds per trial
total_trials = len(scenario_df)
total_time_sec = reaction_time * total_trials
total_minutes = int(total_time_sec // 60)
total_seconds = int(total_time_sec % 60)

# Save to a CSV file in the current directory
file_path = 'symbols_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head())  # Display the first few rows of the DataFrame
print(f'Approximate total time to complete the task: {total_minutes} minutes and {total_seconds} seconds.')
