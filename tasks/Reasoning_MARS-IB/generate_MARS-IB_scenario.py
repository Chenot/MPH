import csv
import random

# Define the practice data
practice = [
  {"item": 3, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 1, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 2, "distractor": "pd", "shape_set": 3, "form": 1},
]

# Define the test data for test form 1
test_form_1 = [
  {"item": 55, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 30, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 64, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 45, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 35, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 72, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 27, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 79, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 29, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 24, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 42, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 54, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 17, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 58, "distractor": "md", "shape_set": 3, "form": 1},
  {"item": 73, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 36, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 63, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 75, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 74, "distractor": "pd", "shape_set": 3, "form": 1},
  {"item": 76, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 80, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 66, "distractor": "pd", "shape_set": 2, "form": 1},
  {"item": 21, "distractor": "pd", "shape_set": 1, "form": 1},
  {"item": 78, "distractor": "pd", "shape_set": 1, "form": 1},
]

# Define blocks
blocks = [
    {"block": "practice", "block_n": 1, "data": practice},
    {"block": "test", "block_n": 1, "data": test_form_1}
]

# Randomize the placement of the correct answer across opt1 to opt4 for the test block
randomized_positions = [1, 2, 3, 4] * 6  # Create a list of positions for 24 trials (6 times each position)
random.shuffle(randomized_positions)  # Shuffle the list to randomize positions

# Generate the CSV file
with open('MARS-IB_scenario.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["block", "block_n", "trial", "image_file_main", "image_file_opt1", "image_file_opt2", "image_file_opt3", "image_file_opt4", "correct_resp"])

    # Loop through each block and write to CSV
    trial_counter = 0
    for block in blocks:
        block_name = block["block"]
        block_n = block["block_n"]
        block_data = block["data"]

        for idx, entry in enumerate(block_data, start=1):
            item = entry["item"]
            distractor = entry["distractor"]
            shape_set = entry["shape_set"]
            form = entry["form"]

            # Correct answer is always T1
            correct_answer = f"ressources/mars_{item}_T1_ss{shape_set}_{distractor}.jpeg"

            # For the test block, use pseudorandomized positions
            if block_name == "test":
                trial_counter += 1
                correct_position = randomized_positions[trial_counter - 1]
                # Exclude the correct answer from options
                options = [
                    f"ressources/mars_{item}_T2_ss{shape_set}_{distractor}.jpeg",
                    f"ressources/mars_{item}_T3_ss{shape_set}_{distractor}.jpeg",
                    f"ressources/mars_{item}_T4_ss{shape_set}_{distractor}.jpeg",
                ]
                random.shuffle(options)  # Shuffle other options
                # Insert the correct answer at the randomized correct position
                options.insert(correct_position - 1, correct_answer)
            else:
                # For the practice block, randomly shuffle the options including the correct answer
                options = [
                    f"ressources/mars_{item}_T1_ss{shape_set}_{distractor}.jpeg",
                    f"ressources/mars_{item}_T2_ss{shape_set}_{distractor}.jpeg",
                    f"ressources/mars_{item}_T3_ss{shape_set}_{distractor}.jpeg",
                    f"ressources/mars_{item}_T4_ss{shape_set}_{distractor}.jpeg",
                ]
                random.shuffle(options)
                # Find the position of the correct answer
                correct_position = options.index(correct_answer) + 1

            # Write the row with the correct answer's position
            writer.writerow([
                block_name,
                block_n,
                idx,
                f"ressources/mars_{item}_M_ss{shape_set}.jpeg",
                options[0],
                options[1],
                options[2],
                options[3],
                correct_answer
            ])

print("CSV file 'MARS-IB_scenario.csv' has been generated successfully.")
