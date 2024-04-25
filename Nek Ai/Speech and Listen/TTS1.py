# https://readloud.net/english/british/1-male-voice-brian.html
# pip install selenium chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from chromedriver_autoinstaller import install

# Install ChromeDriver
chrome_path = install()

# Set up Chrome options
chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
chrome_options.add_argument("--headless=new")

# Start the Service
service = Service(executable_path=chrome_path)

# Start the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://readloud.net/english/british/1-male-voice-brian.html")

script = """function mediaElementIsPlaying(el) {
  return el && el.currentTime > 0 && !el.paused && !el.ended && el.readyState > 2;
}
// Check if any audio element is playing
const audioIsPlaying = !![...document.getElementsByTagName('audio')].find((el) => mediaElementIsPlaying(el));
// If either audio or video is playing, return true
return audioIsPlaying;"""

def TextToSpeech(text):
    try:
        textarea = driver.find_element(By.NAME, "but1")
        textarea.clear()
        textarea.send_keys(text)

        submit = driver.find_element(By.NAME, "butt0")
        submit.click()

        while 1:
            playing = driver.execute_script(script)
            if not playing:
                break
            sleep(0.1)

    except Exception as e:
        print(e)
        print("Restarting website")
        driver.get("https://readloud.net/english/british/1-male-voice-brian.html")
        TextToSpeech(text)

if __name__ == "__main__":
    while 1:
        text = input(">>>  ")
        TextToSpeech(text)
        