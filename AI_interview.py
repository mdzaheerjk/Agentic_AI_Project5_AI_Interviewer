from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination 
from dotenv import load_dotenv
from autogen_agentchat.base import TaskResult
from autogen_agentchat.ui import Console
import os


load_dotenv()

async def team_Config(job_position="Software Engineer"):

    model_client = OpenAIChatCompletionClient(model="gpt-4o",api_key=os.getenv("OPENAI_API_KEY"))

    # Defining our Agent
    # 1. Interviewer Agent
    # 2. Interviewee Agent
    # 3. Career coach Agent
    job_position = "Software Engineer"

    interviewer = AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        description=f"An AI agent that conducts interviews for a {job_position} position.",
        system_message=f'''
        You are a professional interviewer for a {job_position} position.
        Ask one clear question at a time and Wait for user to respond. 
        Your job. is to continue and ask questions, don't pay any attention to career coach response. 
        Make sure to ask question based on Candidate's answer and your expertise in the field.
        Ask 3 questions in total covering technical skills and experience, problem-solving abilities, and cultural fit.
        After asking 3 questions, say 'TERMINATE' at the end of the interview.
        Make question under 50 words.
    '''
    )

    candidate = UserProxyAgent(
        name = "candidate",
        description=f"An agent that simulates a candidate for a {job_position} position.",
        input_func=input
    )


    # 3. Career Coach Agent
    career_coach = AssistantAgent(
        name="Career_Coach",
        model_client=model_client,
        description=f"An AI agent that provides feedback and advice to candidates for a {job_position} position.",
        system_message=f'''
        You are a career coach specializing in preparing candidates for {job_position} interviews.
        Provide constructive feedback on the candidate's responses and suggest improvements.
        After the interview, summarize the candidate's performance and provide actionable advice.
        Make it under 100 words.
    '''
    )

    terminate_condition = TextMentionTermination(text="TERMINATE")

    team = RoundRobinGroupChat(
        participants=[interviewer, candidate, career_coach],
        termination_condition=terminate_condition,
        max_turns=20
    )
    return team


async def interview(team):
# Running the interview
    async for message in team.run_stream(task='Start the interview with the first question ?'):
        if isinstance(message,TaskResult):
            message = f'Interview completed with result: {message.stop_reason}'
            yield message
        else:
            message = f'{message.source}: {message.content}'
            yield message



# async def main():
#     job_position = "Software Engineer"
#     team = await team_Config(job_position)

#     async for message in interview(team):
#         print('-'*70)
#         print((message))

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())