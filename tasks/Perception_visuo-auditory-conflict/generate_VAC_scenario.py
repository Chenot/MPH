import pandas as pd
import numpy as np

# Number of trials for each block
num_trials_block = 48
num_trials_practice = 8  # Number of trials for the practice block
iti_values = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]  # ITI values in seconds

# Function to generate shuffled ITI values
def generate_iti_column(num_trials):
    repeated_iti = iti_values * (num_trials // len(iti_values))
    remaining_iti = iti_values[:num_trials % len(iti_values)]
    all_iti = repeated_iti + remaining_iti
    np.random.shuffle(all_iti)
    return all_iti

# Function to create a practice block
def create_practice_block(block_name, block_num, num_trials):
    half_trials = num_trials // 2  # Half for visual, half for auditory
    trials = list(range(1, num_trials + 1))
    
    # Generate all possible combinations of positions
    positions = [('left', 'left'), ('left', 'right'), ('right', 'left'), ('right', 'right')]
    
    # Ensure even distribution of congruent and incongruent trials
    congruence = ['congruent', 'incongruent'] * (num_trials // 2)
    np.random.shuffle(congruence)
    
    # Prepare a shuffled list of all possible positions to ensure balance
    visual_positions = positions * (half_trials // len(positions))
    auditory_positions = positions * (half_trials // len(positions))
    np.random.shuffle(visual_positions)
    np.random.shuffle(auditory_positions)
    
    positions_visual = []
    positions_auditory = []
    block_types = []
    correct_resp = []
    
    # Generate trials for the practice block
    for i, trial in enumerate(trials):
        if trial <= half_trials:
            block_type = 'visual'
            position_pair = visual_positions.pop()
            if congruence[i] == 'congruent':
                positions_visual.append(position_pair[0])
                positions_auditory.append(position_pair[0])
            else:
                positions_visual.append(position_pair[0])
                positions_auditory.append('right' if position_pair[0] == 'left' else 'left')
            
            correct_resp.append('k' if positions_visual[-1] == 'right' else 'd')
        else:
            block_type = 'auditory'
            position_pair = auditory_positions.pop()
            if congruence[i] == 'congruent':
                positions_visual.append(position_pair[0])
                positions_auditory.append(position_pair[0])
            else:
                positions_visual.append(position_pair[0])
                positions_auditory.append('right' if position_pair[0] == 'left' else 'left')
            
            correct_resp.append('k' if positions_auditory[-1] == 'right' else 'd')
        
        block_types.append(block_type)
    
    iti_column = generate_iti_column(num_trials)
    
    return pd.DataFrame({
        'block': [block_name] * num_trials,
        'block_n': [block_num] * num_trials,
        'block_type': block_types,
        'trial': trials,
        'position_visual': positions_visual,
        'position_auditory': positions_auditory,
        'congruence': congruence,
        'correct_resp': correct_resp,
        'ITI': iti_column,
        'ITI_frame60hz': [iti * 60 for iti in iti_column]
    })

# Function to create a block of trials
def create_block(block_name, block_num, block_type, num_trials):
    block = [block_name] * num_trials
    block_n = [block_num] * num_trials
    block_type_col = [block_type] * num_trials
    trial = list(range(1, num_trials + 1))
    
    # Create positions with equal distribution
    positions_visual = np.tile(['left', 'right'], num_trials // 2)
    positions_auditory = np.tile(['left', 'right'], num_trials // 2)
    
    # Create congruence with equal distribution
    congruence = np.tile(['congruent', 'incongruent'], num_trials // 2)
    
    # Shuffle positions and congruence
    np.random.shuffle(positions_visual)
    np.random.shuffle(positions_auditory)
    np.random.shuffle(congruence)
    
    # Adjust positions for congruent and incongruent trials
    for i in range(num_trials):
        if congruence[i] == 'congruent':
            positions_auditory[i] = positions_visual[i]
        else:
            positions_auditory[i] = 'right' if positions_visual[i] == 'left' else 'left'
    
    # Determine the correct response
    correct_resp = []
    for i in range(num_trials):
        if block_type == 'visual':
            correct_resp.append('k' if positions_visual[i] == 'right' else 'd')
        else:
            correct_resp.append('k' if positions_auditory[i] == 'right' else 'd')
    
    iti_column = generate_iti_column(num_trials)
    
    return pd.DataFrame({
        'block': block,
        'block_n': block_n,
        'block_type': block_type_col,
        'trial': trial,
        'position_visual': positions_visual,
        'position_auditory': positions_auditory,
        'congruence': congruence,
        'correct_resp': correct_resp,
        'ITI': iti_column,
        'ITI_frame60hz': [iti * 60 for iti in iti_column]
    })

# Create the practice block
practice_block = create_practice_block('practice', 0, num_trials_practice)

# Create the test blocks
block1 = create_block('test', 1, 'visual', num_trials_block)
block2 = create_block('test', 2, 'auditory', num_trials_block)

# Concatenate all blocks
scenario_df = pd.concat([practice_block, block1, block2])

# Save to a CSV file in the current directory
file_path = 'visual_auditory_conflict_task_scenario.csv'
scenario_df.to_csv(file_path, index=False)

print("Scenario file created successfully!")
print(scenario_df.head(20))  # Display the first few rows of the DataFrame
