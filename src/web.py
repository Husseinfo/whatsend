from os import environ
from pathlib import Path
from re import sub

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

driver: WebDriver


def init():
    global driver
    environ['PATH'] += f':{Path(__file__).parent.parent}/driver/'

    options = Options()
    options.add_argument(f"--user-data-dir={Path(__file__).parent.parent}/chrome/")
    options.add_argument('--profile-directory=Profile 1')
    driver = webdriver.Chrome(options=options)

    driver.get("https://web.whatsapp.com/")


def click_send(number) -> bool:
    global driver
    button_path = 'footer button:last-child'
    click_script = f"document.querySelectorAll('{button_path}')[1].click()"

    try:
        WebDriverWait(driver, 30).until(lambda _driver: _driver.find_element_by_css_selector(button_path))
        driver.execute_script(click_script)
        return True
    except TimeoutException:
        print(f'Failed to start chat with "{number}" (number not found)')
        return False
    except Exception as e:
        print(f'Error occurred: {e}')
        return False


def send_message(to: str, message: str) -> bool:
    global driver
    to = sub('\\D', '', str(to))
    driver.execute_script(f'window.location="https://web.whatsapp.com/send?phone={to}&text={message}"')
    return click_send(to)
