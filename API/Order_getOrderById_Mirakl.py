#Coded By: Salaudeen
#Version: 1.0
#Submission Date: 07/jan/2020
#Revised Date: 12/jan/2020 [Added the queries for CSO.AMAZON table]
#Purpose: To do a regression check for GetOrderByID Call (to see if the call is success, all the data are properly fetched from DB for Amazon (cso TABLE), and also the tags and data are validated)
#Revised Date: Dec 2020
#Revised Reason: Code Revised to be compatible with python latest version 3.8.5

import requests
#from requests.auth import HTTPDigestAuth
#import php
import subprocess
import MySQLdb
import sys
import csv
import datetime
from apipackages import xml_order_mirakl_parse

now = datetime.datetime.now()

try:
#	with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a') as outfile:
	with open('Test_Report.rtf','a') as outfile:
		outfile.write("\n")
		with open('orderaz.csv') as csvDataFile:
			csvReader = csv.DictReader(csvDataFile)
			for row in csvReader:
				break
#DB connect
		try:
			connection = MySQLdb.connect (host=row['input_dbhost'], port=int(row['input_port']), user = row['input_dbuser'])
			cursor = connection.cursor ()
			connection.autocommit(True)
			cursor.execute (row['query_insert_role'])
			cursor.execute (row['query_delete_order'])
			cursor.execute (row['query_insert_order'])
			print("\n")
			outfile.write("\n")
			print("Precondition Query has been executed sucessfully")
			outfile.write("Precondition Query has been executed sucessfully")
			print ("\n")
			outfile.write("\n")
		except Exception as ex:
			print ("FAILED -> " + str(ex))
			outfile.write("FAILED -> " + str(ex))


#start time	
		print ("\n")
		outfile.write("\n")
		print("Start Date/Time of Execution : "+now.strftime("%d/%m/%Y %H:%M"))
		outfile.write("Start Date/Time of Execution : "+now.strftime("%d/%m/%Y %H:%M"))
		a = datetime.datetime.now()
		#print("\n")
		outfile.write("\n")
		#code here

		

#OOPS		
		obj1=xml_order_mirakl_parse.getorderbyid()
#call1
		r=obj1.getorderstatuscode()
		
