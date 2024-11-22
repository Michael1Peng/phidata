import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat

task = "Write a short story about life in 500000 years"

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-11-20", base_url=os.getenv("OPENAI_API_BASE")),
    reasoning_model=OpenAIChat(id="gpt-4o-2024-11-20", base_url=os.getenv("OPENAI_API_BASE")),
    reasoning=True,
    markdown=True,
    structured_outputs=True,
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
