class RiverCleanRobot:
    def __init__(self, max_capacity=10):
        # Initialize the robot's state and parameters
        self.trash_collected = 0
        self.max_capacity = max_capacity
    
    def move_forward(self):
        # Code to move the robot forward
        print("Moving forward")

    def turn_left(self):
        # Code to turn the robot left
        print("Turning left")

    def turn_right(self):
        # Code to turn the robot right
        print("Turning right")

    def collect_trash(self):
        # Code to collect trash
        print("Collecting trash")
        self.trash_collected += 1

    def check_for_trash(self):
        # Code to check for trash
        # For the purpose of this example, we'll randomly decide if there's trash
        import random
        return random.choice([True, False])

    def call_dumper(self):
        # Code to call the dumper
        print("Calling dumper to empty trash bin")
        self.trash_collected = 0

    def patrol_and_clean(self, steps):
        # Patrol the river and clean for a given number of steps
        for _ in range(steps):
            if self.check_for_trash():
                self.collect_trash()
                if self.trash_collected >= self.max_capacity:
                    self.call_dumper()
            self.move_forward()

    def patrol_and_clean_with_turns(self, steps):
        # Patrol the river and clean for a given number of steps, with random turns
        import random
        for _ in range(steps):
            if self.check_for_trash():
                self.collect_trash()
                if self.trash_collected >= self.max_capacity:
                    self.call_dumper()
            self.move_forward()
            # Randomly decide to turn left or right
            if random.choice([True, False]):
                self.turn_left()
            else:
                self.turn_right()

# Example usage
robot = RiverCleanRobot(max_capacity=5)
robot.patrol_and_clean(10)  # Patrol and clean for 10 steps
robot.patrol_and_clean_with_turns(20)  # Patrol and clean for 20 steps with random turns

print(f"Total trash collected: {robot.trash_collected}")
