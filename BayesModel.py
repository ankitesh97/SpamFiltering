
import pandas
import numpy
import os

email_path = '/home/ankitesh/projects/SpamFiltering/Emails/'
email_files = [x for x in os.listdir(email_path)]

to_filter = [',', '?', '!', ' ', ' ', ' '] #list of strings that will be filtered from the mails

#method to parse email files
def parse_files(email_files, email_path):
	emails = [] #will contain parsed email
	labels = []  #ham 0 - spam 1
	for e in email_files:
		email = open(email_path+e,'r')
		text = [x for x in email.read().lower().replace('\n',' ')]
		for ch in to_filter:
			text = [x.replace(ch,' ') for x in text]
		text = ''.join(text).split()
		lbl = text[-1]
		labels.append(lbl)
		del text[-1]
		emails.append(text)

	return emails,labels


print parse_files(email_files,email_path)