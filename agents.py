from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = "gpt-4-0125-preview"


# Initializing the LLM
llm = ChatOpenAI(
        model="gpt-4-0125-preview",
        temperature=0
    )

# I will create 2 agents

# 1. Senior Blog content researcher agent --> Responsible for researching and summarizing blog content

blog_researcher = Agent(
    role='Blog Researcher from Youtube videos',
    goal = 'Get the relevant video content for the topic {topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI, Data Science, Machine Learning, Gen AI and provide suggestions"
    ),
    tool = [yt_tool],
    llm = llm,
    allow_delegation = True   # Means I will transfering the work that this agent does to someone else
)


# 2. Senior Blog writer agent --> Responsible for writing blog content based on the research done by the researcher agent

blog_writer = Agent(
    role="Blog Writer",
    goal = "Narrate compelling tech stories abput the video {topic} from Youtube channel",
    verbose = True,
    memory = True,
    backstory = (
        "with a flais for simplifying complex topics, you craft"
        "engaing narrative that captivates and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tool = [yt_tool],
    llm = llm,
    allow_delegation = False
)
