
# coding: utf-8

class pre():
	def log_file_preprocessing(log_file):
		import pandas as pd
		logs=pd.read_csv(log_file,sep='- -',header =None,names=['IP','Values'])
		text=logs.values
		sd=[]
		for text in text:
			conv=str(text)
			sd.append(conv.split())
		date=[]
		http=[]
		reciver=[]
		server_status=[]
		for i in range(len(sd)):
			date.append(sd[i][3:4])
			http.append(sd[i][6:8])
			reciver.append(sd[i][11:])
			server_status.append(sd[i][8])
		logs.drop('Values',axis=1,inplace=True)
		logs['Date']=date
		logs['http']=http
		logs['reciver']=reciver
		logs['server_status']=server_status
		return logs


