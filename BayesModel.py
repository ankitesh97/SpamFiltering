
import pandas as pd
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

def create_frequency_table(texts, labels=None, parse=False):

	frequency_table = pd.DataFrame([])
	for idx, t in enumerate(texts):
		vocab = set(t)
		d = pd.Series({v:t.count(v) for v in vocab})  #each email represents a column in the final dataframe
#series vs dataframes is like array vs multi dimensional array
		if labels != None:
			d['*class*'] = labels[idx]
		frequency_table = frequency_table.append(d,ignore_index=True)
	return frequency_table



emails,labels = parse_files(email_files,email_path)
create_frequency_table(emails,labels).to_csv('a.csv')