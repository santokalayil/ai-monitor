from typing import NoReturn
from ai.core import monitor_status, get_version
from pydantic import BaseModel, Field
from pydantic_ai import Agent
import asyncio
import nest_asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Apply nest_asyncio to allow async code to run in Jupyter notebooks
nest_asyncio.apply()

class WeatherResponse(BaseModel):
    """Structured response for weather queries"""
    temperature: float = Field(description="Temperature in Celsius")
    condition: str = Field(description="Weather condition")
    recommendation: str = Field(description="What to wear based on the weather")

async def weather_example() -> None:
    """Example of using PydanticAI with structured responses"""
    # Create an agent with a specific model
    agent = Agent(
        'google-gla:gemini-2.0-flash',
        result_type=WeatherResponse,
        system_prompt="You are a weather assistant. Provide weather information and clothing recommendations."
    )
    
    try:
        # Run the agent asynchronously
        result = await agent.run("What's the weather like in Paris today?")
        print("\nWeather Example Response:")
        print(f"Temperature: {result.data.temperature}°C")
        print(f"Condition: {result.data.condition}")
        print(f"Recommendation: {result.data.recommendation}")
    except Exception as e:
        print(f"Error in weather example: {e}")

def basic_example() -> None:
    """Basic example of using PydanticAI"""
    # Create a simple agent
    agent = Agent(
        'google-gla:gemini-2.0-flash',
        system_prompt="Be concise, reply with one sentence."
    )
    
    try:
        # Run the agent synchronously
        result = agent.run_sync("What is the capital of France?")
        print("\nBasic Example Response:")
        print(result.data)
    except Exception as e:
        print(f"Error in basic example: {e}")

async def main() -> NoReturn:
    """
    Main entry point for the application.
    
    Returns:
        NoReturn: This function doesn't return anything
    """
    print("Hello, World!")
    print(f"AI Monitor Version: {get_version()}")
    print(f"Status: {monitor_status()}")
    
    # Run examples
    print("\nRunning PydanticAI Examples:")
    basic_example()
    await weather_example()

if __name__ == "__main__":
    asyncio.run(main()) 