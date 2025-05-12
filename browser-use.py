from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv  
load_dotenv()
# Load environment variables from .env file




async def main():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )
    
    agent = Agent(
        task = "Search on youtube  for videos about the Agent-Native Cloud Development playlists of panaversity urdu channel.",
        llm=llm,
    )
    
    await agent.run()
    
asyncio.run(main())    