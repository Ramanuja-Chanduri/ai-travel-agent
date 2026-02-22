from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from typing import List

from src.config.config import config

llm = ChatGroq(api_key=config.GROQ_API_KEY, name="openai/gpt-oss-20b", temperature=0.3)

iternerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. \n\n Provide a brief, bulleted itinerary.")
    ("human", "Create an itinerary for a day trip.")
])

def generate_itinerary(city: str, interests: List[str]) -> str:
    """
    Generate a day trip itinerary for a given city and user interests.

    Args:
        city (str): The city for which to create the itinerary.
        interests (List[str]): A list of user interests to tailor the itinerary.

    Returns:
        str: A brief, bulleted itinerary for the day trip.
    """
    prompt = iternerary_prompt.format_messages(city=city, interests=", ".join(interests))
    response = llm.invoke(prompt)
    return response.content