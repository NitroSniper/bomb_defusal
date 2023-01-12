# This is a recode of the selenium script I built with my current knowledge.
import asyncio
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BotController():
    def __init__(self, room_code: str) -> None:
        self.driver = webdriver.Firefox()
        self.driver_wait = WebDriverWait(
                driver=self.driver, 
                timeout=10, 
                poll_frequency=1
                )


        # Try to join the room. 
        self.driver.get(f"https://jklm.fun/{room_code}")
        self.driver_wait.until(
                method=expected_conditions.element_to_be_clickable()
                )
        


        
    async def answer_question(self) -> None:
        
    

def main() -> None:
    pass



if __name__ == "__main__":
    main()
