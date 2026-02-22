from langchain_core.messages import HumanMessage, AIMessage

from src.chains.iternary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exceptions import CustomException
from src.config.config import config

logger = get_logger(__name__)

class TravelPlanner:

    def __init__(self):
        self.messages = []
        self.city = str()
        self.interests = []
        self.itinerary = str()

        logger.info("Initialized TravelPlanner")
    
    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=f"City: {city}"))
            logger.info(f"Set city to: {city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException(f"Failed to set city", e)
        
    def set_interests(self, interests: str):
        try:
            self.interests = [interest.strip() for interest in interests.split(",")]
            self.messages.append(HumanMessage(content=f"Interests: {interests}"))
            logger.info(f"Set interests to: {self.interests}")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException(f"Failed to set interests", e)
    
    def create_itinerary(self):
        try:
            if not self.city or not self.interests:
                raise CustomException("City and interests must be set before creating itinerary")
            
            logger.info(f"Creating itinerary for city: {self.city} with interests: {self.interests}")
            self.itinerary = generate_itinerary(self.city, self.interests)
            self.messages.append(AIMessage(content=self.itinerary))
            logger.info("Generated itinerary successfully")
        except Exception as e:
            logger.error(f"Error creating itinerary: {e}")
            raise CustomException(f"Failed to create itinerary", e)

