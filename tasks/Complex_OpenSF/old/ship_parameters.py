import math

# Ship movement parameters
ship_acceleration = 0.30
ship_max_vel = 6
ship_turn_speed = 6

# Ship start parameters
ship_radius = 12                # probably related to collision
ship_hit_points = 4             # ship health
ship_orientation = 90           # Ship starts pointing north
ship_pos_x = 245                # ship starts on the left of the center (may require adjustment)
ship_pos_y = 315                # ship starts on the left of the center (may require adjustment)
ship_vel_x = 0                  # ship starts with no movement
ship_vel_y = 0                  # ship starts with no movement
ship_acceleration_start = 0     # ship starts with no acceleration
ship_thrust_start = False       # ship starts without thrust
ship_turn_left_start = False    # ship starts without turning
ship_turn_right_start = False   # ship starts without turning


class Ship:
    def __init__(self):
        """Initialize or reinitialize the ship with default parameters.""" # Start position or restart position after being destroy
        self.collision_radius = ship_radius
        self.position = {'x': ship_pos_x, 'y': ship_pos_y}
        self.velocity = {'x': ship_vel_x, 'y': ship_vel_y}
        self.orientation = ship_orientation
        self.thrust_flag = ship_thrust_start
        self.turn_left_flag = ship_turn_left_start
        self.turn_right_flag = ship_turn_right_start
        self.acceleration = ship_acceleration_start
        self.acceleration_factor = ship_acceleration
        self.health = ship_hit_points
        self.max_vel = ship_max_vel
        self.turn_speed = ship_turn_speed

    def compute(self, world_width, world_height):
        """Update ship state based on control inputs and physics."""
        # Update orientation based on turn flags
        if self.turn_left_flag:
            self.orientation = (self.orientation + self.turn_speed) % 360
        elif self.turn_right_flag:
            self.orientation = (self.orientation - self.turn_speed) % 360

        # Update acceleration based on thrust
        self.acceleration = self.acceleration_factor if self.thrust_flag else 0

        # Update velocity based on acceleration and orientation
        self.velocity['x'] += self.acceleration * math.cos(math.radians(self.orientation))
        self.velocity['y'] += self.acceleration * math.sin(math.radians(self.orientation))

        # Clamp velocity to max velocity
        self.velocity['x'] = max(min(self.velocity['x'], self.max_vel), -self.max_vel)
        self.velocity['y'] = max(min(self.velocity['y'], self.max_vel), -self.max_vel)

        # Update position based on velocity
        self.position['x'] = (self.position['x'] + self.velocity['x']) % world_width
        self.position['y'] = (self.position['y'] - self.velocity['y']) % world_height
