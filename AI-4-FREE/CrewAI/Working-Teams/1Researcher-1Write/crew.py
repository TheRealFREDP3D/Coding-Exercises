# ------------------------------------------------------------------------------- 
# crewai.py - Pythomon script to create agents and tasks with the crewai library.
# ------------------------------------------------------------------------------- 
# Author: Frederick Pellerin
# Github: https://github.com/TheRealFREDP3D
# X: https://x.com/TheRealFredP3D
# Date: 2024-07-15
# ------------------------------------------------------------------------------- 
# This Python script is using the crewai library to create a Crew object with 
# two Agent objects (researcher and writer) and two Task objects 
# (research_task and write_task). The Crew object is then used to execute the
# kickoff method with some input parameters. The result of the kickoff method
# is then printed.
# ------------------------------------------------------------------------------- 

from crewai import Crew, Process 
from task import research_task, write_task  
from agents import researcher, writer  

def create_crew():
    """
    Create a crew object with two Agent objects (researcher and writer) and two Task objects (research_task and write_task).

    Returns:
        Crew: The created crew object.
    """
    return Crew(agents=[researcher, writer],  # Creating a crew object with the specified agents and tasks
               tasks=[research_task, write_task],
               process=Process.sequential)  # Using a sequential process for the crew


def execute_kickoff():
    """
    Execute the kickoff method with some input parameters.

    This function prompts the user to enter a topic and creates a crew object
    with the specified agents and tasks. It then executes the kickoff method of
    the crew object with the specified inputs, which in this case is a dictionary
    with a single key-value pair where the key is "topic" and the value is the
    topic entered by the user. The result of the kickoff method is then returned.

    Returns:
        dict: The result of the kickoff method.
    """
    # Prompt the user to enter a topic
    topic = input("Enter the topic: ")

    # Create a crew object with the specified agents and tasks
    crew = create_crew()

    # Execute the kickoff method of the crew object with the specified inputs
    # The inputs are a dictionary with a single key-value pair where the key is
    # "topic" and the value is the topic entered by the user
    result = crew.kickoff(inputs={"topic": topic})

    # Return the result of the kickoff method
    return result


if __name__ == "__main__":
    result = execute_kickoff()  # Executing the kickoff method and storing the result in the result variable
    print(result)  # Printing the result to the console

