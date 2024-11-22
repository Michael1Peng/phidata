from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    monitoring=True,
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    monitoring=True,
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=OpenAIChat(id="gpt-4o", base_url=os.getenv("OPENAI_API_BASE")),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    monitoring=True,
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("分析中国保险法和香港保险法，在针对储蓄型保险的差异", stream=True)
