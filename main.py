# This is a recode of the selenium script I built with my current knowledge.
import asyncio
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        
        text_box: WebElement = self.driver_wait.until(
                method=expected_conditions.element_to_be_clickable(
                    (By.CLASS_NAME, "styled.nickname")
                    )
                )
        
        # Write User info
        text_box.clear()
        text_box.send_keys("Ortin")
        text_box.send_keys(Keys.ENTER)


        
    async def answer_question(self) -> None:
        pass
    

def main() -> None:
    BotController(room_code="TFQT")



if __name__ == "__main__":
    main()
