#Coded By: Salaudeen
#Version: 1.0
#Submission Date: 07/jan/2020
#Revised Date: Dec 2020
#Revised Reason: Code Revised to be compatible with python latest version 3.8.5
#Purpose: To validate the Inventory tags and data



import sys
import os
import csv
import subprocess
import requests
import datetime
from apipackages import inventory_request_response


with open('inv.csv') as csvDataFile:
	csvReader = csv.DictReader(csvDataFile)
	for row in csvReader:
		break

#class
class getinventory:
	#def __init__(self,x):
	#	self.x=x

#default method1 calling request response program	
	def __init__(self):

		obj1=inventory_request_response.requestgetinventory()	
		self.r=obj1.r
		self.xml=obj1.xml
#method2	
	def getinventorystatuscode(self):
		r=self.r
		return r

#method3
	def getinventorystatus(self):
	#code for parsing XML & return passed or failed (if i=0, then all passed, if i>0, some has bene failed)
	#CHECK FOR SKU
		try:
		
			i=0
			start=str(row['tag_sku_start'])
			end=str(row['tag_sku_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_sku']:
				pass
			else:
				i=i+1


		#CHECK FOR Quantity
			start=str(row['tag_quantity_start'])
			end=str(row['tag_quantity_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_quantity']:
				pass
			else:
				i=i+1

		#CHECK FOR TITLE
			start=str(row['tag_title_start'])
			end=str(row['tag_title_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_title']:
				pass
			else:
				i=i+1

		#CHECK FOR VERSION
			start=str(row['tag_version_start'])
			end=str(row['tag_version_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_version']:
				pass
			else:
				i=i+1

		#CHECK FOR EMAIL
			start=str(row['tag_email_start'])
			end=str(row['tag_email_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_email']:
				pass
			else:
				i=i+1

			
		#CHECK FOR STATUS
			start=str(row['tag_status_start'])
			end=str(row['tag_status_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_status']:
				pass
			else:
				i=i+1

		#CHECK FOR MESSAGEID
			start=str(row['tag_message_start'])
			end=str(row['tag_message_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_message']:
				pass
			else:
				i=i+1


		#CHECK FOR ITEM NOTE
			start=str(row['tag_itemnote_start'])
			end=str(row['tag_itemnote_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_itemnote']:
				pass
			else:
				i=i+1


			return i

		except Exception as ex:
			print ("WARNING !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))
	
#method4
	def getinventorycheck(self):

#		with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a+') as outfile:
		with open('Test_Report.rtf','a') as outfile:
			outfile.write("\n")

			try:
			
			#CHECK FOR SKU

				start=str(row['tag_sku_start'])
				end=str(row['tag_sku_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_sku']:
					outfile.write(row['tag_sku_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_sku_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_sku_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_sku_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR Quantity
				start=str(row['tag_quantity_start'])
				end=str(row['tag_quantity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_quantity']:
					outfile.write(row['tag_quantity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_quantity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_quantity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_quantity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TITLE
				start=str(row['tag_title_start'])
				end=str(row['tag_title_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_title']:
					outfile.write(row['tag_title_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_title_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_title_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_title_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR VERSION
				start=str(row['tag_version_start'])
				end=str(row['tag_version_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_version']:
					outfile.write(row['tag_version_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_version_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_version_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_version_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR EMAIL
				start=str(row['tag_email_start'])
				end=str(row['tag_email_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_email']:
					outfile.write(row['tag_email_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_email_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_email_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_email_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

				
			#CHECK FOR STATUS
				start=str(row['tag_status_start'])
				end=str(row['tag_status_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_status']:
					outfile.write(row['tag_status_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_status_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_status_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_status_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR MESSAGEID
				start=str(row['tag_message_start'])
				end=str(row['tag_message_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_message']:
					outfile.write(row['tag_message_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_message_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_message_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_message_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM NOTE
				start=str(row['tag_itemnote_start'])
				end=str(row['tag_itemnote_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemnote']:
					outfile.write(row['tag_itemnote_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemnote_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemnote_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemnote_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			except Exception as ex:
				print ("WARNING/FAILED !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))
		



######################################CODE FOR GetSkuQuantity Call###################################

#class
class getskuquantity:
	#def __init__(self,x):
	#	self.x=x

#default method1 calling request response program	
	def __init__(self):

		obj1=inventory_request_response.requestskuquantity()	
		self.r=obj1.r
		self.xml=obj1.xml
		

#method2	
	def getskuquantitystatuscode(self):
		r=self.r
		return r

#method3
	def getskuquantitystatus(self):
	#code for parsing XML & return passed or failed (if i=0, then all passed, if i>0, some has bene failed)
	#CHECK FOR SKU
		try:
		
			i=0
			start=str(row['tag_id_start'])
			end=str(row['tag_id_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_id']:
				print ("PARSING PASED")
				pass
			else:
				i=i+1


		#CHECK FOR Quantity
			start=str(row['tag_quantity_start'])
			end=str(row['tag_quantity_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_quantity']:
				pass
			else:
				i=i+1

	
		#CHECK FOR VERSION
			start=str(row['tag_version_start'])
			end=str(row['tag_version_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_version']:
				pass
			else:
				i=i+1

		#CHECK FOR EMAIL
			start=str(row['tag_email_start'])
			end=str(row['tag_email_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_email']:
				pass
			else:
				i=i+1

			
		#CHECK FOR STATUS
			start=str(row['tag_status_start'])
			end=str(row['tag_status_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_status']:
				pass
			else:
				i=i+1

		#CHECK FOR MESSAGEID
			start=str(row['tag_message_start'])
			end=str(row['tag_message_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_message']:
				pass
			else:
				i=i+1


			return i

		except Exception as ex:
			print ("WARNING !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))
	
#method4
	def getskuquantitycheck(self):

#		with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a+') as outfile:
		with open('Test_Report.rtf','a') as outfile:
			outfile.write("\n")

			try:
			
			#CHECK FOR SKU

				start=str(row['tag_id_start'])
				end=str(row['tag_id_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_id']:
					outfile.write(row['tag_id_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_id_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_id_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_id_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR Quantity
				start=str(row['tag_quantity_start'])
				end=str(row['tag_quantity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_quantity']:
					outfile.write(row['tag_quantity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_quantity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_quantity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_quantity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR VERSION
				start=str(row['tag_version_start'])
				end=str(row['tag_version_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_version']:
					outfile.write(row['tag_version_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_version_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_version_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_version_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR EMAIL
				start=str(row['tag_email_start'])
				end=str(row['tag_email_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_email']:
					outfile.write(row['tag_email_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_email_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:			
					self.xml=self.r.content
					outfile.write(row['tag_email_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_email_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

				
			#CHECK FOR STATUS
				start=str(row['tag_status_start'])
				end=str(row['tag_status_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_status']:
					outfile.write(row['tag_status_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_status_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_status_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_status_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR MESSAGEID
				start=str(row['tag_message_start'])
				end=str(row['tag_message_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_message']:
					outfile.write(row['tag_message_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_message_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_message_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_message_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			except Exception as ex:
				print ("WARNING/FAILED !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))





			#outfile.close()

