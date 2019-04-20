import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

found = 0

frd = ""

while(found!=1):
	
	driver = webdriver.Chrome("/usr/bin/chromedriver")
	driver.get("https://in.bookmyshow.com/mumbai/movies/avengers-endgame/ET00090482")
	

	try:
	    myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'wzrk-cancel')))
	    print "Page is ready!"
	except TimeoutException:
	    print "Loading took too much time!"

	driver.refresh()

	bkbtn = driver.find_elements_by_xpath("//a[contains(text(), 'Book Tickets')]")

	if(bkbtn[0]):
		bkbtn[0].click()

	# fdbtn = driver.find_elements_by_xpath("//a[contains(text(), '3D 4DX')]")
	# fdbtn = driver.find_elements_by_xpath("//a[contains(text(), '3D')]")

	fdbtn = driver.find_elements_by_class_name("dimension-pill")
	print(len(fdbtn))
	for e in fdbtn:
		print(e.get_attribute('innerHTML'))
		if(e.get_attribute('innerHTML')=="3D 4DX"): #IMAX 3D or 3D 4DX
			found = 1
			frd = e

	if(found != 1):
		print("not availble now!")
		driver.quit()
		

duration = 2  # seconds
freq = 440  # Hz


if(found == 1):
	frd.click()
	print("availbale now just book")
	while True:
		os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
		time.sleep(2)
	print "\a"