import csv
import random
from datetime import timedelta

# Define game variables
game_duration = 180  # in seconds (3 minutes)
ship_missiles = 50  # number of missiles in the ship at the start
num_mines = 18
num_bonuses = 30
time_jitter = 3  # Time jitter to prevent regular intervals of mines and bonuses in seconds
num_type1_mines = int(num_mines * 0.5)  # 50% of type-1 mines
num_capturable_bonuses = int(num_bonuses * 0.5)  # 50% of capturable bonuses
last_mine_appearance = int(game_duration-10)  # Last mine will appear exactly 10 seconds before the end of the game
last_bonus_appearance = int(game_duration-5)  # Last bonus will appear exactly 5 seconds before the end of the game

# Define possible positions and stimuli
BONUS_POSITIONS = [
    "near_north_west", "near_north", "near_north_east", "near_east", 
    "near_south_east", "near_south", "near_south_west", "near_west",
    "far_north_west", "far_north", "far_north_east", "far_east",
    "far_south_east", "far_south", "far_south_west", "far_west"
]

MINE_POSITIONS = ["opposite", "horizontal", "vertical"]

# Function to convert seconds into HH:MM:SS format
def format_time(seconds):
    return str(timedelta(seconds=seconds))

# Function to initialize the three letters for type-1 mines
def initialize_mine_letters():
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)  # Three random letters for type-1 mines
    return letters

# Function to shuffle mines and bonuses with constraints (no more than 2 consecutive)
def shuffle_with_constraints(items):
    random.shuffle(items)
    while any(items[i] == items[i+1] == items[i+2] for i in range(len(items)-2)):
        random.shuffle(items)
    return items

# Function to calculate mine positions based on rules
def distribute_mine_positions(num_mines):
    num_opposite = num_mines // 3 + (num_mines % 3)  # Majority of extra mines go to "opposite"
    num_horizontal = num_vertical = (num_mines - num_opposite) // 2  # Equal distribution for horizontal and vertical
    return ["opposite"] * num_opposite + ["horizontal"] * num_horizontal + ["vertical"] * num_vertical

# Function to shuffle bonus positions ensuring no repeats until all positions are exhausted
def shuffle_bonus_positions(bonus_count):
    shuffled_positions = []
    while len(shuffled_positions) < bonus_count:
        positions = BONUS_POSITIONS.copy()
        random.shuffle(positions)
        shuffled_positions.extend(positions[:min(len(positions), bonus_count - len(shuffled_positions))])
    return shuffled_positions

# Function to calculate min/max intervals
def calculate_time_intervals(time_list):
    intervals = [time_list[i] - time_list[i-1] for i in range(1, len(time_list))]
    return min(intervals), max(intervals)

# Function to generate the scenario
def generate_scenario():
    # Time step excludes the final appearance of the last mine and bonus
    time_step_mine = (last_mine_appearance) / (num_mines - 1)  # All mines except the last one
    time_step_bonus = (last_bonus_appearance) / (num_bonuses - 1)  # All bonuses except the last one

    current_time_mine = 0
    current_time_bonus = 0
    
    type1_letters = initialize_mine_letters()
    type2_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letter not in type1_letters]

    # Create exactly num_type1_mines of type-1 and the rest as type-2
    mine_types = ["type-1"] * num_type1_mines + ["type-2"] * (num_mines - num_type1_mines)
    shuffled_mine_types = shuffle_with_constraints(mine_types)

    # Distribute mine positions based on rules
    mine_positions = distribute_mine_positions(num_mines)
    shuffled_mine_positions = shuffle_with_constraints(mine_positions)

    # Shuffle bonus positions
    shuffled_bonus_positions = shuffle_bonus_positions(num_bonuses)

    events = []
    mine_times = []
    bonus_times = []

    # Add initial game, ship, and fortress entries
    events.append(("0:00:00", "game", "NA", "NA", "start"))
    events.append(("0:00:00", "ship", "near_west", "NA", ship_missiles))
    events.append(("0:00:00", "fortress", "middle", "NA", "NA"))

    # Generate mines except the last one
    for i, mine_type in enumerate(shuffled_mine_types[:-1]):
        current_time_mine += int(time_step_mine + random.uniform(-time_jitter, time_jitter))
        mine_times.append(current_time_mine)
        time_str = format_time(current_time_mine)
        if mine_type == "type-1":
            mine_letter = random.choice(type1_letters)
        else:
            mine_letter = random.choice(type2_letters)
        position = shuffled_mine_positions[i]
        events.append((time_str, 'mine', position, mine_letter, mine_type))

    # Add the last mine at exactly 00:02:50
    events.append((format_time(last_mine_appearance), 'mine', shuffled_mine_positions[-1], random.choice(type1_letters + type2_letters), shuffled_mine_types[-1]))
    mine_times.append(last_mine_appearance)

    # Create bonuses except the last one
    bonus_types = ["capturable"] * num_capturable_bonuses + ["incapturable"] * (num_bonuses - num_capturable_bonuses)
    shuffled_bonus_types = shuffle_with_constraints(bonus_types)

    for i, bonus_type in enumerate(shuffled_bonus_types[:-1]):
        current_time_bonus += int(time_step_bonus + random.uniform(-time_jitter, time_jitter))
        bonus_times.append(current_time_bonus)
        time_str = format_time(current_time_bonus)
        position = shuffled_bonus_positions[i]
        
        if bonus_type == "capturable":
            stimulus = "#_$"  # Capturable sequence
        else:
            # For incapturable bonuses, ensure the combination is not "#_$"
            while True:
                symbol1 = random.choice(["&", "#", "$", "@"])
                symbol2 = random.choice(["&", "#", "$", "@"])
                stimulus = f"{symbol1}_{symbol2}"
                if stimulus != "#_$":  # Ensure it's not the capturable sequence
                    break
        
        events.append((time_str, 'bonus', position, stimulus, bonus_type))

    # Add the last bonus at exactly 00:02:55
    events.append((format_time(last_bonus_appearance), 'bonus', shuffled_bonus_positions[-1], "#_$", shuffled_bonus_types[-1]))
    bonus_times.append(last_bonus_appearance)

    # Add end of the game entry
    end_time_str = format_time(game_duration)
    events.append((end_time_str, "game", "NA", "NA", "end"))

    # Sort events by time
    events.sort(key=lambda x: x[0])

    # Generate the output file name with mine letters, number of mines and bonuses
    file_name = f"scenario_{''.join(type1_letters)}_{num_mines}m_{num_bonuses}b.csv"

    # Write events to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['time', 'object', 'position', 'stimulus', 'info'])
        for event in events:
            writer.writerow(event)

    # Calculate min/max intervals
    mine_min_interval, mine_max_interval = calculate_time_intervals(mine_times)
    bonus_min_interval, bonus_max_interval = calculate_time_intervals(bonus_times)

    # Print detailed summary
    print(f"Scenario saved to {file_name}")
    print(f"Number of mines: {len(mine_times)} (Type-1: {mine_types.count('type-1')}, Type-2: {mine_types.count('type-2')})")
    print(f"Number of bonuses: {len(bonus_times)} (Capturable: {bonus_types.count('capturable')}, Incapturable: {bonus_types.count('incapturable')})")
    print(f"Mine intervals - Min: {mine_min_interval}s, Max: {mine_max_interval}s")
    print(f"Bonus intervals - Min: {bonus_min_interval}s, Max: {bonus_max_interval}s")

# Example usage:
generate_scenario()
