class Door:
    def __init__(self, color, material, status):
        self.color = color
        self.material = material
        self.status = status

    def get_door(self):
        print("The color is {}, made of {} material and it\'s {}".format(self.color, self.material, self.status))

adoor = Door('Brown', 'wooden', 'open')
adoor.get_door()
print("\n") #The end of this class. It just adds a new line to the program

#OR Make2017$$

"""
class Door:
    def __init__(self, color, material, status):
        self.color = color
        self.material = material
        self.status = status

    def get_color(self):
        print("The color is {}".format(self.color))

    def get_material(self):
        print("The material is {}".format(self.material))

    def get_status(self):
        print("The door status is {}".format(self.status))

door = Door('white', 'wooden', 'open')
door.get_color()
door.get_material()
door.get_status()
"""


class pet:
    number_of_legs = 0

    def sleep(self):
        print ("zzz")

    def count_legs(self):
        print ("I have %s legs" % self.number_of_legs)


doug = pet()
doug.number_of_legs = 4
doug.count_legs()

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()
print("\n") #This is the end of this class


class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod #This is a decorator. it's the short form of how_many = classmethod(how_many).
    # It is simply used to tell Python that the next function nis a class function
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()