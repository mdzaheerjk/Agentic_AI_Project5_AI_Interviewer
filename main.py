from AI_interview import team_Config, interview
import asyncio


async def main():
    job_position = "Software Engineer"
    team = await team_Config(job_position)

    async for message in interview(team):
        print('-' * 70)
        print(message)


if __name__ == "__main__":
    asyncio.run(main())