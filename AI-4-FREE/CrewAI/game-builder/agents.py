from crewai import Agent
from langchain_community.llms import Ollama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model = "gemma2:latest",
    base_url = "http://localhost:11434")


from textwrap import dedent
from crewai import Agent
from langroid import llm_response_batch


class GameAgents():
    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            goal='Create software as needed',
            backstory=dedent("""\
                You are a Senior Software Engineer at a leading tech think tank.
                Your expertise in programming in python. and do your best to
                produce perfect code"""),
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
          goal='create prefect code, by analizing the code that is given for errors',
          backstory=dedent("""\
                You are a software engineer that specializes in checking code
              for errors. You have an eye for detail and a knack for finding
                hidden bugs.
              You check for missing imports, variable declarations, mismatched
                brackets and syntax errors.
              You also check for security vulnerabilities, and logic errors"""),
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
          goal='Ensure that the code does the job that it is supposed to do',
          backstory=dedent("""\
                You feel that programmers always do only half the job, so you are
                super dedicate to make high quality code."""),
            allow_delegation=True,
            verbose=True,
            llm=llm,
        )