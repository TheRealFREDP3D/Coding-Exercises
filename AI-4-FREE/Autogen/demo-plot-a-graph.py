# ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
# │ autogen_ollama_gemma2_demo.py                                                                                    │
# │-================================================================================================================-│
# │                                                                                                                  │
# │ Python 3.x.x                                                                                                     │ 
# │ Author: Frederick Pellerin                                                                                       │ 
# │ Email: fredp3d@proton.me                                                                                         │ 
# │ X/Github/Medium: @TheRealFredP3D                                                                                 │ 
# │                                                                                                                  │
# │-================================================================================================================-│
# │                                                                                                                  │   
# │ This script demonstrate how to make Autogen agent works using open-source LLM models with local Ollama server.   │
# │                                                                                                                  │
# │-================================================================================================================-│
# │                                                                                                                  │
# │ In this case, the model is Gemma2 served by a local Ollama server.                                               │
# │ The test is successful and here is the code to make it run.                                                      │
# │                                                                                                                  │
# │-================================================================================================================-│
# │                                                                                                                  │
# │ Workflow                                                                                                         │
# │                                                                                                                  │
# │ Agent #1 - Assistant: Create a script to fetch the data and plot a chart of NVDA and TESLA price change YTD.     │
# │ Agent #2 - User Proxy: Write the script in the ./coding directory and execute it.                                │
# │                                                                                                                  │
# │-================================================================================================================-│
# │                                                                                                                  │
# │ WARNING: When asked, be sure to check the generated code before continuing to ensure it is safe to run.          │
# │                                                                                                                  │
# └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

import autogen
import os
from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "config_list": [
        {
            "model": "gemma2:latest",
            "api_key": "ollama",
            "base_url": "http://127.0.0.1:11434/v1"
        }
    ]
}

# print(llm_config)

assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
)

# Start Chat here

user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD.",
)