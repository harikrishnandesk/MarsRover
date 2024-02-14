# Rover Class
class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

    def move(self):
        movements = {
            'N': lambda x, y: (x, y + 1) if y < self.grid.size[1] - 1 else (x, y),
            'S': lambda x, y: (x, y - 1) if y > 0 else (x, y),
            'E': lambda x, y: (x + 1, y) if x < self.grid.size[0] - 1 else (x, y),
            'W': lambda x, y: (x - 1, y) if x > 0 else (x, y),
        }
        self.x, self.y = movements[self.direction](self.x, self.y)

    def turn_left(self):
        directions = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = directions[self.direction]

    def turn_right(self):
        directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = directions[self.direction]

    def send_status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."


# Grid Class
class Grid(GridComponent):
    def __init__(self, size):
        self.size = size
        self.obstacles = []

    def add_obstacle(self, position):
        obstacle = Obstacle()
        self.obstacles.append((position, obstacle))

    def move(self):
        print("Moving on the grid.")

        for obstacle_position, obstacle in self.obstacles:
            if (self.x, self.y) == obstacle_position:
                obstacle.move()
                return
