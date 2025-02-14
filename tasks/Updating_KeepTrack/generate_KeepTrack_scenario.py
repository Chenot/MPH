import csv
import random

# Parameters
practice_blocks_configuration = [(1, 2), (1, 3)]  # (number_of_blocks, number_of_words_to_memorize)
test_blocks_configuration = [(2, 2), (4, 3), (4, 4), (2, 5)]  # (number_of_blocks, number_of_words_to_memorize)
trials_per_block = 12
max_num_categories = 5  # Maximum number of categories to memorize

# Categories and their items in both French and English
categories = {
    'animal': [("ours", "bear"), ("chien", "dog"), ("cheval", "horse"), ("lion", "lion"), ("lapin", "rabbit"), ("loup", "wolf")],
    'color': [("bleu", "blue"), ("vert", "green"), ("blanc", "white"), ("violet", "purple"), ("rouge", "red"), ("jaune", "yellow")],
    'country': [("Australie", "Australia"), ("Brésil", "Brazil"), ("Chine", "China"), ("Italie", "Italy"), ("Inde", "India"), ("Japon", "Japan")],
    'fruit': [("banane", "banana"), ("fraise", "strawberry"), ("melon", "melon"), ("poire", "pear"), ("pomme", "apple"), ("abricot", "apricot")],
    'body': [("bouche", "mouth"), ("bras", "arm"), ("coude", "elbow"), ("pied", "foot"), ("jambe", "leg"), ("main", "hand")],
    'family': [("mère", "mother"), ("père", "father"), ("frère", "brother"), ("soeur", "sister"), ("tante", "aunt"), ("oncle", "uncle")]
}

# Generate practice and test blocks based on parameters
def generate_blocks(practice_blocks_configuration, test_blocks_configuration):
    blocks = []
    block_num = 1
    for num_blocks, words_to_memorize in practice_blocks_configuration:
        for _ in range(num_blocks):
            blocks.append(('practice', block_num, words_to_memorize))
            block_num += 1
    
    block_num = 1
    for num_blocks, words_to_memorize in test_blocks_configuration:
        for _ in range(num_blocks):
            blocks.append(('test', block_num, words_to_memorize))
            block_num += 1

    return blocks

blocks = generate_blocks(practice_blocks_configuration, test_blocks_configuration)

def generate_scenario():
    scenario_data = []
    with open('keep_track_scenario.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ['block', 'block_n', 'word_n', 'trial', 'stim_fr', 'stim_eng', 'animal', 'color', 'country', 'fruit', 'body', 'family'] + \
                 [f'cat_to_memorize{i+1}' for i in range(max_num_categories)]
        writer.writerow(header)

        for block_type, block_num, num_categories in blocks:
            target_categories = random.sample(list(categories.keys()), num_categories)
            trials = generate_trials(target_categories, num_categories)
            for trial_number, trial in enumerate(trials, start=1):
                row = [block_type, block_num, num_categories, trial_number] + trial + target_categories + ['NA'] * (max_num_categories - num_categories)
                scenario_data.append(row)
                writer.writerow(row)

    return scenario_data

def generate_trials(target_categories, num_categories):
    trials = []
    last_words = {category: 'NA' for category in categories}
    last_words_eng = {category: 'NA' for category in categories}
    
    target_items = [item for category in target_categories for item in categories[category]]
    non_target_categories = [cat for cat in categories if cat not in target_categories]
    non_target_items = [item for category in non_target_categories for item in categories[category]]

    if num_categories == 5:
        target_sample_size = 10
        non_target_sample_size = 2
    else:
        target_sample_size = 8
        non_target_sample_size = 4

    for _ in range(trials_per_block):
        trial_items = random.sample(target_items, target_sample_size) + random.sample(non_target_items, non_target_sample_size)
        random.shuffle(trial_items)

        for word_fr, word_eng in trial_items[:12]:
            category = get_category(word_fr)
            if category in target_categories:
                last_words[category] = word_fr
                last_words_eng[category] = word_eng
            
            trials.append([word_fr, word_eng, *last_words_eng.values()])

    return trials[:trials_per_block]

def get_category(word):
    for category, words in categories.items():
        if any(word in pair for pair in words):
            return category
    return None

def calculate_average_time(scenario_data):
    trials_per_block = 12
    num_blocks = len(scenario_data) // trials_per_block
    response_time_per_trial = 2  # seconds
    end_of_block_time = 30  # seconds

    total_trials_time = len(scenario_data) * response_time_per_trial
    total_end_of_block_time = num_blocks * end_of_block_time

    total_time = total_trials_time + total_end_of_block_time
    average_time_minutes = total_time / 60  # convert seconds to minutes

    print(f"Estimated average time to complete the experiment: {average_time_minutes:.2f} minutes")

if __name__ == "__main__":
    scenario_data = generate_scenario()
    calculate_average_time(scenario_data)
