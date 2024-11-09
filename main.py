from crewai import Agent, Task, Crew,LLM
from crewai_tools import FileReadTool


# Initialize the tool with a specific file path, so the agent can only read the content of the specified file
file_read_tools = FileReadTool(file_path='ai.txt' )



# Set up the LLM
llm = LLM(
    model="ollama/qwen2.5",
    base_url="http://localhost:11434",
)

agent1 = Agent(
    role="what is this file about ?",
    goal="just give me a what is this file about?",
    backstory="agent backstory",
    verbose=True,
    llm=llm,
    max_retry_limit=3,
    tools=[file_read_tools],
)

task1 = Task(
    expected_output="a summrize of this data",
    description="a summrize of this data",
    agent=agent1,
    max_retry_limit=3,
)

# agent2 = Agent(
#     role="Senior Translator",
#     goal="Translate to the persian",
#     backstory="You are a senior persian translator at the wsj",
#     verbose=True,
#     llm=llm,
#     max_retry_limit=3,
# )
#
# task2 = Task(
#     description="Translate to the perisan",
#     expected_output="Translate into a fluent persian",
#     agent=agent1,
#     context=[task1],
#     max_retry_limit=3,
#
# )

my_crew = Crew(agents=[agent1], tasks=[task1] )
crew = my_crew.kickoff()


