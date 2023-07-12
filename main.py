import zntrack
from src.hello_world import HelloWorld

# Write the computational graph
with zntrack.Project() as project:
    hello_world = HelloWorld(max_number=256)
project.run()
