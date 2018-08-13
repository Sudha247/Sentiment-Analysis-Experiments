from selenium import webdriver    #open webdriver for specific browser
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import time  
path = '/home/sudha/Documents/chromedriver'
handles = ['Incredibles 2']

for handle in handles:
	driver = webdriver.Chrome(path)
	driver.get("https://www.twitter.com/search?q=" + handle)
	for i in range(25):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3)
	#html_source = driver.page_source
	#file.write(html_source)
	#print(data)
	file = open(handle+".txt", "w")
	tweets = driver.find_elements_by_class_name('tweet-text')
	for tweet in tweets:
		file.write(tweet.text)
		file.write('$\n') 
	driver.close()