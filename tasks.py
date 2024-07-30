from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# The first task --> Research Task for blog_researcher agent
research_task = Task(
    description = (
        "Identify the video {topic}."
        "Get detailed information about the video from the channel"
    ),
    expected_output = "A comprehensive 3 paragrpahs long report based on the {topic} of video content.",
    tools = [yt_tool],
    agent = blog_researcher
)

# The second task --> Writing task for the blog_writer agent
writer_task = Task(
    description = (
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output = "Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog.",
    tool = yt_tool,
    agent = blog_writer,
    async_execution = False,    # If it is set to true then both the agents will be parallely working
    output_file = 'Prajoth-blog-post.md'
    )