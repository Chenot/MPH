import random

# Parameters for 1-minute scenario (to be repeated 4 times)
num_sysmon_failures_lights = 1  # 4 total, 2 for lights-1, 2 for lights-2
num_sysmon_failures_scales = 1  # 1 for each scale-1 to scale-4
num_communications_own = 1  # 2 own communications
num_communications_other = 0  # 1 other communication
num_pump_off = 1  # 6 pumps, one off for each

minute_duration = 60  # time in seconds for one minute
max_time = minute_duration  # time for one minute
com_spacing = 15  # minimum time between communications
min_interval = 5  # minimum time interval for sysmon and pump events
last_com_time = 45  # last communication should be no later than 45 seconds per minute

# Sysmon failure generation
sysmon_lights = ['lights-1-failure', 'lights-2-failure']
sysmon_scales = [f'scales-{i}-failure' for i in range(1, 5)]

# Shuffling function to ensure no repeating patterns for pumps and other events
def shuffled_list(original_list):
    shuffled = original_list.copy()
    random.shuffle(shuffled)
    return shuffled

# Ensuring even distribution by generating times while respecting min_interval
def generate_event_times(num_events, duration, min_interval):
    available_times = list(range(min_interval, duration - min_interval))
    return sorted(random.sample(available_times, num_events))

# Generate the events for one minute, ensuring minimum interval and shuffle
def generate_minute_events(minute_offset):
    events = []
    
    # Generate times for sysmon failures (spread regularly across the time span)
    sysmon_times = generate_event_times(num_sysmon_failures_lights + num_sysmon_failures_scales, max_time, min_interval)
    sysmon_failures = shuffled_list(sysmon_lights * 2 + sysmon_scales)

    # Generate random times for pump off events with shuffle and min_interval
    pump_times = generate_event_times(num_pump_off, max_time, min_interval)
    pump_failures = shuffled_list([f'pump-{i + 1}-state;off' for i in range(6)])

    # Generate communication times with at least 15 seconds spacing
    com_times = []
    current_time = random.randint(min_interval, last_com_time - (com_spacing * (num_communications_own + num_communications_other - 1)))
    for _ in range(num_communications_own + num_communications_other):
        com_times.append(current_time)
        current_time += random.randint(com_spacing, com_spacing + 5)  # Ensuring at least 15 seconds between communications

    communications = shuffled_list(['radioprompt;own'] * num_communications_own + ['radioprompt;other'])

    # Generate sysmon events
    for time, failure in zip(sysmon_times, sysmon_failures):
        total_time = minute_offset + time
        minutes, seconds = divmod(total_time, 60)
        events.append((f"0:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}", f"sysmon;{failure};True"))

    # Generate communication events
    for time, com in zip(com_times, communications):
        total_time = minute_offset + time
        minutes, seconds = divmod(total_time, 60)
        events.append((f"0:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}", f"communications;{com}"))

    # Generate pump off events
    for time, pump in zip(pump_times, pump_failures):
        total_time = minute_offset + time
        minutes, seconds = divmod(total_time, 60)
        events.append((f"0:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}", f"resman;{pump}"))

    return events

# Output the generated events for 4 minutes
all_events = []
for minute in range(4):
    minute_offset = minute * minute_duration
    all_events.extend(generate_minute_events(minute_offset))

# Sort events by time
events_by_time = sorted(all_events)

# Sort events by task (sysmon, resman, communications)
events_by_task = sorted(all_events, key=lambda x: x[1].split(';')[0])

# Print events by time
print("# Events by Time")
for event in events_by_time:
    print(f"{event[0]};{event[1]}")

# Print events by task name
print("\n# Events by Task")
for event in events_by_task:
    print(f"{event[0]};{event[1]}")