#code for parsing XML
#Get Status code and print the results
		print ("\n")
		try:

			if int(r.status_code)==200:
	#call2
				i=obj1.getorderbyidstatus()
	#			print i


				if i==0:
					outfile.write("\n")
					outfile.write("-------------------------------------------")
					outfile.write("\n")
					print ("-------------------------------------------")
					outfile.write("ORDER API - GetOrderById --> PASSED")
					outfile.write("\n")
					print ("ORDER API - GetOrderById --> PASSED")
					outfile.write("-------------------------------------------")
					print ("-------------------------------------------")
					outfile.write("\n")
					print ("\n")

				else:
					outfile.write("\n")
					outfile.write("---------------------------------------------------------------------------")
					outfile.write("\n")
					print ("---------------------------------------------------------------------------")
					outfile.write("ORDER API - GetOrderById --> PASSED WITH ERROR / DATA MISMATCH")
					outfile.write("\n")
					print ("ORDER API - GetOrderById --> PASSED WITH ERROR / DATA MISMATCH")
					outfile.write("---------------------------------------------------------------------------")
					print ("---------------------------------------------------------------------------")
					outfile.write("\n")
					print ("\n")

				outfile.write("Please find the response details below : ")
				outfile.write("\n")
				outfile.write("\n")
				print ("Please find the response details below : "+"\n")
				outfile.write("STATUS : "+str(r.status_code))
				outfile.write("\n")
				print ("STATUS : "+str(r.status_code)+"\n")
				outfile.write("RESPONSE : ")
				outfile.write("\n")
				outfile.write(str(r.content))
				outfile.write("\n")
				print ("RESPONSE : "+"\n"+str(r.content)+"\n")
				print ("\n")
				outfile.write("\n")
	#call3
				obj1.getorderbyidcheck()

				

			elif int(r.status_code)==404:
				outfile.write("\n")
				outfile.write("-------------------------------------------")
				outfile.write("\n")
				print ("-------------------------------------------")
				outfile.write("ORDER API - GetOrderById --> FAILED")
				outfile.write("\n")
				print ("ORDER API - GetOrderById --> FAILED")
				outfile.write("-------------------------------------------")
				print ("-------------------------------------------")
				outfile.write("\n")
				print ("\n")
				outfile.write("YOUR ENDPOINT COULD BE WRONG. Please correct your data.")
				outfile.write("\n")
				print ("YOUR ENDPOINT COULD BE WRONG. Please correct your data.")
				outfile.write("\n")
				print ("\n")
				outfile.write("Please find the response details below : ")
				outfile.write("\n")
				print ("Please find the response details below : "+"\n")

				outfile.write("STATUS : "+str(r.status_code))
				outfile.write("\n")
				print ("STATUS : "+str(r.status_code)+"\n")
				outfile.write("RESPONSE : ")
				outfile.write("\n")
				outfile.write(str(r.content))
				outfile.write("\n")
				print ("RESPONSE : "+"\n"+str(r.content)+"\n")
				print ("\n")
				outfile.write("\n")

			elif int(r.status_code)==500:
				outfile.write("\n")
				outfile.write("-------------------------------------------")
				outfile.write("\n")
				print ("-------------------------------------------")
				outfile.write("ORDER API - GetOrderById --> FAILED")
				outfile.write("\n")
				print ("ORDER API - GetOrderById --> FAILED")
				outfile.write("-------------------------------------------")
				print ("-------------------------------------------")
				outfile.write("\n")
				print ("\n")
				outfile.write("INTERNAL SERVER ERROR - A security error was encountered")
				outfile.write("\n")
				print ("INTERNAL SERVER ERROR - A security error was encountered")
				print ("\n")

				outfile.write("Please find the response details below : ")
				outfile.write("\n")
				print ("Please find the response details below : "+"\n")

				outfile.write("STATUS : "+str(r.status_code))
				outfile.write("\n")
				print ("STATUS : "+str(r.status_code)+"\n")
				outfile.write("RESPONSE : ")
				outfile.write("\n")
				outfile.write(str(r.content))
				outfile.write("\n")
				print ("RESPONSE : "+"\n"+str(r.content)+"\n")
				print ("\n")
				outfile.write("\n")

			else:
				outfile.write("\n")
				outfile.write("-------------------------------------------")
				outfile.write("\n")
				print ("-------------------------------------------")
				outfile.write("ORDER API - GetOrderById --> FAILED")
				outfile.write("\n")
				print ("ORDER API - GetOrderById --> FAILED")
				outfile.write("-------------------------------------------")
				print ("-------------------------------------------")
				outfile.write("\n")
				print ("\n")

				outfile.write("Please find the response details below : ")
				outfile.write("\n")
				print ("Please find the response details below : "+"\n")

				outfile.write("STATUS : "+str(r.status_code))
				outfile.write("\n")
				print ("STATUS : "+str(r.status_code)+"\n")
				outfile.write("RESPONSE : ")
				outfile.write("\n")
				outfile.write(str(r.content))
				outfile.write("\n")
				print ("RESPONSE : "+"\n"+str(r.content)+"\n")
				print ("\n")
				outfile.write("\n")


	#End time
			print("End Date/Time of Execution : "+now.strftime("%d/%m/%Y %H:%M"))
			outfile.write("End Date/Time of Execution : "+now.strftime("%d/%m/%Y %H:%M"))
			print("\n")
			outfile.write("\n")
			b = datetime.datetime.now()
			print("Total time of Execution: "+str(b-a))
			outfile.write("Total time of Execution: "+str(b-a))
			print("\n")
			outfile.write("\n")

		except Exception as ex:
			print("RESPONSE STATUS CODE CONDITION CHECK IN THE MAIN PROGRAM FAILED..."+str(ex))

	outfile.close()

except Exception as ex:
	print("Test Report Generation Failed"+str(ex))



