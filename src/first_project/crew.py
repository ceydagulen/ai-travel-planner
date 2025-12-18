from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class FirstProject():
    """FirstProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def city_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['city_scout'],
            verbose=True
        )

    @agent
    def travel_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_planner'],
            verbose=True
        )

    @agent
    def budget_estimator(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_estimator'],
            verbose=True
        )

    @task
    def location_scouting_task(self) -> Task:
        return Task(
            config=self.tasks_config['location_scouting_task'],
        )

    @task
    def itinerary_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_planning_task'],
        )

    @task
    def budget_calculation_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_calculation_task'],
            output_file='tatil_plani.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )