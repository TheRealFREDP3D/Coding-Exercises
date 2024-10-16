# --------------------------------------------------------------------------- 
# agents.py - Python script to create agents with the crewai library.
# --------------------------------------------------------------------------- 
# Author: Frederick Pellerin
# Github: https://github.com/TheRealFREDP3D
# X: https://x.com/TheRealFredP3D
# Date: 2024-07-15
# --------------------------------------------------------------------------- 
# This code snippet is importing necessary modules and setting up two agents, 
# researcher and writer, using the Agent class from the crewai library.
#
# The Agent class is initialized with various parameters such as role, goal, 
# backstory, tools, llm, allow_delegation, verbose, and memory.
#
# The llm parameter is an instance of the ChatGoogleGenerativeAI class from 
# the langchain_google_genai library, which is initialized with specific 
# parameters such as model, verbose, temperature, and google_api_key (which 
# is retrieved from the environment variables using os.getenv).
#
# The agents are created with different roles and goals, and they share the 
# same llm instance. The allow_delegation parameter is set to True for the 
# researcher agent and False for the writer agent.
# --------------------------------------------------------------------------- 

# Importing the Agent class from the crewai library
from crewai import Agent

# Importing the Ollama class from the langchain_community.llms library
from langchain_community.llms import Ollama

llm = Ollama(
    model = "llama3.1:latest",
    base_url = "http://localhost:11434/",    
)

# Creating an instance of the Agent class for the Senior Researcher role
# The Agent class is initialized with various parameters such as role, goal, backstory, tools, llm, allow_delegation, verbose, and memory
researcher_agent = Agent(
    role = "Senior Researcher", # The role of the agent
    goal = """Uncover groundbreaking topics 
    in {topic}""", # The goal of the agent
    backstory = ("""Driven by curiosity, you are at the forefront of Innovation sharing 
    knowledge and news that would change the world"""), # The backstory or background of the agent
    tools = [], # The tools used by the agent
    llm = llm, # The language model used by the agent
    allow_delegation = True, # Allowing the agent to delegate tasks
    verbose = True, # Enabling verbose mode for debugging purposes
    memory = True # Enabling memory storage for the agent
)

# Creating an instance of the Agent class for the Writer role
writer_agent = Agent(
    role = "Writer", # The role of the agent
    goal = "Narrate compelling tech stories about {topic}", # The goal of the agent
    backstory = ("""Your expertise lies in breaking down complex topics into simpler and 
    digestible knowledge, you specialize in captivating audience attention with your 
    writing and create engaging narratives and stories"""), # The backstory or background of the agent
    tools = [], # The tools used by the agent
    llm = llm, # The language model used by the agent
    allow_delegation = True, # Not allowing the agent to delegate tasks
    verbose = True, # Enabling verbose mode for debugging purposes
    memory = True # Enabling memory storage for the agent
)

