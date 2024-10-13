# ------------------------------------------------------------------------------- 
# crewai.py - Python script to create agents and tasks with the crewai library.
# ------------------------------------------------------------------------------- 
# Author: Frederick Pellerin
# Github: https://github.com/TheRealFREDP3D
# X: https://x.com/TheRealFredP3D
# Date: 2024-07-15
# -------------------------------------------------------------------------------
# This code defines two tasks, research_task and write_task, each with a 
# description, expected output format, tools needed, the agent responsible for
# the task, and additional task-specific details like async_execution and output
# file. The tasks seem to involve research and writing, with specific 
# requirements for the output format and content.
# -------------------------------------------------------------------------------

from crewai import Task
from tools import tool
from agents import researcher,writer

# Creating a research_task Task object
# The Task object is initialized with various parameters such as description,
# expected_output, tools, agent, async_execution, and output_file
#
# The description parameter is a string that describes the task
# The expected_output parameter is a string that specifies the expected output format
# The tools parameter is a list of tools needed for the task
# The agent parameter is the agent responsible for completing the task
# The async_execution parameter specifies whether the task should be executed asynchronously
# The output_file parameter specifies the output file containing the final draft
#
# Note: The {topic} placeholder in the expected_output string will be replaced with the actual topic value
research_task= Task(description=(
    "Find useful learning ressources for {topic}. "
    "Focus on identifying pros and cons and the overall narrative. "
    "Your final report should clearly articulate the key points, "
    "its a roadmap to follow, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the new trending topics in {topic} formatted as markdown.',
  tools=[tool],
  agent=researcher)

# Creating a write_task Task object
# The Task object is initialized with various parameters such as description,
# expected_output, tools, agent, async_execution, and output_file
#
# The description parameter is a string that describes the task
# The expected_output parameter is a string that specifies the expected output format
# The tools parameter is a list of tools needed for the task
# The agent parameter is the agent responsible for completing the task
# The async_execution parameter specifies whether the task should be executed asynchronously
# The output_file parameter specifies the output file containing the final draft
#
# Note: The {topic} placeholder in the expected_output string will be replaced with the actual topic value
write_task = Task(description=(
    "Compose an insightful article on {topic}. "
    "Focus on the latest trends and how it's impacting the industry. "
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'  # output file containing final draft

)
