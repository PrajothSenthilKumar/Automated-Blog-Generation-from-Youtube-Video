from crewai import Crew, Process                    # Since we are going to execute tasks sequential flow
from agents import blog_researcher, blog_writer
from tasks import research_task, writer_task

# Now in order to call this in a sequential manner we will be using the crew class

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writer_task],
    process = Process.sequential,    # By default it is sequential
    memory = True,
    verbose = True,
    max_rpm = 100,
    share_crew = True
)

# Start the task execution with enhanced feedback
result = crew.kickoff(
    inputs = {'topic': "CNNs, RNNs, LSTMs, and Transformers"}
)

print(result)