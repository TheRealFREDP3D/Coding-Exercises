# --------------------------------------------------------------------------- 
# MathProfessor.py - Python script to create agents and tasks with the crewai
# library. {Ollama} + {Llama3:latest}
# --------------------------------------------------------------------------- 
# Author: CrewAI Documentation
# Github: https://github.com/TheRealFREDP3D
# X: https://x.com/TheRealFredP3D
# Date: 2024-07-15
# ------------------------------------------------------------------------- 
# This code snippet is using the crewai library to create a Crew object 
# with one Agent object (general_agent) and one Task object (task). The
# Crew object is then used to execute the kickoff method with no input
# parameters. The result of the kickoff method is then printed.
# ---------------------------------------------------------------------------
# 
# ---------------------------------------------------------------------- 

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model = "crewai-llama3",
    base_url = "http://localhost:11434/v1")

general_agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm)
task = Task (description="""what is 3 + 5""",
             agent = general_agent,
             expected_output="A numerical answer.")

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

print(result)