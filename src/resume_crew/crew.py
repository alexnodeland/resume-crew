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
            return ChatOpenAI(model="gpt-3.5-turbo")

    def _get_tools(self):
        return {
            'search': SerperDevTool(),
            'scrape': ScrapeWebsiteTool(),
            'read_resume': FileReadTool(file_path='./fake_resume.md'),
            'semantic_search_resume': MDXSearchTool(mdx='./fake_resume.md')
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
            output_file="tailored_resume.md",
            context=[self.research_task(), self.profile_task()]
        )

    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_preparation_task'],
            agent=self.interview_preparer(),
            output_file="interview_materials.md",
            context=[self.research_task(), self.profile_task(), self.resume_strategy_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )

if __name__ == "__main__":
    resume_crew = ResumeCrewCrew()
    job_application_inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }
    result = resume_crew.crew().kickoff(inputs=job_application_inputs)