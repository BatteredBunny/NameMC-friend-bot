from selenium import webdriver
import json
import requests
import time

driver = webdriver.Firefox()

friendsList = requests.get('https://api.namemc.com/profile/b4769eac-1010-405a-b668-04a07b2f20f3/friends')
friendsNames = json.loads(friendsList.text)

driver.get("https://namemc.com/login")
x = input("Press enter after you have logged in. ")
print(" ")

waitTime = 60
x = 0

for i in friendsNames:

	while x <= waitTime:
		time.sleep(1)
		timeRemaining = waitTime - x
		print("Wait: " + str(timeReamining) + " Seconds")
		x += 1
	x = 0

	driver.get("https://namemc.com/profile/" + i["name"])
	try:
		button = driver.find_element_by_id('add-friend-button')
		button.click()
	except:
		print(" ")
		print("I can't find the button, skipping it!")
	print("Username: " + i["name"])
	print(" ")






