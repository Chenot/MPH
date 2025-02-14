import random
from datetime import timedelta
import yaml

# CONFIGURATION VARIABLES
experiment_name = 'expename'

config_general = {
    'sound': True,
    'allow_pause': True,
    'pause_overlay': True
}

config_graphics = {
    'display_mode': 'full_screen',
    'show_fps': False,
    'line_width': 1,
    'border_thickness': 2
}

config_scoring = {
    'missile_points': 0,
    'letters': ['A', 'B', 'C']
}

config_defaults = {
    'mines': {
        'ttl': 10,
        'expected_key': 'J'
    }
}

config_lsl = [
    {'stream_inlet': 'sf_lslin'},
    {'stream_outlet': 'sf_lslout_keys', 'event_types': ['keys']}
]

navigation_pages = {
    'title_screen': {'type': 'title'},
    'easy_game': {'type': 'game', 'scenario': 'easy_scenario', 'enable_lsl': True},
    'score_easy': {'type': 'score'},
    'mines': {'type': 'instruction_mine'},
    'hard_game': {'type': 'game', 'scenario': 'hard_scenario'},
    'score_hard': {'type': 'score'},
    'end': {'type': 'end'}
}

navigation_links = {
    'title_screen': {'space': 'easy_game'},
    'easy_game': {'_': 'score_easy'},
    'score_easy': {'space': 'hard_game'},
    'hard_game': {'_': 'score_hard'},
    'score_hard': {'space': 'end'}
}

navigation_initial = 'title_screen'

# GAME VARIABLES
game_duration = 240  # in seconds (4 minutes)
time_jitter = 3  # Time jitter to prevent regular intervals of mines and bonuses in seconds

# Ship parameters
ship_missiles = 50  # number of missiles in the ship at the start

# Bonuses
num_bonus_pairs = int(game_duration/8)  # Approximately one pair of bonus every 8 seconds.
num_capturable_bonuses = int(num_bonus_pairs * 0.5)  # 50% of capturable bonuses
last_bonus_appearance = int(game_duration - 5)  # Last bonus will appear exactly 5 seconds before the end of the game
bonus_pair_time_interval = 3  # 3 seconds between the first and second symbols in a bonus pair
bonus_ttl = 2  # Each symbol (bonus) is shown for 2 seconds
bonus_ttl_key = 3  # When valid, a bonus can be captured for 3 seconds after it is shown
BONUS_POSITIONS = [
    "near_north_west", "near_north", "near_north_east", "near_east",
    "near_south_east", "near_south", "near_south_west", "near_west",
    "far_north_west", "far_north", "far_north_east", "far_east",
    "far_south_east", "far_south", "far_south_west", "far_west"
]

# Mines
num_mines = int(game_duration/12)  # Approximately one mine every 12 seconds.
num_type2_mines = int(num_mines * 0.5)  # 50% of type-2 mines
mine_ttl = 10  # Each mine will live for 10 seconds
last_mine_appearance = int(game_duration - 10)  # Last mine will appear exactly 10 seconds before the end of the game
MINE_POSITIONS = ["opposite", "horizontal", "vertical"]


# Function to convert seconds into HH:MM:SS format
def format_time(seconds):
    return str(timedelta(seconds=seconds))


# Function to initialize the three letters for type-2 mines
def initialize_mine_letters():
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)  # Three random letters for type-2 mines
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


# Function to parse timestamp string into total seconds for sorting
def parse_time_to_seconds(time_str):
    parts = time_str.split(':')
    try:
        parts = [int(part) for part in parts]
    except ValueError:
        # Handle cases where time_str might not be properly formatted
        return 0
    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        hours = 0
        minutes, seconds = parts
    elif len(parts) == 1:
        hours = 0
        minutes = 0
        seconds = parts[0]
    else:
        # Unexpected format
        return 0
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


