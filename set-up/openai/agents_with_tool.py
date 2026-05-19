import asyncio

from agents import Agent, Runner, function_tool


@function_tool
def history_fun_fact() -> str:
    """REturn a short history fact."""
    return "Sharks are older than trees."

agent = Agent(
    name="History Tutor",
    instructions="Answer history question cleary. Use history_fun_fact when it helps.",
    tools=[history_fun_fact],
)

async def main() -> None:
    result = await Runner.run(agent, "Tell me a fun fact about history.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
