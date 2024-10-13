# pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29

from crewai import Agent, Task, Crew
import os
# Setup up the notebook to use Ollama. Model gemma2:latest"
from langchain_community.llms import Ollama
# from crewai_tools import SerperDevTool
# os.environ["SERPER_API_KEY"] = "6a342062643da99e239823cb8d52b344535ca74c"



os.environ["OPENAI_API_KEY"] = "NA"
llm = Ollama(model="llama3", base_url="http://localhost:11434")

# Serper Dev Tool

# Creating Agents

planner = Agent(
    role="Senior Content Planner",
    goal="Plan engaging and accurate content on {topic} using a unique persptive",
    backstory="You're working on planning a blog article "
    "about the topic: {topic}."
    "You gather information for the curious audience "
    "who wish to learn something new "
    "and make informed decisions. "
    "You work for the senior writer who provides needs you to to have a solid outline "
    "to build the blog article."
    "Your work is given as an outline for the Content Writer to write an article on this topic."
    "You can add suggestions if something is missing and pertinent to include in the article."
    "A mermaid diagram is expected with the final text, keep a list of key words and a step-by-step "
    "workflow of the crew actions",
    allow_delegation=True,
    verbose=True,
    # Tools,
    human_input_mode="a",
    llm=llm,
)


# Agent: Writer

writer = Agent(
    role="Content Writer",
    goal="Write factually accurate and pertinent "
    "opinion piece about the topic: {topic}",
    backstory="You're working on writing "
    "a new opinion piece about the topic: {topic}. "
    "You base your writing on the work of "
    "the Content Planner, who provides an outline "
    "and relevant context about the topic. "
    "You follow the main objectives and "
    "direction of the outline, "
    "as provide by the Content Planner. "
    "You also provide objective and impartial insights "
    "and back them up with information "
    "provide by the Content Planner. "
    "You add a touch of humour to the article. "
    "You acknowledge in your opinion piece "
    "when your statements are opinions "
    "as opposed to objective statements."
    "You keep in mind to explain everything like everybody was new to the subject"
    "Use a step-by-step workflow"
    "You prepare a list of key words to later tag the published article, "
    "A mermaid diagram of the article writing plan will be outputted with the final text",
    allow_delegation=False,
    verbose=True,
    llm=llm,
)


# Agent: Editor

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with "
    "the writing style of the author @TheRealFredP3D. ",
    backstory="You are an editor who receives a blog post "
    "from the Content Writer. "
    "Your goal is to review the blog post "
    "to ensure that it follows journalistic best practices,"
    "provides balanced viewpoints "
    "when providing opinions or assertions, "
    "and also avoids major controversial topics "
    "or opinions when possible"
    "The text must be entertaining and engaging. "
    "You make sure the mermaid diagram is accurate and coherent with the final text",
    allow_delegation=False,
    verbose=True,
    llm=llm,
)


# Creating Tasks

# Task: Plan

plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, "
        "and noteworthy news on {topic}.\n"
        "2. Identify the target audience, considering "
        "their interests and pain points. Assume the audiance is male, 20-30, technology nerds\n"
        "3. Develop a detailed content outline including "
        "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="1. A comprehensive content plan document "
    "with an outline, audience analysis, "
    "SEO keywords, and resources."
    "A mermaid diagram of the text plan",
    agent=planner,
)


# Task: Write

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
        "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Sections/Subtitles are properly named "
        "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
        "engaging introduction, insightful body, "
        "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
        "alignment with the brand's voice.\n"
        "6. A mermaid diagram of the text plan\n"
    ),
    expected_output="1. A well-written blog post "
    "in markdown format, ready for publication, "
    "each section should have 2 or 3 paragraphs."
    "2. A mermaid diagram of the text plan",
    agent=writer,
)


# Task: Edit

edit = Task(
    description=(
        "Proofread the given blog post for "
        "grammatical errors and "
        "alignment with the brand's voice."
    ),
    expected_output="A well-written blog post in markdown format, "
    "ready for publication, "
    "each section should have 2 or 3 paragraphs."
    "A final version of the blog post with a mermaid diagram of the text plan.",
    agent=editor,
)


# Creating the Crew

crew = Crew(agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=2)


# Running the Crew

topic = input("Article subject:")
result = crew.kickoff(inputs={"topic": topic})
