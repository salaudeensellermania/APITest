#Coded By: Salaudeen
#Version: 1.0
#Submission Date: 07/jan/2020
#Purpose: To geenrate the Order Request file
#Revised Date: Dec 2020
#Revised Reason: Code Revised to be compatible with python latest version 3.8.5

import sys
import os
import csv
import subprocess
import requests
import datetime



with open('orderaz.csv') as csvDataFile:
	csvReader = csv.DictReader(csvDataFile)
	for row in csvReader:
		break

#class
class requestgetorderbyid:
	#def __init__(self,x):
	#	self.x=x

#default method1 for request response	
	def __init__(self):

		user=row['input_user']
		password=row['input_password']
		url=row['input_endpoint']
		orderid=row['input_order_id']				

#generate security header
		output = subprocess.Popen("php ./securityheader.php "+user+" "+password, shell=True, stdout=subprocess.PIPE)
		script_response = output.stdout.read()

		data1= '''
		<soapenv:Envelope xmlns:ord="http://order.apis.sellermania.com/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

		<soapenv:Header>
		'''

		data2= script_response

		data3= '''
		</soapenv:Header>

		   <soapenv:Body>

      			<ord:GetOrderById>
			 <orderId>
			'''
		data4=orderid
		data5= ''' </orderId>
      			</ord:GetOrderById>
		     
		   </soapenv:Body>

		</soapenv:Envelope>
		'''
#pack request
		data = data1 + str(data2) + data3 + data4 + data5


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data1,auth=HTTPDigestAuth('picoSC@yopmail.com', '64ddfe0fd8df3cf6311e4056dd74c767f3b4a48d6c30c7685d0f80bcec9f47ee'))


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data4)
#Post request
		self.r = requests.post(url,data)
		self.xml=self.r.content


######################################GetOrderByDateCall###################################


#class
class requestgetorderbydate:
	#def __init__(self,x):
	#	self.x=x

#default method1 for request response	
	def __init__(self):

		user=row['input_user']
		password=row['input_password']
		url=row['input_endpoint']
		startdate=row['input_startdate']	
		enddate=row['input_enddate']			

#generate security header
		output = subprocess.Popen("php ./securityheader.php "+user+" "+password, shell=True, stdout=subprocess.PIPE)
		script_response = output.stdout.read()

		data1= '''
		<soapenv:Envelope xmlns:ord="http://order.apis.sellermania.com/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

		<soapenv:Header>
		'''

		data2= script_response

		data3= '''
		</soapenv:Header>

		   <soapenv:Body>

      			<ord:GetOrderByDate>
			 <date>
			'''
		data4=startdate
		data5= ''' </date>
			<enddate>
			'''
		data6=enddate
		data7='''
			</enddate>
      			</ord:GetOrderByDate>
		     
		   </soapenv:Body>

		</soapenv:Envelope>
		'''
#pack request
		data = data1 + str(data2) + data3 + data4 + data5 + data6 + data7


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data1,auth=HTTPDigestAuth('picoSC@yopmail.com', '64ddfe0fd8df3cf6311e4056dd74c767f3b4a48d6c30c7685d0f80bcec9f47ee'))


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data4)
#Post request
		self.r = requests.post(url,data)
		self.xml=self.r.content



######################################GetOrderByStatus Call###################################


#class
class requestgetorderbystatus:
	#def __init__(self,x):
	#	self.x=x

#default method1 for request response	
	def __init__(self):

		user=row['input_user']
		password=row['input_password']
		url=row['input_endpoint']
		startdate=row['input_startdate']	
		enddate=row['input_enddate']			
		status=row['input_status']	
		marketplace=row['input_mkpname']

#generate security header
		output = subprocess.Popen("php ./securityheader.php "+user+" "+password, shell=True, stdout=subprocess.PIPE)
		script_response = output.stdout.read()

		data1= '''
		<soapenv:Envelope xmlns:ord="http://order.apis.sellermania.com/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

		<soapenv:Header>
		'''

		data2= script_response

		data3= '''
		</soapenv:Header>

		   <soapenv:Body>

      			<ord:GetOrderByStatus>
			 <date>
			'''
		data4=startdate
		data5= ''' </date>
			<enddate>
			'''
		data6=enddate
		data7='''
			</enddate>
			<status>
			'''
		data8=status
		data9='''
			</status>
			<marketplace>
			'''
		data10=marketplace
		data11='''
			</marketplace>
      			</ord:GetOrderByStatus>
		     
		   </soapenv:Body>

		</soapenv:Envelope>
		'''
#pack request
		data = data1 + str(data2) + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data1,auth=HTTPDigestAuth('picoSC@yopmail.com', '64ddfe0fd8df3cf6311e4056dd74c767f3b4a48d6c30c7685d0f80bcec9f47ee'))


		#r = requests.post(url='http://preprod.api.sellermania.com/InventoryAPISFR_11_12_2017/InventoryAPIS?wsdl',data=data4)
#Post request
		self.r = requests.post(url,data)
		self.xml=self.r.content

