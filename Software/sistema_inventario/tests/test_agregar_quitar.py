import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestAgregarQuitar:
    def setup_method(self, method):
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.set_window_size(1094, 1392)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_agregar_quitar(self):
        self.driver.get("http://localhost:8000/inventario.html")

        def double_click(selector):
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            ActionChains(self.driver).double_click(element).perform()

        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        double_click("button:nth-child(3)")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        double_click("button:nth-child(4)")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        double_click("button:nth-child(4)")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
  
