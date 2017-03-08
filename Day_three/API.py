""" Using status codes to gauge the servers response to you"""

import requests
website = raw_input("What website would you like to check? Hint: Answer format http://domainname.com ")

response = requests.get(website)
website_status = response.status_code

status_checker = str(website_status)

#refering to code academy <https://www.codecademy.com/en/courses/python-intermediate-en-6zbLp/2/1?curriculum_id=5122e7dcb514665974000a9d> to find out what the code means

if status_checker[0] == '1':
 	print "Got it! I'm working on your request."

if status_checker[0] == '2':
	print "okay! I will successfully respond to your request"

elif status_checker[0] == '3':
	print "I can do what you want, but I have to do something else first." 

elif status_checker[0] == '4':
	print "Oops, you must have made a mistake"
else:
	print "Sorry can't successfully respond to your request."



