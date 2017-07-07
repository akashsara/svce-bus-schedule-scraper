#!python3
#Script to scrape the SVCE college website and obtain the bus schedule for the current week
import requests, bs4, re, smtplib, os, datetime, config

#Bus schedule URL
url = r'https://svce.ac.in/departments/transport/schedule.php'

#Dates are in the format of DateDay. So regex to separate Date and Day with a space
dateFormat = re.compile(r'([0-9]{2}/[0-9]{2}/[0-9]{2})([a-zA-Z]+)')

#Download the page and check for errors
page = requests.get(url)
page.raise_for_status()

#Parse the page and get table values
html = bs4.BeautifulSoup(page.text, "html.parser")
busTable = html.select('.CSSTableGenerator td')

#5 headings on the table
headings = ['Date', 'Morning', 'Special(1:30)', 'Evening(3:30)', 'Late(4:30)']

#Counter initialization
loopCounter = 5
headingCounter = 0

#Create a schedule list to hold the schedule
schedule = []
while loopCounter < len(busTable):
	#If the value we check is a date, we format the date and add it to the list along with its heading
	if dateFormat.search(busTable[loopCounter].getText()):
		date = dateFormat.search(busTable[loopCounter].getText())
		formattedDate = date[1] + ' ' + date[2]
		headingCounter = 0
		schedule.append('\n' + headings[headingCounter] + ':' + formattedDate)
	#If it says unavailable, check how many of the columns say so and for each column print unavailable
	elif busTable[loopCounter].has_attr('colspan'):
		limit = loopCounter + int(busTable[loopCounter]['colspan'])
		for j in range(loopCounter, limit):
			schedule.append(headings[headingCounter] + ':' + busTable[loopCounter].getText())
			headingCounter += 1
	#In any other case add the value to the heading
	else:
		schedule.append(headings[headingCounter] + ': ' + busTable[loopCounter].getText().replace(' ', '').replace('\r\n', ','))
	loopCounter += 1
	headingCounter += 1

#Login to gmail
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(smtpObj.ehlo())
smtpObj.login(config.emailID, config.password)

#Try to send the mail else log the error to a file
if(smtpObj.sendmail(config.emailID, config.emailList, config.emailMessage + '\n'.join(schedule))):
	now = datetime.datetime.now()
	date = now.strftime('\n%d-%m-%Y %H:%M:%S')
	errorLog = open(r'.\errorlog.txt', 'a', encoding='utf-8')
	errorLog.write(date)
	errorLog.write('\nCould not send mail to one or more recepients!')
	errorLog.close()

#Logout
smtpObj.quit()