# Function to generate the scenario in YAML format
def generate_scenario_yaml():
    # Time step excludes the final appearance of the last mine and bonus
    time_step_mine = (last_mine_appearance) / (num_mines - 1)  # All mines except the last one
    time_step_bonus = (last_bonus_appearance - bonus_pair_time_interval) / (num_bonus_pairs - 1)  # All bonuses except the last one

    current_time_mine = 0
    current_time_bonus = 0

    type2_letters = initialize_mine_letters()
    type1_letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letter not in type2_letters]

    # Create exactly num_type2_mines of type-2 and the rest as type-1
    mine_types = ["type-2"] * num_type2_mines + ["type-1"] * (num_mines - num_type2_mines)
    shuffled_mine_types = shuffle_with_constraints(mine_types)

    # Distribute mine positions based on rules
    mine_positions = distribute_mine_positions(num_mines)
    shuffled_mine_positions = shuffle_with_constraints(mine_positions)

    # Shuffle bonus positions
    shuffled_bonus_positions = shuffle_bonus_positions(num_bonus_pairs)

    events_hard_scenario = []
    mine_times = []
    bonus_times = []

    mine_id = 1
    bonus_id = 1

    # Generate mines except the last one
    for i, mine_type in enumerate(shuffled_mine_types[:-1]):
        current_time_mine += int(time_step_mine + random.uniform(-time_jitter, time_jitter))
        mine_times.append(current_time_mine)
        time_str = format_time(current_time_mine)
        mine_letter = random.choice(type2_letters) if mine_type == "type-2" else random.choice(type1_letters)
        position = shuffled_mine_positions[i]

        # Build the event dictionary
        event_entry = {
            "timestamp": time_str,
            "events": [{
                "event": "pop_mine",
                "id": f"m{mine_id}",
                "location": position,
                "letter": mine_letter,
                "log": f"mine_{mine_type}"
            }]
        }

        # Add foe type
        event_entry["events"][0]["foe"] = mine_type

        events_hard_scenario.append(event_entry)
        mine_id += 1

    # Add the last mine at exactly 10 seconds before the end
    last_mine_type = shuffled_mine_types[-1]
    last_mine_letter = random.choice(type2_letters if last_mine_type == "type-2" else type1_letters)
    last_mine_position = shuffled_mine_positions[-1]
    time_str = format_time(last_mine_appearance)
    event_entry = {
        "timestamp": time_str,
        "events": [{
            "event": "pop_mine",
            "id": f"m{mine_id}",
            "location": last_mine_position,
            "letter": last_mine_letter,
            "log": f"mine_{last_mine_type}"
        }]
    }

    # Add foe type
    event_entry["events"][0]["foe"] = last_mine_type

    events_hard_scenario.append(event_entry)
    mine_times.append(last_mine_appearance)

    # Create bonuses, handling the last bonus separately
    bonus_types = ["valid"] * num_capturable_bonuses + ["invalid"] * (num_bonus_pairs - num_capturable_bonuses)
    shuffled_bonus_types = shuffle_with_constraints(bonus_types)

    for i, bonus_type in enumerate(shuffled_bonus_types[:-1]):  # Exclude the last bonus
        current_time_bonus += int(time_step_bonus + random.uniform(-time_jitter, time_jitter))
        bonus_times.append(current_time_bonus)
        time_str_1 = format_time(current_time_bonus)
        time_str_2 = format_time(current_time_bonus + bonus_pair_time_interval)
        position = shuffled_bonus_positions[i]

        # Assign symbol pairs
        if bonus_type == "valid":
            symbol_1 = "#"
            symbol_2 = "$"
            symbol_n_1 = 1
            symbol_n_2 = 2
        else:
            while True:
                symbol1 = random.choice(["&", "#", "$", "@"])
                symbol2 = random.choice(["&", "#", "$", "@"])
                if not (symbol1 == "#" and symbol2 == "$"):  # Ensure it's not the valid sequence
                    symbol_1 = symbol1
                    symbol_2 = symbol2
                    symbol_n_1 = 1
                    symbol_n_2 = 2
                    break

        # First symbol of the pair (pop_bonus)
        event_entry_1 = {
            "timestamp": time_str_1,
            "events": [{
                "event": "pop_bonus",
                "id": f"b{bonus_id}",
                "location": position,
                "symbol": symbol_1,
                "symbol_n": symbol_n_1,
                "validity": bonus_type,
                "log": f"bonus_symbol_{symbol_1}"
            }]
        }
        events_hard_scenario.append(event_entry_1)

        # Second symbol of the pair
        if bonus_type == "valid" and symbol_2 == "$":
            event_entry_2 = {
                "timestamp": time_str_2,
                "events": [{
                    "event": "pop_bonus_valid",
                    "id": f"b{bonus_id}",
                    "location": position,
                    "symbol": symbol_2,
                    "symbol_n": symbol_n_2,
                    "validity": bonus_type,
                    "expected_bonus_key": "L",
                    "expected_missile_key": "K",
                    "ttl_key": bonus_ttl_key,
                    "log": f"bonus_symbol_{symbol_2}"
                }]
            }
        else:
            event_entry_2 = {
                "timestamp": time_str_2,
                "events": [{
                    "event": "pop_bonus",
                    "id": f"b{bonus_id}",
                    "location": position,
                    "symbol": symbol_2,
                    "symbol_n": symbol_n_2,
                    "validity": bonus_type,
                    "log": f"bonus_symbol_{symbol_2}"
                }]
            }
        events_hard_scenario.append(event_entry_2)

        bonus_id += 1

    # Now, handle the last bonus to appear exactly 5 seconds before the end
    last_bonus_type = shuffled_bonus_types[-1]
    position = shuffled_bonus_positions[-1]
    bonus_start_time = last_bonus_appearance - bonus_pair_time_interval  # Start time for the first symbol

    time_str_1 = format_time(bonus_start_time)
    time_str_2 = format_time(last_bonus_appearance)

    # Assign symbol pairs for the last bonus
    if last_bonus_type == "valid":
        symbol_1 = "#"
        symbol_2 = "$"
        symbol_n_1 = 1
        symbol_n_2 = 2
    else:
        while True:
            symbol1 = random.choice(["&", "#", "$", "@"])
            symbol2 = random.choice(["&", "#", "$", "@"])
            if not (symbol1 == "#" and symbol2 == "$"):  # Ensure it's not the valid sequence
                symbol_1 = symbol1
                symbol_2 = symbol2
                symbol_n_1 = 1
                symbol_n_2 = 2
                break

    # First symbol of the last pair (pop_bonus)
    event_entry_1 = {
        "timestamp": time_str_1,
        "events": [{
            "event": "pop_bonus",
            "id": f"b{bonus_id}",
            "location": position,
            "symbol": symbol_1,
            "symbol_n": symbol_n_1,
            "validity": last_bonus_type,
            "log": f"bonus_symbol_{symbol_1}"
        }]
    }
    events_hard_scenario.append(event_entry_1)

    # Second symbol of the last pair
    if last_bonus_type == "valid" and symbol_2 == "$":
        event_entry_2 = {
            "timestamp": time_str_2,
            "events": [{
                "event": "pop_bonus_valid",
                "id": f"b{bonus_id}",
                "location": position,
                "symbol": symbol_2,
                "symbol_n": symbol_n_2,
                "validity": last_bonus_type,
                "expected_bonus_key": "L",
                "expected_missile_key": "K",
                "ttl_key": bonus_ttl_key,
                "log": f"bonus_symbol_{symbol_2}"
            }]
        }
    else:
        event_entry_2 = {
            "timestamp": time_str_2,
            "events": [{
                "event": "pop_bonus",
                "id": f"b{bonus_id}",
                "location": position,
                "symbol": symbol_2,
                "symbol_n": symbol_n_2,
                "validity": last_bonus_type,
                "log": f"bonus_symbol_{symbol_2}"
            }]
        }
    events_hard_scenario.append(event_entry_2)
    bonus_id += 1

    # Add end of the game entry
    events_hard_scenario.append({
        "timestamp": format_time(game_duration),
        "events": [{
            "event": "game_end",
            "log": "game_end"  # Added log for consistency
        }]
    })

    # Sort events by timestamp
    events_hard_scenario.sort(key=lambda e: parse_time_to_seconds(e['timestamp']))

    # Now build the output dictionary
    output = {
        "experiment": {
            "name": experiment_name,
            "config": {
                "general": config_general,
                "graphics": config_graphics,
                "scoring": config_scoring,
                "defaults": config_defaults,
                "lsl": config_lsl
            },
            "navigation": {
                "pages": navigation_pages,
                "links": navigation_links,
                "initial": navigation_initial
            },
            "scenarios": {
                "hard_scenario": {
                    "steps": events_hard_scenario
                }
            }
        }
    }

    # Write YAML to file
    file_name = f"scenario_{''.join(type2_letters)}_{num_mines}m_{num_bonus_pairs * 2}b.yaml"
    with open(file_name, 'w') as yaml_file:
        yaml.dump(output, yaml_file, default_flow_style=False, sort_keys=False)

    print(f"Scenario saved to {file_name}")

    # ================================
    # Print Events Table (Sorted by Timestamp)
    # ================================

    # Prepare table headers
    headers = ["Timestamp", "Event", "Log"]

    # Collect table rows
    table_rows = []
    for event_entry in events_hard_scenario:
        timestamp = event_entry.get("timestamp", "")
        for sub_event in event_entry.get("events", []):
            event_name = sub_event.get("event", "")
            log = sub_event.get("log", "")
            table_rows.append([timestamp, event_name, log])

    # Sort the table_rows based on the parsed timestamp
    table_rows.sort(key=lambda row: parse_time_to_seconds(row[0]))

    # Determine column widths based on the sorted table_rows
    col_widths = [len(header) for header in headers]
    for row in table_rows:
        for idx, item in enumerate(row):
            if len(str(item)) > col_widths[idx]:
                col_widths[idx] = len(str(item))

    # Function to create a separator line
    def separator_line(widths):
        line = "+"
        for width in widths:
            line += "-" * (width + 2) + "+"
        return line

    # Function to format a row
    def format_row(row, widths):
        formatted = "|"
        for idx, item in enumerate(row):
            formatted += " " + str(item).ljust(widths[idx]) + " |"
        return formatted

    # Print the sorted table
    print("\n" + separator_line(col_widths))
    print(format_row(headers, col_widths))
    print(separator_line(col_widths))
    for row in table_rows:
        print(format_row(row, col_widths))
    print(separator_line(col_widths))
    # ================================
    # End of Print Table code
    # ================================


# Generate the scenario
generate_scenario_yaml()
