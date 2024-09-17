import zntrack

from random import randrange


class HelloWorld(zntrack.Node):
    """Define a ZnTrack Node"""
    # parameter to be tracked
    max_number: int = zntrack.params()
    # parameter to store as output
    random_number: int = zntrack.metrics()

    def run(self):
        """Command to be run by DVC"""
        self.random_number = randrange(self.max_number)
