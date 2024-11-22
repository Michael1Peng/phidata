import os

from phi.agent import Agent
from phi.model.openai import OpenAIChat

task = "帮我发现香港储蓄型保险可能存在的问题"

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    reasoning_model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    reasoning=True,
    markdown=True,
    structured_outputs=True,
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
