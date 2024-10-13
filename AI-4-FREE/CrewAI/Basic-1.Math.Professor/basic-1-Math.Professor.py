from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model = "mistral-7b-instruct:latest",
    base_url = "http://localhost:11434")

general_agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution. You always are entertaining, funny, with a love for dark comedy.""",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm)

task = Task(description="""Demonstrate Phytagore Theorem to a class of Software Engineers. Make it ludic and  fun for them. You must take your rime to explain step-by-step what you are doing. You can use visual material in .md format, using mermaid or mindmaps. Any information that could add value to your course should be included.""",
             agent = general_agent,
             expected_output="A markdown format courses about the Pythagore Theorem")

crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

print(result)
