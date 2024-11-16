from crewai import Agent, Task, Crew, LLM
import os

llm = LLM(
    model = "ollama/gemma:2b",
)

Math_Teacher_Agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution. You always are entertaining, funny, with a love for dark comedy.""",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm)

Teaching_Task = Task(description=f"""
                            Give a class about {topic}. Make it ludic and fun for the students. 
                            You must take your time and use step-by-step explanation.
                            You can use visual material in .md format, using mermaid or mindmaps. 
                            Any information that could add value to your course should be included.
                            """,
             agent = Math_Teacher_Agent,
             expected_output=f"A complete course about the {topic}")

crew = Crew(
            agents=[Math_Teacher_Agent],
            tasks=[Teaching_Task],
            verbose=True
            
        )

topic = input('What topic you want to learn?')
result = crew.kickoff()

print(result)

    