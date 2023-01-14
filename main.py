# This is a recode of the selenium script I built with my current knowledge.
import asyncio
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BotController():
    def __init__(self, room_code: str, verbose: bool = False) -> None:
        self.verbose = verbose
        self.driver = webdriver.Firefox()
        
        # Try to join the room. 
        self.driver.get(f"https://jklm.fun/{room_code}")
        
        text_box: WebElement = WebDriverWait(
                driver=self.driver,
                timeout=10,
                poll_frequency=1
                ).until(
                method=expected_conditions.element_to_be_clickable(
                    (By.CLASS_NAME, "styled.nickname")
                    )
                )
        
        # Write User info
        text_box.clear()
        text_box.send_keys("Ortin")
        text_box.send_keys(Keys.ENTER)
        
        self.driver_wait = WebDriverWait(
                driver=self.driver, 
                timeout=1_000_000, # infinite amount 
                poll_frequency=1 # can be an argument to the class
                )
        
        game_frame: WebElement = self.driver_wait.until(
                method=expected_conditions.presence_of_element_located(
                    (By.TAG_NAME, "iframe")
                    )
                )
        self.driver.switch_to.frame(frame_reference=game_frame)
        
        join_button: WebElement = self.driver_wait.until(
                method=expected_conditions.element_to_be_clickable(
                    (By.CLASS_NAME, "joinRound")
                    )
                )
        join_button.click()
        
        self.self_turn: WebElement = self.driver.find_element(By.CLASS_NAME, "selfTurn") # used to check if it is our turn.
        self.game_state: WebElement = self.driver.find_element(By.CLASS_NAME, "round") # Checks if bot is in game

        self.start()
        
    def start(self) -> None:
        self.driver_wait.until(
                method=lambda driver: self.game_state.is_displayed()
                )
        if self.verbose:
            print ("Game has started")
        #get player id from the javascript
        self.player_id: int = self.driver.execute_script("return milestone.currentPlayerId")
        self.game_loop()

        
    def game_loop(self) -> None:
        # run if it's our turn
        self.driver_wait.until(
                method=lambda driver: self.self_turn.is_displayed()
                )
        if self.verbose:
            print ("Our turn")



    async def answer_question(self) -> None:

        pass
    

def main() -> None:
    BotController(room_code="YHBP", verbose=True)



if __name__ == "__main__":
    main()
