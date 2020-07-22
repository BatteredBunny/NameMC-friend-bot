from selenium import webdriver
import json, requests, time

# Browser used by the bot
driver = webdriver.Firefox()

# Replace this with some other friends list if you want!
apiLink = "https://api.namemc.com/profile/b4769eac-1010-405a-b668-04a07b2f20f3/friends"
waitTime = 60
x = 0

friendsList = requests.get(apiLink)
friendsNames = json.loads(friendsList.text)

# You have to login or else it doesn't work
driver.get("https://namemc.com/login")
t = input("Press enter after you have logged in. ")
print(" ")

for i in friendsNames:
	while x <= waitTime:
		time.sleep(1)
		timeRemaining = waitTime - x
		print("Wait: " + str(timeRemaining) + " Seconds")
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
