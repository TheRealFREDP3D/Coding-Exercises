# ------------------------------------------------------------------------------- #
# tools.py - The script sets the SERPER_API_KEY environment variable to the value #
# of the SERPER_API_KEY environment variable.                                     #
# ------------------------------------------------------------------------------- #
# Author: CrewAI Documentation                                                    #
# Github: https://github.com/TheRealFREDP3D                                       #
# X: https://x.com/TheRealFredP3D                                                 #
# Date: 2024-07-15                                                                #
# ------------------------------------------------------------------------------- #

from dotenv import load_dotenv
load_dotenv()

import os
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

tool = SerperDevTool()
