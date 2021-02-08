#Coded By: Salaudeen
#Version: 1.0
#Submission Date: 07/jan/2020
#Purpose: To generate the Inventory request file
#Revised Date: Dec 2020
#Revised Reason: Code Revised to be compatible with python latest version 3.8.5

import sys
import os
import csv
import subprocess
import requests
import datetime



with open('inv.csv') as csvDataFile:
	csvReader = csv.DictReader(csvDataFile)
	for row in csvReader:
		break

#class

######################################REQUEST CALL FOR GetInventory Call###################################

class requestgetinventory:
	#def __init__(self,x):
	#	self.x=x

#default method1 for request response	
	def __init__(self):

		user=row['input_user']
		password=row['input_password']
		url=row['input_endpoint']
		sku1=row['input_sku']				

		try:
	#generate security header
			output = subprocess.Popen("php ./securityheader.php "+user+" "+password, shell=True, stdout=subprocess.PIPE)
			script_response = output.stdout.read()

			data1= '''
			<soapenv:Envelope xmlns:inv="http://inventory.apis.sellermania.com/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

			<soapenv:Header>
			'''

			data2= script_response

			data3= '''
			</soapenv:Header>

			   <soapenv:Body>

			      <inv:GetInventory>
				 <Sku>
				'''
			data4=sku1
			data5= ''' </Sku>
			      </inv:GetInventory>

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

		except Exception as ex:
			print ("FAILED -> PROBLEM  WITH THE INPUT PARAMETERS FOR API REQUEST. PLEASE CHECK YOUR USER/PASSWORD/ENDPOINT/SKU "+ str(ex))



######################################REQUEST CALL FOR GetSkuQuantity Call###################################

class requestskuquantity:
	#def __init__(self,x):
	#	self.x=x

#default method1 for request response	
	def __init__(self):

		user=row['input_user']
		password=row['input_password']
		url=row['input_endpoint']
		sku1=row['input_sku']				

		try:
	#generate security header
			output = subprocess.Popen("php ./securityheader.php "+user+" "+password, shell=True, stdout=subprocess.PIPE)
			script_response = output.stdout.read()

			data1= '''
			<soapenv:Envelope xmlns:inv="http://inventory.apis.sellermania.com/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">

			<soapenv:Header>
			'''

			data2= script_response

			data3= '''
			</soapenv:Header>

			   <soapenv:Body>

			      <inv:GetSkuQuantity>
				 <Sku>
				'''
			data4=sku1
			data5= ''' </Sku>
			      </inv:GetSkuQuantity>

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
			

		except Exception as ex:
			print ("FAILED -> PROBLEM  WITH THE INPUT PARAMETERS FOR API REQUEST. PLEASE CHECK YOUR USER/PASSWORD/ENDPOINT/SKU "+ str(ex))
