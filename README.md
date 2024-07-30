# Automated-Blog-Generation-from-Youtube-Video

## When we query any videos with respect to "AI", there will be a researcher who will go through all the videos in the YouTube channel and validate the content with the help of a domain expert. Then it will pass the content to the blog writer to generate the blog.

## We utilize the CrewAI framework, which consists of three key components:
### a) Tools: Specialized utilities for specific tasks for the agent to perform.
### b) Agents: Autonomous entities designed for particular roles.
### c) Tasks: Defined objectives for the agents to accomplish.
## The CrewAI framework enables effective inter-agent communication, allowing for a seamless and collaborative content creation process.

## As a first step, create a virtual environment using the command "conda create -p venv python==3.10" (using version 3.10, since some modules are compatible with this version) and activate the environment "conda activate '.....\venv'". Then install the necessary modules by "pip install -r requirements.txt".

# agents.py

## 1)  Before using OpenAI models, we must create and download the openai_api_key from "https://platform.openai.com/api-keys". Then store the key as a variable in your system environment variables like "OPENAI_API_KEY": "......".

![OpenAI_SS](https://github.com/user-attachments/assets/5aa1a290-f37d-4191-9793-478f385a4d46)


## Load the environment variable into our environment, and initialize the LLM model

![Load_Env_SS](https://github.com/user-attachments/assets/fe72cb03-e49f-453b-955c-765db7cfaab8)


## 2) Create Agents --> We have to create two agents a) Senior blog content researcher agent, and b) Senior blog content writer agent with YouTube tool. I will transfer whatever work Agent 1 does to Agent 2. In our case, we would transfer the info about the video from the channel to Agent 2 to generate a blog out of it.

  ## a) Senior blog content researcher agent with YouTube tool.

![Agents1_SS](https://github.com/user-attachments/assets/2cc32675-3917-4c33-8509-8b2bc6a25085)
![Agents1_2SS](https://github.com/user-attachments/assets/8b6eebf1-28ab-4fd2-bd07-5a6051168139)

  
  ## b) Senior blog content writer agent with YouTube tool.

![Agents2_SS](https://github.com/user-attachments/assets/7be85ea8-600b-4004-bf7d-7ca3f2b8afa0)


# tools.py

## We have already installed the "crewai_tools" package, so

## 3) Initialize the tool --> "YoutubeChannelSearchTool" with specific YouTube channel content to target out search, which helps the agent to learn about it during the execution.

![Tools_ss](https://github.com/user-attachments/assets/cca3eafa-c030-4cba-b785-3e53d401674b)

  ### After initializing this tool, update the packages in agents.py as "from tools import yt_tool", to use this tool for both the agents (:- in the tool list)


# tasks.py

## 4) We need to create two tasks for two agents created earlier.

  ## a) Research Task for the blog_researcher agent --> This will get a detailed information about the video

![Task1_SS](https://github.com/user-attachments/assets/8d7c0d87-ea95-417e-8c9c-05f5a3014ce8)

  
  ## b) Writing Task for the blog_writer agent --> This will generate the blog and store it in the file "Prajoth-blog-post.md"
  
![Task2_SS](https://github.com/user-attachments/assets/96a204f2-035b-47b6-80a1-13d465a7bee4)


# crew.py

## 5) Finally, to run all these agents we will be using the "Crew" class. I have mentioned the process as sequential because once the "blog_researcher" agent completes its work then the next agent "blog_writer" agent will do its assigned task. (By default the process is sequential).

![Crew_SS](https://github.com/user-attachments/assets/0b24dcf1-79ea-4ffa-98bb-3778e970631a)

  ## Then invoked the agents and tasks with an input.

![kickoff_SS](https://github.com/user-attachments/assets/57cd887e-333f-47cb-96bd-ecfb76f3b62b)


# 6) Observing the Output

  ## a) blog_researcher agent and its task output
  
![Output_1](https://github.com/user-attachments/assets/ca177664-06b6-40c0-9dc5-26e1028d629f)
![Output_2](https://github.com/user-attachments/assets/71591889-4bb5-4d0b-aa05-b77ed68cea4b)
![Output_3](https://github.com/user-attachments/assets/47e6b953-20aa-41df-8b72-0b4a1fd9efd0)

  ## b) blog_writer agent and its task output

![Output_4](https://github.com/user-attachments/assets/6b5cecc7-bcd3-462f-b050-e4e2360bcfe5)
![Output_5](https://github.com/user-attachments/assets/df976bda-d3f1-4870-a614-df8837f2e493)
![Output_6](https://github.com/user-attachments/assets/9850458b-615d-4f3e-9958-1f7c8ca9291f)
![Output_7](https://github.com/user-attachments/assets/f67ba509-3770-4b6c-ace7-185f7a60a03b)


# 7) Prajoth-blog-post.md

![Blog1_SS](https://github.com/user-attachments/assets/d2b5c0d0-946d-4e70-829c-fbd30eb7b8ea)
![Blog2_SS](https://github.com/user-attachments/assets/e4b0671f-f587-4b16-8f7f-89063f8d76a3)


## Finally the Blog is generated from a YouTube video and stored in the output file.














