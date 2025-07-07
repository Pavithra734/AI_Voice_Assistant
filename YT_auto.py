from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class MusicPlayer:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def play(self, query):
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        self.driver.implicitly_wait(5)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
