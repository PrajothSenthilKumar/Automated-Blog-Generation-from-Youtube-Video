from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific Youtube Channel content to target your search, 
# so that the agent learns about it during it's execution

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle = '@Roboflow'
)