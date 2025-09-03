import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get("http://127.0.0.1:5000/")
    assert "Hello, Selenium!" in browser.page_source
