from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)


driver.get("https://youtube.com")
time.sleep(2)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)


driver.get("https://google.com")
time.sleep(4)

print("Checking...")




print("Done :)")
driver.quit()
