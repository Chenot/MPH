import csv
import random

# Constants
total_sounds = 160
block_size = 10
high_pitch_per_block = 2
low_pitch_per_block = block_size - high_pitch_per_block
time_values = [1.2, 1.35, 1.5, 1.65, 1.8]  # Predefined time intervals
total_duration = 240  # 4 minutes in seconds (16 blocks of 15 seconds each)
target_high_pitch = 32  # We need exactly 32 high-pitched sounds
target_frequency = 800  # Hz of the high pitch
notarget_frequency = target_frequency / 2  # Hz of the low pitch

# Function to generate a block with high-pitch sounds, ensuring no two consecutive high-pitch sounds
def generate_block(high_count, low_count, prev_last_sound=None):
    while True:
        block = ['low'] * low_count + ['high'] * high_count
        random.shuffle(block)
        
        # Ensure no two consecutive high-pitch sounds within the block
        valid_block = True
        for i in range(1, len(block)):
            if block[i] == 'high' and block[i - 1] == 'high':
                valid_block = False
                break

        # Ensure the first sound of the block is not 'high' if the last sound of the previous block was also 'high'
        if prev_last_sound == 'high' and block[0] == 'high':
            valid_block = False

        if valid_block:
            return block

# Function to generate a set of time intervals (two occurrences of each value in the block)
def generate_time_intervals():
    intervals = time_values * 2  # Repeat each time value twice
    random.shuffle(intervals)  # Shuffle the intervals
    return intervals

# Function to generate the entire oddball task scenario
def generate_oddball_scenario():
    while True:  # Keep regenerating until we have exactly 32 high-pitched sounds
        sound_sequence = []
        time_intervals = []
        high_count = 0  # Count the number of high-pitched sounds
        prev_last_sound = None  # Keep track of the last sound of the previous block

        # Generate blocks of sounds
        for i in range(total_sounds // block_size):
            # Generate the block and ensure no consecutive high-pitch sounds across blocks
            block = generate_block(high_pitch_per_block, low_pitch_per_block, prev_last_sound)

            # Count the number of high-pitched sounds in this block
            high_count += block.count('high')

            # Add the block to the sound sequence
            sound_sequence.extend(block)

            # Update the last sound of the current block for the next iteration
            prev_last_sound = block[-1]

            # For each block, generate and store the time intervals
            time_intervals.extend(generate_time_intervals())

        # Check if we have exactly 32 high-pitched sounds
        if high_count == target_high_pitch:
            break  # Exit the loop if the count is correct

    # Now calculate both time_trial and cumulative time
    cumulative_time = 1.0  # Start the first sound at 1 second
    csv_data = []
    low_count = 0
    for i in range(total_sounds):
        sound = sound_sequence[i]
        time_trial = time_intervals[i]  # Time interval for the current trial
        time = cumulative_time  # Cumulative time is the start time of the trial
        cumulative_time += time_trial  # Update cumulative time for the next trial
        
        frequency = int(target_frequency) if sound == 'high' else int(notarget_frequency)
        trial = i + 1  # Trial number starting from 1
        csv_data.append([f"{time:.2f}", f"{time_trial:.2f}", trial, sound, frequency])

        # Count the number of low sounds
        if sound == 'low':
            low_count += 1

    # Ensure the last sound ends exactly at 240 seconds by adjusting the last cumulative time
    if cumulative_time != 240:
        csv_data[-1][0] = "240.00"  # Set the last time to exactly 240 seconds

    # Save to CSV
    with open('oddball_task.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['time', 'time_trial', 'trial', 'sound', 'frequency'])
        writer.writerows(csv_data)

    # Print summary information
    print(f"CSV file 'oddball_task.csv' generated successfully!")
    print(f"Total number of trials: {total_sounds}")
    print(f"Total number of low-pitched sounds: {low_count}")
    print(f"Total number of high-pitched sounds: {target_high_pitch}")

# Call the function to generate the scenario
generate_oddball_scenario()
