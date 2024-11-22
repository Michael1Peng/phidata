"""Run `pip install openai duckduckgo-search phidata` to install dependencies."""

import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("how to copy all opened files in vscode?", stream=True)
