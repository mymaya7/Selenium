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

# Finding the element of the textbox bu ID.
search = driver.find_element(By.ID,"inputfield")
startTime = time.time()

# Index of the current word in the sentence.
wordNum=1

# Loop until the sentence is over.
while True:

	# Find the current word element.
	text="//*[@id='row1']/span[{}]".format(wordNum)
	try:
		#Get the word element by ID.
	    words = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, text))
	    )

	    # The sentence ended.
	    if words.text== '':
	    	endTime = time.time()
	    	print("DONE - number of words {} , in : {} seconds".format(wordNum-1,endTime - startTime))
	    	break
	  
	    search.send_keys(words.text)
	    search.send_keys(Keys.SPACE)
	    wordNum=wordNum+1
	except:
	    driver.quit()
time.sleep(20)	
driver.quit()