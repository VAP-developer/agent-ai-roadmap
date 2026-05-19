import asyncio

from agents import Agent, Runner

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)

async def main() -> None:
    result = await Runner.run(agent, "When did the Spanish Empire fall?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
