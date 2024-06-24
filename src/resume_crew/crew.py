from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

@CrewBase
class ResumeCrewCrew():
    """ResumeCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm_provider = 'openai'
        self.llm = self._get_llm()
        self.tools = self._get_tools()

    def _get_llm(self):
        if self.llm_provider == 'openai':
            return ChatOpenAI(model="gpt-4o", temperature=0.5)

    def _get_tools(self):
        return {
            'search': SerperDevTool(),
            'scrape': ScrapeWebsiteTool(),
            'read_resume': FileReadTool(file_path='./resume.md'),
            'semantic_search_resume': MDXSearchTool(mdx='./resume.md')
        }

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[self.tools['scrape'], self.tools['search']],
            verbose=True,
            llm=self.llm
        )

    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config['profiler'],
            tools=[self.tools['scrape'], self.tools['search'],
                   self.tools['read_resume'], self.tools['semantic_search_resume']],
            verbose=True,
            llm=self.llm
        )

    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_strategist'],
            tools=[self.tools['scrape'], self.tools['search'],
                   self.tools['read_resume'], self.tools['semantic_search_resume']],
            verbose=True,
            llm=self.llm
        )

    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_preparer'],
            tools=[self.tools['scrape'], self.tools['search'],
                   self.tools['read_resume'], self.tools['semantic_search_resume']],
            verbose=True,
            llm=self.llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher(),
            async_execution=True
        )

    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config['profile_task'],
            agent=self.profiler(),
            async_execution=True
        )

    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_strategy_task'],
            agent=self.resume_strategist(),
            output_file="output/tailored_resume.md",
            context=[self.research_task(), self.profile_task()]
        )

    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task'],
            agent=self.interview_preparer(),
            output_file="output/interview_materials.md",
            context=[self.research_task(), self.profile_task(), self.resume_strategy_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=1,
            process=Process.sequential
        )
    