import json, requests, time, getpass
from selenium import webdriver

waitTime = 60

#gets the username and password so it can login to account
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
print(" ")

#accepts friend lists and gives default value
print("Type nothing for default option.")
apiLink = input("Insert friends list api link: ")
if apiLink == "":
	apiLink = "https://api.namemc.com/profile/b4769eac-1010-405a-b668-04a07b2f20f3/friends"

# loads friend list as python dictionary
friendsList = requests.get(apiLink)
friendsNames = json.loads(friendsList.text)


# Opens browser and login page
driver = webdriver.Firefox()
driver.get("https://namemc.com/login")
time.sleep(1)

try:
	# password, username and submit fields for the bot to use them
	emailField = driver.find_element_by_id("email")
	passwordField = driver.find_element_by_id("password")
	submitButton = driver.find_element_by_xpath("//button[@class='btn btn-primary']")

	#send the inputs and clicks button
	passwordField.send_keys(password)
	emailField.send_keys(username)
	submitButton.click()
except:
	print(" ")
	t = input("Please complete the captcha then press enter.")

	# password, username and submit fields for the bot to use them
	emailField = driver.find_element_by_id("email")
	passwordField = driver.find_element_by_id("password")
	submitButton = driver.find_element_by_xpath("//button[@class='btn btn-primary']")

	#send the inputs and clicks button
	passwordField.send_keys(password)
	emailField.send_keys(username)
	submitButton.click()

for i in friendsNames:

	driver.get("https://namemc.com/profile/" + i["name"])

	print(" ")
	print("Username: " + i["name"] + " UUID: " + i["uuid"])

	try:

		button = driver.find_element_by_id('add-friend-button')
		button.click()

	except:
		print("I already sent friend request to them. (Or im not logged in)")
		print("Waiting " + str(waitTime) + " Seconds")

	else:
		print("Request sent, waiting " + str(waitTime) + " Seconds")

	time.sleep(waitTime)
