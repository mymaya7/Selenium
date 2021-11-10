import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://10fastfingers.com/typing-test/english")
search = driver.find_element(By.ID,"inputfield")
startTime = time.time()

i=1
while i>0:
	text="//*[@id='row1']/span[{}]".format(i)
	try:
	    words = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, text))
	    )

	    if words.text== '':
	    	endTime = time.time()
	    	print("done number of words {} , in : {} seconds".format(i-1,endTime - startTime))
	    	break
	  
	    search.send_keys(words.text)
	    search.send_keys(Keys.SPACE)
	    i=i+1
	except:
	    driver.quit()
time.sleep(20)	
driver.quit()