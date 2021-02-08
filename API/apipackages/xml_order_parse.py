#Coded By: Salaudeen
#Version: 1.0
#Submission Date: 07/jan/2020
#Revised Date: 12/jan/2020 [Added the CSO.AMAZON fields as well]
#Purpose: To validate the Order tags and data
#Revised Date: Dec 2020
#Revised Reason: Code Revised to be compatible with python latest version 3.8.5

import sys
import os
import csv
import subprocess
import requests
import datetime
from apipackages import order_request_response


with open('orderaz.csv') as csvDataFile:
	csvReader = csv.DictReader(csvDataFile)
	for row in csvReader:
		break

#class
class getorderbyid:
	#def __init__(self,x):
	#	self.x=x

#default method1 calling request response program	
	def __init__(self):

		obj1=order_request_response.requestgetorderbyid()	
		self.r=obj1.r
		self.xml=obj1.xml
#method2	
	def getorderstatuscode(self):
		r=self.r
		return r

#method3
	def getorderbyidstatus(self):
	#code for parsing XML & return passed or failed (if i=0, then all passed, if i>0, some has bene failed)

	#CHECK FOR VERSION
		try:
			i=0
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

		#CHECK FOR MESSAGEID
			start=str(row['tag_message_start'])
			end=str(row['tag_message_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_message']:
				pass
			else:
				i=i+1


		#CHECK FOR ORDERID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderid']:
				pass
			else:
				i=i+1


		#CHECK FOR SKU
			start=str(row['tag_sku_start'])
			end=str(row['tag_sku_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_sku']:
				pass
			else:
				i=i+1
				pass

		#CHECK FOR ITEM_NAME
			start=str(row['tag_itemname_start'])
			end=str(row['tag_itemname_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_itemname']:
				pass
			else:
				i=i+1

		#CHECK FOR ORDER ITEM ID
			start=str(row['tag_orderitemid_start'])
			end=str(row['tag_orderitemid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderitemid']:
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

			
		#CHECK FOR ORDER_STATUS
			start=str(row['tag_status_start'])
			end=str(row['tag_status_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_status']:
				pass
			else:
				i=i+1


		#CHECK FOR SHIPPING TYPE (type1)
			start=str(row['tag_shippingtype_start'])
			end=str(row['tag_shippingtype_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_shippingtype']:
				pass
			else:
				i=i+1

		#CHECK FOR BILLING TYPE (type2)
			start=str(row['tag_billingtype_start'])
			end=str(row['tag_billingtype_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING NAME
			start=str(row['tag_shippingname_start'])
			end=str(row['tag_shippingname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING NAME
			start=str(row['tag_billingname_start'])
			end=str(row['tag_billingname_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER NICKNAME
			start=str(row['tag_buyernickname_start'])
			end=str(row['tag_buyernickname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyernickname']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP COMPANY NAME
			start=str(row['tag_shipcompany_start'])
			end=str(row['tag_shipcompany_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR BILL COMPANY NAME
			start=str(row['tag_billcompany_start'])
			end=str(row['tag_billcompany_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PHONE
			start=str(row['tag_shipphone_start'])
			end=str(row['tag_shipphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipphone']:
				pass

			else:
				i=i+1

		#CHECK FOR USER PHONE
			start=str(row['tag_userphone_start'])
			end=str(row['tag_userphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_userphone']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER EMAIL
			start=str(row['tag_buyeremail_start'])
			end=str(row['tag_buyeremail_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyeremail']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING ADDRESS - STREET 1
			start=str(row['tag_shipstreet1_start'])
			end=str(row['tag_shipstreet1_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 1
			start=str(row['tag_billstreet1_start'])
			end=str(row['tag_billstreet1_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING ADDRESS - STREET 2
			start=str(row['tag_shipstreet2_start'])
			end=str(row['tag_shipstreet2_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet2']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 2
			start=str(row['tag_billstreet2_start'])
			end=str(row['tag_billstreet2_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet2']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - ZIPCODE
			start=str(row['tag_shipzipcode_start'])
			end=str(row['tag_shipzipcode_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - ZIPCODE
			start=str(row['tag_billzipcode_start'])
			end=str(row['tag_billzipcode_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - CITY
			start=str(row['tag_shipcity_start'])
			end=str(row['tag_shipcity_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcity']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - CITY
			start=str(row['tag_billcity_start'])
			end=str(row['tag_billcity_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcity']:
				pass

			else:
				i=i+1



		#CHECK FOR SHIPPING - STATE
			start=str(row['tag_shipstate_start'])
			end=str(row['tag_shipstate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstate']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - STATE
			start=str(row['tag_billstate_start'])
			end=str(row['tag_billstate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstate']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - COUNTRY
			start=str(row['tag_shipcountry_start'])
			end=str(row['tag_shipcountry_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - COUNTRY
			start=str(row['tag_billcountry_start'])
			end=str(row['tag_billcountry_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE URL
			start=str(row['tag_invoiceurl_start'])
			end=str(row['tag_invoiceurl_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceurl']:
				pass

			else:
				i=i+1

		#CHECK FOR MKP NAME
			start=str(row['tag_mkpname_start'])
			end=str(row['tag_mkpname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_mkpname']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDER ID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderid']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT (price1)
			start=str(row['tag_orderinfoamount_start'])
			end=str(row['tag_orderinfoamount_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
			start=str(row['tag_orderinfoamountcurrency_start'])
			end=str(row['tag_orderinfoamountcurrency_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
			start=str(row['tag_orderinfototalamount_start'])
			end=str(row['tag_orderinfototalamount_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
			start=str(row['tag_orderinfototalamountcurrency_start'])
			end=str(row['tag_orderinfototalamountcurrency_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE DATE
			start=str(row['tag_purchasedate_start'])
			end=str(row['tag_purchasedate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchasedate']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT NAME
			start=str(row['tag_transportname_start'])
			end=str(row['tag_transportname_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportname']:
				pass

			else:
				i=i+1

		#CHECK FOR TRANSPORT - AMOUNT (price3)
			start=str(row['tag_transportamount_start'])
			end=str(row['tag_transportamount_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamount']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT - AMOUNT CURRENCY (currency3)
			start=str(row['tag_transportamountcurrency_start'])
			end=str(row['tag_transportamountcurrency_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING TYPE (rapid,etc..)
			start=str(row['tag_realshippingtype_start'])
			end=str(row['tag_realshippingtype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_realshippingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR TRACKING NUMBER
			start=str(row['tag_trackingnumber_start'])
			end=str(row['tag_trackingnumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_trackingnumber']:
				pass

			else:
				i=i+1

		#CHECK FOR DELIVERY INSTRUCTION
			start=str(row['tag_deliveryinstruction_start'])
			end=str(row['tag_deliveryinstruction_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_deliveryinstruction']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE AVAILABILITY
			start=str(row['tag_invoiceavailability_start'])
			end=str(row['tag_invoiceavailability_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceavailability']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TYPE (type3)
			start=str(row['tag_paymenttype_start'])
			end=str(row['tag_paymenttype_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_paymenttype']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT DATE (date2)
			start=str(row['tag_paymentdate_start'])
			end=str(row['tag_paymentdate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_paymentdate']:
				pass

			else:
				i=i+1


		#CHECK FOR EAN
			start=str(row['tag_ean_start'])
			end=str(row['tag_ean_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_ean']:
				pass

			else:
				i=i+1


		#CHECK FOR PRODUCT ID
			start=str(row['tag_productid_start'])
			end=str(row['tag_productid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_productid']:
				pass

			else:
				i=i+1


		#CHECK FOR LISTING ID
			start=str(row['tag_listingid_start'])
			end=str(row['tag_listingid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_listingid']:
				pass

			else:
				i=i+1


		#CHECK FOR EXTERNAL ORDER ID
			start=str(row['tag_externalorderid_start'])
			end=str(row['tag_externalorderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_externalorderid']:
				pass

			else:
				i=i+1


		#CHECK FOR UPC
			start=str(row['tag_upc_start'])
			end=str(row['tag_upc_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_upc']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PRICE (price4)
			start=str(row['tag_itemprice_start'])
			end=str(row['tag_itemprice_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itemprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PRICE CURRENCY(currency4)
			start=str(row['tag_itempricecurrency_start'])
			end=str(row['tag_itempricecurrency_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itempricecurrency']:
				pass

			else:
				i=i+1



		#CHECK FOR ITEM TAX (price5)
			start=str(row['tag_itemtax_start'])
			end=str(row['tag_itemtax_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtax']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM TAX CURRENCY(currency5)
			start=str(row['tag_itemtaxcurrency_start'])
			end=str(row['tag_itemtaxcurrency_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE (price6)
			start=str(row['tag_shippingfee_start'])
			end=str(row['tag_shippingfee_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfee']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE CURRENCY(currency6)
			start=str(row['tag_shippingfeecurrency_start'])
			end=str(row['tag_shippingfeecurrency_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfeecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX (price7)
			start=str(row['tag_shippingtax_start'])
			end=str(row['tag_shippingtax_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtax']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX CURRENCY(currency7)
			start=str(row['tag_shippingtaxcurrency_start'])
			end=str(row['tag_shippingtaxcurrency_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE
			start=str(row['tag_vatrate_start'])
			end=str(row['tag_vatrate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrate']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE SHIPPING
			start=str(row['tag_vatrateshipping_start'])
			end=str(row['tag_vatrateshipping_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrateshipping']:
				pass

			else:
				i=i+1


		#CHECK FOR REFUNDED AMOUNT (price8)
			start=str(row['tag_refundedamount_start'])
			end=str(row['tag_refundedamount_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamount']:
				pass

			else:
				i=i+1

		#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
			start=str(row['tag_refundedamountcurrency_start'])
			end=str(row['tag_refundedamountcurrency_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TRANSACTION ID
			start=str(row['tag_paymenttransactionid_start'])
			end=str(row['tag_paymenttransactionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymenttransactionid']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT STATUS
			start=str(row['tag_paymentstatus_start'])
			end=str(row['tag_paymentstatus_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymentstatus']:
				pass

			else:
				i=i+1

		#CHECK FOR OPTIONAL FEATURE PRICE (price9)
			start=str(row['tag_optionalfeatureprice_start'])
			end=str(row['tag_optionalfeatureprice_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeatureprice']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
			start=str(row['tag_optionalfeaturepricecurrency_start'])
			end=str(row['tag_optionalfeaturepricecurrency_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeaturepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX (price10)
			start=str(row['tag_optionalfeaturetax_start'])
			end=str(row['tag_optionalfeaturetax_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetax']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
			start=str(row['tag_optionalfeaturetaxcurrency_start'])
			end=str(row['tag_optionalfeaturetaxcurrency_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TYPE
			start=str(row['tag_optionalfeaturetype_start'])
			end=str(row['tag_optionalfeaturetype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetype']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TEXT
			start=str(row['tag_optionalfeaturetext_start'])
			end=str(row['tag_optionalfeaturetext_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetext']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PROMOTION ID
			start=str(row['tag_itempromotionid_start'])
			end=str(row['tag_itempromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itempromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
			start=str(row['tag_itempromotiondiscountprice_start'])
			end=str(row['tag_itempromotiondiscountprice_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
			start=str(row['tag_itempromotiondiscountpricecurrency_start'])
			end=str(row['tag_itempromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION ID
			start=str(row['tag_shippromotionid_start'])
			end=str(row['tag_shippromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
			start=str(row['tag_shippromotiondiscountprice_start'])
			end=str(row['tag_shippromotiondiscountprice_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
			start=str(row['tag_shippromotiondiscountpricecurrency_start'])
			end=str(row['tag_shippromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM NOTE
			start=str(row['tag_itemnote_start'])
			end=str(row['tag_itemnote_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemnote']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM CONDITION
			start=str(row['tag_itemcondition_start'])
			end=str(row['tag_itemcondition_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemcondition']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE (price13)
			start=str(row['tag_shippingcredittosellerprice_start'])
			end=str(row['tag_shippingcredittosellerprice_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE CURRENCY (Currency13)
			start=str(row['tag_shippingcredittosellerpricecurrency_start'])
			end=str(row['tag_shippingcredittosellerpricecurrency_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SPECIAL COMMENTS
			start=str(row['tag_specialcomments_start'])
			end=str(row['tag_specialcomments_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_specialcomments']:
				pass

			else:
				i=i+1



		#CHECK FOR INSURANCE YES OR NO
			start=str(row['tag_insuranceyesno_start'])
			end=str(row['tag_insuranceyesno_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_insuranceyesno']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE (price14)
			start=str(row['tag_insuranceprice_start'])
			end=str(row['tag_insuranceprice_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insuranceprice']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
			start=str(row['tag_insurancepricecurrency_start'])
			end=str(row['tag_insurancepricecurrency_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insurancepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR CONFIRMATION DATE
			start=str(row['tag_confirmationdate_start'])
			end=str(row['tag_confirmationdate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_confirmationdate']:
				pass

			else:
				i=i+1

		#CHECK FOR IS BUSINESS ORDER
			start=str(row['tag_isbusinessorder_start'])
			end=str(row['tag_isbusinessorder_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isbusinessorder']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE ORDER NUMBER	
			start=str(row['tag_purchaseordernumber_start'])
			end=str(row['tag_purchaseordernumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchaseordernumber']:
				pass

			else:
				i=i+1

		#CHECK FOR IS LOYALTY MEMBER	
			start=str(row['tag_isloyalty_start'])
			end=str(row['tag_isloyalty_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isloyalty']:
				pass

			else:
				i=i+1


		#CHECK FOR PRICE DESIGNATION	
			start=str(row['tag_pricedesignation_start'])
			end=str(row['tag_pricedesignation_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_pricedesignation']:
				pass

			else:
				i=i+1



			
			return i
		

		except Exception as ex:
			print ("WARNING !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))

#method4
	def getorderbyidcheck(self):

#		with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a+') as outfile:
		with open('Test_Report.rtf','a') as outfile:
			outfile.write("\n")
			outfile.write("\n")

			try:
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

			#CHECK FOR ORDER_ID
				start=str(row['tag_orderid_start'])
				end=str(row['tag_orderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderid']:
					outfile.write(row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


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


			#CHECK FOR ITEM_NAME

				start=str(row['tag_itemname_start'])
				end=str(row['tag_itemname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemname']:
					outfile.write(row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDER ITEM ID

				start=str(row['tag_orderitemid_start'])
				end=str(row['tag_orderitemid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderitemid']:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")
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

				
			#CHECK FOR ORDER_STATUS
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

			#CHECK FOR SHIPPING TYPE (type1)
				start=str(row['tag_shippingtype_start'])
				end=str(row['tag_shippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingtype']:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING TYPE (type2)
				start=str(row['tag_billingtype_start'])
				end=str(row['tag_billingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingtype']:
					outfile.write(row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING NAME
				start=str(row['tag_shippingname_start'])
				end=str(row['tag_shippingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingname']:
					outfile.write(row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR BILLING NAME
				start=str(row['tag_billingname_start'])
				end=str(row['tag_billingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingname']:
					outfile.write(row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BUYER NICKNAME
				start=str(row['tag_buyernickname_start'])
				end=str(row['tag_buyernickname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyernickname']:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP COMPANY NAME
				start=str(row['tag_shipcompany_start'])
				end=str(row['tag_shipcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcompany']:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BILL COMPANY NAME
				start=str(row['tag_billcompany_start'])
				end=str(row['tag_billcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcompany']:
					outfile.write(row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PHONE
				start=str(row['tag_shipphone_start'])
				end=str(row['tag_shipphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipphone']:
					outfile.write(row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR USER PHONE
				start=str(row['tag_userphone_start'])
				end=str(row['tag_userphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_userphone']:
					outfile.write(row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BUYER EMAIL
				start=str(row['tag_buyeremail_start'])
				end=str(row['tag_buyeremail_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyeremail']:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING ADDRESS - STREET 1
				start=str(row['tag_shipstreet1_start'])
				end=str(row['tag_shipstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet1']:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 1
				start=str(row['tag_billstreet1_start'])
				end=str(row['tag_billstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet1']:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING ADDRESS - STREET 2
				start=str(row['tag_shipstreet2_start'])
				end=str(row['tag_shipstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet2']:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 2
				start=str(row['tag_billstreet2_start'])
				end=str(row['tag_billstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet2']:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - ZIPCODE
				start=str(row['tag_shipzipcode_start'])
				end=str(row['tag_shipzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipzipcode']:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - ZIPCODE
				start=str(row['tag_billzipcode_start'])
				end=str(row['tag_billzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billzipcode']:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - CITY
				start=str(row['tag_shipcity_start'])
				end=str(row['tag_shipcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcity']:
					outfile.write(row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - CITY
				start=str(row['tag_billcity_start'])
				end=str(row['tag_billcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcity']:
					outfile.write(row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - STATE
				start=str(row['tag_shipstate_start'])
				end=str(row['tag_shipstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstate']:
					outfile.write(row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - STATE
				start=str(row['tag_billstate_start'])
				end=str(row['tag_billstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstate']:
					outfile.write(row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - COUNTRY
				start=str(row['tag_shipcountry_start'])
				end=str(row['tag_shipcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcountry']:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - COUNTRY
				start=str(row['tag_billcountry_start'])
				end=str(row['tag_billcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcountry']:
					outfile.write(row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR INVOICE URL
				start=str(row['tag_invoiceurl_start'])
				end=str(row['tag_invoiceurl_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceurl']:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR MKP NAME
				start=str(row['tag_mkpname_start'])
				end=str(row['tag_mkpname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_mkpname']:
					outfile.write(row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT (price1)
				start=str(row['tag_orderinfoamount_start'])
				end=str(row['tag_orderinfoamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamount']:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
				start=str(row['tag_orderinfoamountcurrency_start'])
				end=str(row['tag_orderinfoamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamountcurrency']:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
				start=str(row['tag_orderinfototalamount_start'])
				end=str(row['tag_orderinfototalamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamount']:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
				start=str(row['tag_orderinfototalamountcurrency_start'])
				end=str(row['tag_orderinfototalamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamountcurrency']:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PURCHASE DATE
				start=str(row['tag_purchasedate_start'])
				end=str(row['tag_purchasedate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchasedate']:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT NAME
				start=str(row['tag_transportname_start'])
				end=str(row['tag_transportname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportname']:
					outfile.write(row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT AMOUNT (price3)
				start=str(row['tag_transportamount_start'])
				end=str(row['tag_transportamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamount']:
					outfile.write(row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR TRANSPORT AMOUNT CURRENCY (currency3)
				start=str(row['tag_transportamountcurrency_start'])
				end=str(row['tag_transportamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamountcurrency']:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TYPE (Rapid , etc..)
				start=str(row['tag_realshippingtype_start'])
				end=str(row['tag_realshippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_realshippingtype']:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRACKING NUMBER
				start=str(row['tag_trackingnumber_start'])
				end=str(row['tag_trackingnumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_trackingnumber']:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR DELIVERY INSTRUCTIONS
				start=str(row['tag_deliveryinstruction_start'])
				end=str(row['tag_deliveryinstruction_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_deliveryinstruction']:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR INVOICE AVAILABILITY
				start=str(row['tag_invoiceavailability_start'])
				end=str(row['tag_invoiceavailability_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceavailability']:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TYPE (type3)
				start=str(row['tag_paymenttype_start'])
				end=str(row['tag_paymenttype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_paymenttype']:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT DATE (date2)
				start=str(row['tag_paymentdate_start'])
				end=str(row['tag_paymentdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_paymentdate']:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EAN
				start=str(row['tag_ean_start'])
				end=str(row['tag_ean_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_ean']:
					outfile.write(row['tag_ean_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_ean_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRODUCT ID
				start=str(row['tag_productid_start'])
				end=str(row['tag_productid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_productid']:
					outfile.write(row['tag_productid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_productid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR LISTING ID
				start=str(row['tag_listingid_start'])
				end=str(row['tag_listingid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_listingid']:
					outfile.write(row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EXTERNAL ORDER ID
				start=str(row['tag_externalorderid_start'])
				end=str(row['tag_externalorderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_externalorderid']:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR UPC
				start=str(row['tag_upc_start'])
				end=str(row['tag_upc_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_upc']:
					outfile.write(row['tag_upc_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_upc_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PRICE (price4)
				start=str(row['tag_itemprice_start'])
				end=str(row['tag_itemprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itemprice']:
					outfile.write(row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PRICE CURRENCY (curency4)
				start=str(row['tag_itempricecurrency_start'])
				end=str(row['tag_itempricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itempricecurrency']:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM TAX (price5)
				start=str(row['tag_itemtax_start'])
				end=str(row['tag_itemtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtax']:
					outfile.write(row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR ITEM TAX CURRENCY (curency5)
				start=str(row['tag_itemtaxcurrency_start'])
				end=str(row['tag_itemtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtaxcurrency']:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE (price6)
				start=str(row['tag_shippingfee_start'])
				end=str(row['tag_shippingfee_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfee']:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE CURRENCY (curency6)
				start=str(row['tag_shippingfeecurrency_start'])
				end=str(row['tag_shippingfeecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfeecurrency']:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TAX (price7)
				start=str(row['tag_shippingtax_start'])
				end=str(row['tag_shippingtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtax']:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING TAX CURRENCY (curency7)
				start=str(row['tag_shippingtaxcurrency_start'])
				end=str(row['tag_shippingtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtaxcurrency']:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR VAT RATE
				start=str(row['tag_vatrate_start'])
				end=str(row['tag_vatrate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrate']:
					outfile.write(row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR VAT RATE SHIPPING
				start=str(row['tag_vatrateshipping_start'])
				end=str(row['tag_vatrateshipping_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrateshipping']:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR REFUNDED AMOUNT (price8)
				start=str(row['tag_refundedamount_start'])
				end=str(row['tag_refundedamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamount']:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
				start=str(row['tag_refundedamountcurrency_start'])
				end=str(row['tag_refundedamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamountcurrency']:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TRANSACTION ID
				start=str(row['tag_paymenttransactionid_start'])
				end=str(row['tag_paymenttransactionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymenttransactionid']:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PAYMENT STATUS
				start=str(row['tag_paymentstatus_start'])
				end=str(row['tag_paymentstatus_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymentstatus']:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE PRICE (price9)
				start=str(row['tag_optionalfeatureprice_start'])
				end=str(row['tag_optionalfeatureprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeatureprice']:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
				start=str(row['tag_optionalfeaturepricecurrency_start'])
				end=str(row['tag_optionalfeaturepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeaturepricecurrency']:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TAX (price10)
				start=str(row['tag_optionalfeaturetax_start'])
				end=str(row['tag_optionalfeaturetax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetax']:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
				start=str(row['tag_optionalfeaturetaxcurrency_start'])
				end=str(row['tag_optionalfeaturetaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetaxcurrency']:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TYPE
				start=str(row['tag_optionalfeaturetype_start'])
				end=str(row['tag_optionalfeaturetype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetype']:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TEXT
				start=str(row['tag_optionalfeaturetext_start'])
				end=str(row['tag_optionalfeaturetext_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetext']:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION ID
				start=str(row['tag_itempromotionid_start'])
				end=str(row['tag_itempromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itempromotionid']:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
				start=str(row['tag_itempromotiondiscountprice_start'])
				end=str(row['tag_itempromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountprice']:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
				start=str(row['tag_itempromotiondiscountpricecurrency_start'])
				end=str(row['tag_itempromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountpricecurrency']:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIP PROMOTION ID
				start=str(row['tag_shippromotionid_start'])
				end=str(row['tag_shippromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippromotionid']:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
				start=str(row['tag_shippromotiondiscountprice_start'])
				end=str(row['tag_shippromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountprice']:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
				start=str(row['tag_shippromotiondiscountpricecurrency_start'])
				end=str(row['tag_shippromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountpricecurrency']:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
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

			#CHECK FOR ITEM CONDITION
				start=str(row['tag_itemcondition_start'])
				end=str(row['tag_itemcondition_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemcondition']:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE (price13)
				start=str(row['tag_shippingcredittosellerprice_start'])
				end=str(row['tag_shippingcredittosellerprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerprice']:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE CURRENCY (Currency13)
				start=str(row['tag_shippingcredittosellerpricecurrency_start'])
				end=str(row['tag_shippingcredittosellerpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerpricecurrency']:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SPECIAL COMMENTS
				start=str(row['tag_specialcomments_start'])
				end=str(row['tag_specialcomments_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_specialcomments']:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE YES OR NO
				start=str(row['tag_insuranceyesno_start'])
				end=str(row['tag_insuranceyesno_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_insuranceyesno']:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE (price14)
				start=str(row['tag_insuranceprice_start'])
				end=str(row['tag_insuranceprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insuranceprice']:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
				start=str(row['tag_insurancepricecurrency_start'])
				end=str(row['tag_insurancepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insurancepricecurrency']:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR CONFIRMATION DATE
				start=str(row['tag_confirmationdate_start'])
				end=str(row['tag_confirmationdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_confirmationdate']:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR IS BUSINESS ORDER
				start=str(row['tag_isbusinessorder_start'])
				end=str(row['tag_isbusinessorder_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isbusinessorder']:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PURCHASE ORDER ORDER
				start=str(row['tag_purchaseordernumber_start'])
				end=str(row['tag_purchaseordernumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchaseordernumber']:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR IS LOYALTY MEMBER
				start=str(row['tag_isloyalty_start'])
				end=str(row['tag_isloyalty_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isloyalty']:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRICE DESIGNATION
				start=str(row['tag_pricedesignation_start'])
				end=str(row['tag_pricedesignation_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_pricedesignation']:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			except Exception as ex:
				print ("WARNING/FAILED !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))




####################################CODE FOR GetOrderByDate###################################################3

#class
class getorderbydate:
	#def __init__(self,x):
	#	self.x=x

#default method1 calling request response program	
	def __init__(self):

		obj1=order_request_response.requestgetorderbydate()	
		self.r=obj1.r
		self.xml=obj1.xml
#method2	
	def getorderstatuscode(self):
		r=self.r
		return r

#method3
	def getorderbydatestatus(self):
	#code for parsing XML & return passed or failed (if i=0, then all passed, if i>0, some has bene failed)

	#CHECK FOR VERSION
		try:
			i=0
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

		#CHECK FOR MESSAGEID
			start=str(row['tag_message_start'])
			end=str(row['tag_message_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_message']:
				pass
			else:
				i=i+1


		#CHECK FOR ORDERID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderid']:
				pass
			else:
				i=i+1


		#CHECK FOR SKU
			start=str(row['tag_sku_start'])
			end=str(row['tag_sku_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_sku']:
				pass
			else:
				i=i+1
				pass

		#CHECK FOR ITEM_NAME
			start=str(row['tag_itemname_start'])
			end=str(row['tag_itemname_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_itemname']:
				pass
			else:
				i=i+1

		#CHECK FOR ORDER ITEM ID
			start=str(row['tag_orderitemid_start'])
			end=str(row['tag_orderitemid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderitemid']:
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

			
		#CHECK FOR ORDER_STATUS
			start=str(row['tag_status_start'])
			end=str(row['tag_status_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_status']:
				pass
			else:
				i=i+1


		#CHECK FOR SHIPPING TYPE (type1)
			start=str(row['tag_shippingtype_start'])
			end=str(row['tag_shippingtype_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_shippingtype']:
				pass
			else:
				i=i+1

		#CHECK FOR BILLING TYPE (type2)
			start=str(row['tag_billingtype_start'])
			end=str(row['tag_billingtype_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING NAME
			start=str(row['tag_shippingname_start'])
			end=str(row['tag_shippingname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING NAME
			start=str(row['tag_billingname_start'])
			end=str(row['tag_billingname_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER NICKNAME
			start=str(row['tag_buyernickname_start'])
			end=str(row['tag_buyernickname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyernickname']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP COMPANY NAME
			start=str(row['tag_shipcompany_start'])
			end=str(row['tag_shipcompany_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR BILL COMPANY NAME
			start=str(row['tag_billcompany_start'])
			end=str(row['tag_billcompany_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PHONE
			start=str(row['tag_shipphone_start'])
			end=str(row['tag_shipphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipphone']:
				pass

			else:
				i=i+1

		#CHECK FOR USER PHONE
			start=str(row['tag_userphone_start'])
			end=str(row['tag_userphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_userphone']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER EMAIL
			start=str(row['tag_buyeremail_start'])
			end=str(row['tag_buyeremail_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyeremail']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING ADDRESS - STREET 1
			start=str(row['tag_shipstreet1_start'])
			end=str(row['tag_shipstreet1_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 1
			start=str(row['tag_billstreet1_start'])
			end=str(row['tag_billstreet1_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING ADDRESS - STREET 2
			start=str(row['tag_shipstreet2_start'])
			end=str(row['tag_shipstreet2_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet2']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 2
			start=str(row['tag_billstreet2_start'])
			end=str(row['tag_billstreet2_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet2']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - ZIPCODE
			start=str(row['tag_shipzipcode_start'])
			end=str(row['tag_shipzipcode_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - ZIPCODE
			start=str(row['tag_billzipcode_start'])
			end=str(row['tag_billzipcode_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - CITY
			start=str(row['tag_shipcity_start'])
			end=str(row['tag_shipcity_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcity']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - CITY
			start=str(row['tag_billcity_start'])
			end=str(row['tag_billcity_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcity']:
				pass

			else:
				i=i+1



		#CHECK FOR SHIPPING - STATE
			start=str(row['tag_shipstate_start'])
			end=str(row['tag_shipstate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstate']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - STATE
			start=str(row['tag_billstate_start'])
			end=str(row['tag_billstate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstate']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - COUNTRY
			start=str(row['tag_shipcountry_start'])
			end=str(row['tag_shipcountry_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - COUNTRY
			start=str(row['tag_billcountry_start'])
			end=str(row['tag_billcountry_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE URL
			start=str(row['tag_invoiceurl_start'])
			end=str(row['tag_invoiceurl_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceurl']:
				pass

			else:
				i=i+1

		#CHECK FOR MKP NAME
			start=str(row['tag_mkpname_start'])
			end=str(row['tag_mkpname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_mkpname']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDER ID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderid']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT (price1)
			start=str(row['tag_orderinfoamount_start'])
			end=str(row['tag_orderinfoamount_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
			start=str(row['tag_orderinfoamountcurrency_start'])
			end=str(row['tag_orderinfoamountcurrency_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
			start=str(row['tag_orderinfototalamount_start'])
			end=str(row['tag_orderinfototalamount_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
			start=str(row['tag_orderinfototalamountcurrency_start'])
			end=str(row['tag_orderinfototalamountcurrency_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE DATE
			start=str(row['tag_purchasedate_start'])
			end=str(row['tag_purchasedate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchasedate']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT NAME
			start=str(row['tag_transportname_start'])
			end=str(row['tag_transportname_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportname']:
				pass

			else:
				i=i+1

		#CHECK FOR TRANSPORT - AMOUNT (price3)
			start=str(row['tag_transportamount_start'])
			end=str(row['tag_transportamount_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamount']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT - AMOUNT CURRENCY (currency3)
			start=str(row['tag_transportamountcurrency_start'])
			end=str(row['tag_transportamountcurrency_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING TYPE (rapid,etc..)
			start=str(row['tag_realshippingtype_start'])
			end=str(row['tag_realshippingtype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_realshippingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR TRACKING NUMBER
			start=str(row['tag_trackingnumber_start'])
			end=str(row['tag_trackingnumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_trackingnumber']:
				pass

			else:
				i=i+1

		#CHECK FOR DELIVERY INSTRUCTION
			start=str(row['tag_deliveryinstruction_start'])
			end=str(row['tag_deliveryinstruction_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_deliveryinstruction']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE AVAILABILITY
			start=str(row['tag_invoiceavailability_start'])
			end=str(row['tag_invoiceavailability_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceavailability']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TYPE (type3)
			start=str(row['tag_paymenttype_start'])
			end=str(row['tag_paymenttype_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_paymenttype']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT DATE (date2)
			start=str(row['tag_paymentdate_start'])
			end=str(row['tag_paymentdate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_paymentdate']:
				pass

			else:
				i=i+1


		#CHECK FOR EAN
			start=str(row['tag_ean_start'])
			end=str(row['tag_ean_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_ean']:
				pass

			else:
				i=i+1


		#CHECK FOR PRODUCT ID
			start=str(row['tag_productid_start'])
			end=str(row['tag_productid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_productid']:
				pass

			else:
				i=i+1


		#CHECK FOR LISTING ID
			start=str(row['tag_listingid_start'])
			end=str(row['tag_listingid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_listingid']:
				pass

			else:
				i=i+1


		#CHECK FOR EXTERNAL ORDER ID
			start=str(row['tag_externalorderid_start'])
			end=str(row['tag_externalorderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_externalorderid']:
				pass

			else:
				i=i+1


		#CHECK FOR UPC
			start=str(row['tag_upc_start'])
			end=str(row['tag_upc_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_upc']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PRICE (price4)
			start=str(row['tag_itemprice_start'])
			end=str(row['tag_itemprice_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itemprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PRICE CURRENCY(currency4)
			start=str(row['tag_itempricecurrency_start'])
			end=str(row['tag_itempricecurrency_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itempricecurrency']:
				pass

			else:
				i=i+1



		#CHECK FOR ITEM TAX (price5)
			start=str(row['tag_itemtax_start'])
			end=str(row['tag_itemtax_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtax']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM TAX CURRENCY(currency5)
			start=str(row['tag_itemtaxcurrency_start'])
			end=str(row['tag_itemtaxcurrency_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE (price6)
			start=str(row['tag_shippingfee_start'])
			end=str(row['tag_shippingfee_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfee']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE CURRENCY(currency6)
			start=str(row['tag_shippingfeecurrency_start'])
			end=str(row['tag_shippingfeecurrency_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfeecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX (price7)
			start=str(row['tag_shippingtax_start'])
			end=str(row['tag_shippingtax_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtax']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX CURRENCY(currency7)
			start=str(row['tag_shippingtaxcurrency_start'])
			end=str(row['tag_shippingtaxcurrency_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE
			start=str(row['tag_vatrate_start'])
			end=str(row['tag_vatrate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrate']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE SHIPPING
			start=str(row['tag_vatrateshipping_start'])
			end=str(row['tag_vatrateshipping_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrateshipping']:
				pass

			else:
				i=i+1


		#CHECK FOR REFUNDED AMOUNT (price8)
			start=str(row['tag_refundedamount_start'])
			end=str(row['tag_refundedamount_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamount']:
				pass

			else:
				i=i+1

		#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
			start=str(row['tag_refundedamountcurrency_start'])
			end=str(row['tag_refundedamountcurrency_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TRANSACTION ID
			start=str(row['tag_paymenttransactionid_start'])
			end=str(row['tag_paymenttransactionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymenttransactionid']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT STATUS
			start=str(row['tag_paymentstatus_start'])
			end=str(row['tag_paymentstatus_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymentstatus']:
				pass

			else:
				i=i+1

		#CHECK FOR OPTIONAL FEATURE PRICE (price9)
			start=str(row['tag_optionalfeatureprice_start'])
			end=str(row['tag_optionalfeatureprice_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeatureprice']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
			start=str(row['tag_optionalfeaturepricecurrency_start'])
			end=str(row['tag_optionalfeaturepricecurrency_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeaturepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX (price10)
			start=str(row['tag_optionalfeaturetax_start'])
			end=str(row['tag_optionalfeaturetax_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetax']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
			start=str(row['tag_optionalfeaturetaxcurrency_start'])
			end=str(row['tag_optionalfeaturetaxcurrency_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TYPE
			start=str(row['tag_optionalfeaturetype_start'])
			end=str(row['tag_optionalfeaturetype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetype']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TEXT
			start=str(row['tag_optionalfeaturetext_start'])
			end=str(row['tag_optionalfeaturetext_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetext']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PROMOTION ID
			start=str(row['tag_itempromotionid_start'])
			end=str(row['tag_itempromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itempromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
			start=str(row['tag_itempromotiondiscountprice_start'])
			end=str(row['tag_itempromotiondiscountprice_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
			start=str(row['tag_itempromotiondiscountpricecurrency_start'])
			end=str(row['tag_itempromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION ID
			start=str(row['tag_shippromotionid_start'])
			end=str(row['tag_shippromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
			start=str(row['tag_shippromotiondiscountprice_start'])
			end=str(row['tag_shippromotiondiscountprice_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
			start=str(row['tag_shippromotiondiscountpricecurrency_start'])
			end=str(row['tag_shippromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM NOTE
			start=str(row['tag_itemnote_start'])
			end=str(row['tag_itemnote_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemnote']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM CONDITION
			start=str(row['tag_itemcondition_start'])
			end=str(row['tag_itemcondition_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemcondition']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE (price13)
			start=str(row['tag_shippingcredittosellerprice_start'])
			end=str(row['tag_shippingcredittosellerprice_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE CURRENCY (Currency13)
			start=str(row['tag_shippingcredittosellerpricecurrency_start'])
			end=str(row['tag_shippingcredittosellerpricecurrency_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SPECIAL COMMENTS
			start=str(row['tag_specialcomments_start'])
			end=str(row['tag_specialcomments_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_specialcomments']:
				pass

			else:
				i=i+1



		#CHECK FOR INSURANCE YES OR NO
			start=str(row['tag_insuranceyesno_start'])
			end=str(row['tag_insuranceyesno_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_insuranceyesno']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE (price14)
			start=str(row['tag_insuranceprice_start'])
			end=str(row['tag_insuranceprice_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insuranceprice']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
			start=str(row['tag_insurancepricecurrency_start'])
			end=str(row['tag_insurancepricecurrency_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insurancepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR CONFIRMATION DATE
			start=str(row['tag_confirmationdate_start'])
			end=str(row['tag_confirmationdate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_confirmationdate']:
				pass

			else:
				i=i+1

		#CHECK FOR IS BUSINESS ORDER
			start=str(row['tag_isbusinessorder_start'])
			end=str(row['tag_isbusinessorder_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isbusinessorder']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE ORDER NUMBER	
			start=str(row['tag_purchaseordernumber_start'])
			end=str(row['tag_purchaseordernumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchaseordernumber']:
				pass

			else:
				i=i+1

		#CHECK FOR IS LOYALTY MEMBER	
			start=str(row['tag_isloyalty_start'])
			end=str(row['tag_isloyalty_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isloyalty']:
				pass

			else:
				i=i+1


		#CHECK FOR PRICE DESIGNATION	
			start=str(row['tag_pricedesignation_start'])
			end=str(row['tag_pricedesignation_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_pricedesignation']:
				pass

			else:
				i=i+1



			
			return i
		

		except Exception as ex:
			print ("WARNING !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))

#method4
	def getorderbydatecheck(self):

#		with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a+') as outfile:
		with open('Test_Report.rtf','a') as outfile:
			outfile.write("\n")
			outfile.write("\n")

			try:
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

			#CHECK FOR ORDER_ID
				start=str(row['tag_orderid_start'])
				end=str(row['tag_orderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderid']:
					outfile.write(row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


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


			#CHECK FOR ITEM_NAME

				start=str(row['tag_itemname_start'])
				end=str(row['tag_itemname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemname']:
					outfile.write(row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDER ITEM ID

				start=str(row['tag_orderitemid_start'])
				end=str(row['tag_orderitemid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderitemid']:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")
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

				
			#CHECK FOR ORDER_STATUS
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

			#CHECK FOR SHIPPING TYPE (type1)
				start=str(row['tag_shippingtype_start'])
				end=str(row['tag_shippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingtype']:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING TYPE (type2)
				start=str(row['tag_billingtype_start'])
				end=str(row['tag_billingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingtype']:
					outfile.write(row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING NAME
				start=str(row['tag_shippingname_start'])
				end=str(row['tag_shippingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingname']:
					outfile.write(row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR BILLING NAME
				start=str(row['tag_billingname_start'])
				end=str(row['tag_billingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingname']:
					outfile.write(row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BUYER NICKNAME
				start=str(row['tag_buyernickname_start'])
				end=str(row['tag_buyernickname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyernickname']:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP COMPANY NAME
				start=str(row['tag_shipcompany_start'])
				end=str(row['tag_shipcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcompany']:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BILL COMPANY NAME
				start=str(row['tag_billcompany_start'])
				end=str(row['tag_billcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcompany']:
					outfile.write(row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PHONE
				start=str(row['tag_shipphone_start'])
				end=str(row['tag_shipphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipphone']:
					outfile.write(row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR USER PHONE
				start=str(row['tag_userphone_start'])
				end=str(row['tag_userphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_userphone']:
					outfile.write(row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BUYER EMAIL
				start=str(row['tag_buyeremail_start'])
				end=str(row['tag_buyeremail_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyeremail']:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING ADDRESS - STREET 1
				start=str(row['tag_shipstreet1_start'])
				end=str(row['tag_shipstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet1']:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 1
				start=str(row['tag_billstreet1_start'])
				end=str(row['tag_billstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet1']:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING ADDRESS - STREET 2
				start=str(row['tag_shipstreet2_start'])
				end=str(row['tag_shipstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet2']:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 2
				start=str(row['tag_billstreet2_start'])
				end=str(row['tag_billstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet2']:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - ZIPCODE
				start=str(row['tag_shipzipcode_start'])
				end=str(row['tag_shipzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipzipcode']:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - ZIPCODE
				start=str(row['tag_billzipcode_start'])
				end=str(row['tag_billzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billzipcode']:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - CITY
				start=str(row['tag_shipcity_start'])
				end=str(row['tag_shipcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcity']:
					outfile.write(row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - CITY
				start=str(row['tag_billcity_start'])
				end=str(row['tag_billcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcity']:
					outfile.write(row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - STATE
				start=str(row['tag_shipstate_start'])
				end=str(row['tag_shipstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstate']:
					outfile.write(row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - STATE
				start=str(row['tag_billstate_start'])
				end=str(row['tag_billstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstate']:
					outfile.write(row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - COUNTRY
				start=str(row['tag_shipcountry_start'])
				end=str(row['tag_shipcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcountry']:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - COUNTRY
				start=str(row['tag_billcountry_start'])
				end=str(row['tag_billcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcountry']:
					outfile.write(row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR INVOICE URL
				start=str(row['tag_invoiceurl_start'])
				end=str(row['tag_invoiceurl_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceurl']:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR MKP NAME
				start=str(row['tag_mkpname_start'])
				end=str(row['tag_mkpname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_mkpname']:
					outfile.write(row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT (price1)
				start=str(row['tag_orderinfoamount_start'])
				end=str(row['tag_orderinfoamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamount']:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
				start=str(row['tag_orderinfoamountcurrency_start'])
				end=str(row['tag_orderinfoamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamountcurrency']:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
				start=str(row['tag_orderinfototalamount_start'])
				end=str(row['tag_orderinfototalamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamount']:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
				start=str(row['tag_orderinfototalamountcurrency_start'])
				end=str(row['tag_orderinfototalamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamountcurrency']:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PURCHASE DATE
				start=str(row['tag_purchasedate_start'])
				end=str(row['tag_purchasedate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchasedate']:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT NAME
				start=str(row['tag_transportname_start'])
				end=str(row['tag_transportname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportname']:
					outfile.write(row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT AMOUNT (price3)
				start=str(row['tag_transportamount_start'])
				end=str(row['tag_transportamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamount']:
					outfile.write(row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR TRANSPORT AMOUNT CURRENCY (currency3)
				start=str(row['tag_transportamountcurrency_start'])
				end=str(row['tag_transportamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamountcurrency']:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TYPE (Rapid , etc..)
				start=str(row['tag_realshippingtype_start'])
				end=str(row['tag_realshippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_realshippingtype']:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRACKING NUMBER
				start=str(row['tag_trackingnumber_start'])
				end=str(row['tag_trackingnumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_trackingnumber']:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR DELIVERY INSTRUCTIONS
				start=str(row['tag_deliveryinstruction_start'])
				end=str(row['tag_deliveryinstruction_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_deliveryinstruction']:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR INVOICE AVAILABILITY
				start=str(row['tag_invoiceavailability_start'])
				end=str(row['tag_invoiceavailability_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceavailability']:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TYPE (type3)
				start=str(row['tag_paymenttype_start'])
				end=str(row['tag_paymenttype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_paymenttype']:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT DATE (date2)
				start=str(row['tag_paymentdate_start'])
				end=str(row['tag_paymentdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_paymentdate']:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EAN
				start=str(row['tag_ean_start'])
				end=str(row['tag_ean_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_ean']:
					outfile.write(row['tag_ean_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_ean_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRODUCT ID
				start=str(row['tag_productid_start'])
				end=str(row['tag_productid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_productid']:
					outfile.write(row['tag_productid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_productid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR LISTING ID
				start=str(row['tag_listingid_start'])
				end=str(row['tag_listingid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_listingid']:
					outfile.write(row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EXTERNAL ORDER ID
				start=str(row['tag_externalorderid_start'])
				end=str(row['tag_externalorderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_externalorderid']:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR UPC
				start=str(row['tag_upc_start'])
				end=str(row['tag_upc_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_upc']:
					outfile.write(row['tag_upc_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_upc_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PRICE (price4)
				start=str(row['tag_itemprice_start'])
				end=str(row['tag_itemprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itemprice']:
					outfile.write(row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PRICE CURRENCY (curency4)
				start=str(row['tag_itempricecurrency_start'])
				end=str(row['tag_itempricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itempricecurrency']:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM TAX (price5)
				start=str(row['tag_itemtax_start'])
				end=str(row['tag_itemtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtax']:
					outfile.write(row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR ITEM TAX CURRENCY (curency5)
				start=str(row['tag_itemtaxcurrency_start'])
				end=str(row['tag_itemtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtaxcurrency']:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE (price6)
				start=str(row['tag_shippingfee_start'])
				end=str(row['tag_shippingfee_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfee']:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE CURRENCY (curency6)
				start=str(row['tag_shippingfeecurrency_start'])
				end=str(row['tag_shippingfeecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfeecurrency']:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TAX (price7)
				start=str(row['tag_shippingtax_start'])
				end=str(row['tag_shippingtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtax']:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING TAX CURRENCY (curency7)
				start=str(row['tag_shippingtaxcurrency_start'])
				end=str(row['tag_shippingtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtaxcurrency']:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR VAT RATE
				start=str(row['tag_vatrate_start'])
				end=str(row['tag_vatrate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrate']:
					outfile.write(row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR VAT RATE SHIPPING
				start=str(row['tag_vatrateshipping_start'])
				end=str(row['tag_vatrateshipping_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrateshipping']:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR REFUNDED AMOUNT (price8)
				start=str(row['tag_refundedamount_start'])
				end=str(row['tag_refundedamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamount']:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
				start=str(row['tag_refundedamountcurrency_start'])
				end=str(row['tag_refundedamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamountcurrency']:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TRANSACTION ID
				start=str(row['tag_paymenttransactionid_start'])
				end=str(row['tag_paymenttransactionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymenttransactionid']:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PAYMENT STATUS
				start=str(row['tag_paymentstatus_start'])
				end=str(row['tag_paymentstatus_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymentstatus']:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE PRICE (price9)
				start=str(row['tag_optionalfeatureprice_start'])
				end=str(row['tag_optionalfeatureprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeatureprice']:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
				start=str(row['tag_optionalfeaturepricecurrency_start'])
				end=str(row['tag_optionalfeaturepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeaturepricecurrency']:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TAX (price10)
				start=str(row['tag_optionalfeaturetax_start'])
				end=str(row['tag_optionalfeaturetax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetax']:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
				start=str(row['tag_optionalfeaturetaxcurrency_start'])
				end=str(row['tag_optionalfeaturetaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetaxcurrency']:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TYPE
				start=str(row['tag_optionalfeaturetype_start'])
				end=str(row['tag_optionalfeaturetype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetype']:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TEXT
				start=str(row['tag_optionalfeaturetext_start'])
				end=str(row['tag_optionalfeaturetext_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetext']:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION ID
				start=str(row['tag_itempromotionid_start'])
				end=str(row['tag_itempromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itempromotionid']:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
				start=str(row['tag_itempromotiondiscountprice_start'])
				end=str(row['tag_itempromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountprice']:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
				start=str(row['tag_itempromotiondiscountpricecurrency_start'])
				end=str(row['tag_itempromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountpricecurrency']:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIP PROMOTION ID
				start=str(row['tag_shippromotionid_start'])
				end=str(row['tag_shippromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippromotionid']:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
				start=str(row['tag_shippromotiondiscountprice_start'])
				end=str(row['tag_shippromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountprice']:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
				start=str(row['tag_shippromotiondiscountpricecurrency_start'])
				end=str(row['tag_shippromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountpricecurrency']:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
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

			#CHECK FOR ITEM CONDITION
				start=str(row['tag_itemcondition_start'])
				end=str(row['tag_itemcondition_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemcondition']:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE (price13)
				start=str(row['tag_shippingcredittosellerprice_start'])
				end=str(row['tag_shippingcredittosellerprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerprice']:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE CURRENCY (Currency13)
				start=str(row['tag_shippingcredittosellerpricecurrency_start'])
				end=str(row['tag_shippingcredittosellerpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerpricecurrency']:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SPECIAL COMMENTS
				start=str(row['tag_specialcomments_start'])
				end=str(row['tag_specialcomments_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_specialcomments']:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE YES OR NO
				start=str(row['tag_insuranceyesno_start'])
				end=str(row['tag_insuranceyesno_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_insuranceyesno']:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE (price14)
				start=str(row['tag_insuranceprice_start'])
				end=str(row['tag_insuranceprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insuranceprice']:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
				start=str(row['tag_insurancepricecurrency_start'])
				end=str(row['tag_insurancepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insurancepricecurrency']:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR CONFIRMATION DATE
				start=str(row['tag_confirmationdate_start'])
				end=str(row['tag_confirmationdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_confirmationdate']:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR IS BUSINESS ORDER
				start=str(row['tag_isbusinessorder_start'])
				end=str(row['tag_isbusinessorder_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isbusinessorder']:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PURCHASE ORDER ORDER
				start=str(row['tag_purchaseordernumber_start'])
				end=str(row['tag_purchaseordernumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchaseordernumber']:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR IS LOYALTY MEMBER
				start=str(row['tag_isloyalty_start'])
				end=str(row['tag_isloyalty_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isloyalty']:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRICE DESIGNATION
				start=str(row['tag_pricedesignation_start'])
				end=str(row['tag_pricedesignation_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_pricedesignation']:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			except Exception as ex:
				print ("WARNING/FAILED !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))



####################################CODE FOR GetOrderByStatus###################################################3

#class
class getorderbystatus:
	#def __init__(self,x):
	#	self.x=x

#default method1 calling request response program	
	def __init__(self):

		obj1=order_request_response.requestgetorderbystatus()	
		self.r=obj1.r
		self.xml=obj1.xml
#method2	
	def getorderstatuscode(self):
		r=self.r
		return r

#method3
	def getorderbystatusstatus(self):
	#code for parsing XML & return passed or failed (if i=0, then all passed, if i>0, some has bene failed)

	#CHECK FOR VERSION
		try:
			i=0
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

		#CHECK FOR MESSAGEID
			start=str(row['tag_message_start'])
			end=str(row['tag_message_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_message']:
				pass
			else:
				i=i+1


		#CHECK FOR ORDERID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderid']:
				pass
			else:
				i=i+1


		#CHECK FOR SKU
			start=str(row['tag_sku_start'])
			end=str(row['tag_sku_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_sku']:
				pass
			else:
				i=i+1
				pass

		#CHECK FOR ITEM_NAME
			start=str(row['tag_itemname_start'])
			end=str(row['tag_itemname_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_itemname']:
				pass
			else:
				i=i+1

		#CHECK FOR ORDER ITEM ID
			start=str(row['tag_orderitemid_start'])
			end=str(row['tag_orderitemid_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_orderitemid']:
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

			
		#CHECK FOR ORDER_STATUS
			start=str(row['tag_status_start'])
			end=str(row['tag_status_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_status']:
				pass
			else:
				i=i+1


		#CHECK FOR SHIPPING TYPE (type1)
			start=str(row['tag_shippingtype_start'])
			end=str(row['tag_shippingtype_end'])
			#result1 = xml.partition(Sku)[0]
			output=str(self.xml).split(start)[1].split(end)[0]
			if output == row['data_shippingtype']:
				pass
			else:
				i=i+1

		#CHECK FOR BILLING TYPE (type2)
			start=str(row['tag_billingtype_start'])
			end=str(row['tag_billingtype_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING NAME
			start=str(row['tag_shippingname_start'])
			end=str(row['tag_shippingname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING NAME
			start=str(row['tag_billingname_start'])
			end=str(row['tag_billingname_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billingname']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER NICKNAME
			start=str(row['tag_buyernickname_start'])
			end=str(row['tag_buyernickname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyernickname']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP COMPANY NAME
			start=str(row['tag_shipcompany_start'])
			end=str(row['tag_shipcompany_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR BILL COMPANY NAME
			start=str(row['tag_billcompany_start'])
			end=str(row['tag_billcompany_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcompany']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PHONE
			start=str(row['tag_shipphone_start'])
			end=str(row['tag_shipphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipphone']:
				pass

			else:
				i=i+1

		#CHECK FOR USER PHONE
			start=str(row['tag_userphone_start'])
			end=str(row['tag_userphone_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_userphone']:
				pass

			else:
				i=i+1

		#CHECK FOR BUYER EMAIL
			start=str(row['tag_buyeremail_start'])
			end=str(row['tag_buyeremail_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_buyeremail']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING ADDRESS - STREET 1
			start=str(row['tag_shipstreet1_start'])
			end=str(row['tag_shipstreet1_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 1
			start=str(row['tag_billstreet1_start'])
			end=str(row['tag_billstreet1_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet1']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING ADDRESS - STREET 2
			start=str(row['tag_shipstreet2_start'])
			end=str(row['tag_shipstreet2_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstreet2']:
				pass

			else:
				i=i+1


		#CHECK FOR BILLING ADDRESS - STREET 2
			start=str(row['tag_billstreet2_start'])
			end=str(row['tag_billstreet2_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstreet2']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - ZIPCODE
			start=str(row['tag_shipzipcode_start'])
			end=str(row['tag_shipzipcode_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - ZIPCODE
			start=str(row['tag_billzipcode_start'])
			end=str(row['tag_billzipcode_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billzipcode']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - CITY
			start=str(row['tag_shipcity_start'])
			end=str(row['tag_shipcity_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcity']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - CITY
			start=str(row['tag_billcity_start'])
			end=str(row['tag_billcity_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcity']:
				pass

			else:
				i=i+1



		#CHECK FOR SHIPPING - STATE
			start=str(row['tag_shipstate_start'])
			end=str(row['tag_shipstate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipstate']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - STATE
			start=str(row['tag_billstate_start'])
			end=str(row['tag_billstate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billstate']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING - COUNTRY
			start=str(row['tag_shipcountry_start'])
			end=str(row['tag_shipcountry_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shipcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR BILLING - COUNTRY
			start=str(row['tag_billcountry_start'])
			end=str(row['tag_billcountry_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_billcountry']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE URL
			start=str(row['tag_invoiceurl_start'])
			end=str(row['tag_invoiceurl_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceurl']:
				pass

			else:
				i=i+1

		#CHECK FOR MKP NAME
			start=str(row['tag_mkpname_start'])
			end=str(row['tag_mkpname_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_mkpname']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDER ID
			start=str(row['tag_orderid_start'])
			end=str(row['tag_orderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderid']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT (price1)
			start=str(row['tag_orderinfoamount_start'])
			end=str(row['tag_orderinfoamount_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
			start=str(row['tag_orderinfoamountcurrency_start'])
			end=str(row['tag_orderinfoamountcurrency_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_orderinfoamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
			start=str(row['tag_orderinfototalamount_start'])
			end=str(row['tag_orderinfototalamount_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamount']:
				pass

			else:
				i=i+1

		#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
			start=str(row['tag_orderinfototalamountcurrency_start'])
			end=str(row['tag_orderinfototalamountcurrency_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_orderinfototalamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE DATE
			start=str(row['tag_purchasedate_start'])
			end=str(row['tag_purchasedate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchasedate']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT NAME
			start=str(row['tag_transportname_start'])
			end=str(row['tag_transportname_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportname']:
				pass

			else:
				i=i+1

		#CHECK FOR TRANSPORT - AMOUNT (price3)
			start=str(row['tag_transportamount_start'])
			end=str(row['tag_transportamount_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamount']:
				pass

			else:
				i=i+1


		#CHECK FOR TRANSPORT - AMOUNT CURRENCY (currency3)
			start=str(row['tag_transportamountcurrency_start'])
			end=str(row['tag_transportamountcurrency_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_transportamountcurrency']:
				pass

			else:
				i=i+1

		#CHECK FOR SHIPPING TYPE (rapid,etc..)
			start=str(row['tag_realshippingtype_start'])
			end=str(row['tag_realshippingtype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_realshippingtype']:
				pass

			else:
				i=i+1

		#CHECK FOR TRACKING NUMBER
			start=str(row['tag_trackingnumber_start'])
			end=str(row['tag_trackingnumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_trackingnumber']:
				pass

			else:
				i=i+1

		#CHECK FOR DELIVERY INSTRUCTION
			start=str(row['tag_deliveryinstruction_start'])
			end=str(row['tag_deliveryinstruction_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_deliveryinstruction']:
				pass

			else:
				i=i+1

		#CHECK FOR INVOICE AVAILABILITY
			start=str(row['tag_invoiceavailability_start'])
			end=str(row['tag_invoiceavailability_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_invoiceavailability']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TYPE (type3)
			start=str(row['tag_paymenttype_start'])
			end=str(row['tag_paymenttype_end'])
			output=str(self.xml).split(start)[3].split(end)[0]	
			if output == row['data_paymenttype']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT DATE (date2)
			start=str(row['tag_paymentdate_start'])
			end=str(row['tag_paymentdate_end'])
			output=str(self.xml).split(start)[2].split(end)[0]	
			if output == row['data_paymentdate']:
				pass

			else:
				i=i+1


		#CHECK FOR EAN
			start=str(row['tag_ean_start'])
			end=str(row['tag_ean_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_ean']:
				pass

			else:
				i=i+1


		#CHECK FOR PRODUCT ID
			start=str(row['tag_productid_start'])
			end=str(row['tag_productid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_productid']:
				pass

			else:
				i=i+1


		#CHECK FOR LISTING ID
			start=str(row['tag_listingid_start'])
			end=str(row['tag_listingid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_listingid']:
				pass

			else:
				i=i+1


		#CHECK FOR EXTERNAL ORDER ID
			start=str(row['tag_externalorderid_start'])
			end=str(row['tag_externalorderid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_externalorderid']:
				pass

			else:
				i=i+1


		#CHECK FOR UPC
			start=str(row['tag_upc_start'])
			end=str(row['tag_upc_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_upc']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PRICE (price4)
			start=str(row['tag_itemprice_start'])
			end=str(row['tag_itemprice_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itemprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PRICE CURRENCY(currency4)
			start=str(row['tag_itempricecurrency_start'])
			end=str(row['tag_itempricecurrency_end'])
			output=str(self.xml).split(start)[4].split(end)[0]	
			if output == row['data_itempricecurrency']:
				pass

			else:
				i=i+1



		#CHECK FOR ITEM TAX (price5)
			start=str(row['tag_itemtax_start'])
			end=str(row['tag_itemtax_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtax']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM TAX CURRENCY(currency5)
			start=str(row['tag_itemtaxcurrency_start'])
			end=str(row['tag_itemtaxcurrency_end'])
			output=str(self.xml).split(start)[5].split(end)[0]	
			if output == row['data_itemtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE (price6)
			start=str(row['tag_shippingfee_start'])
			end=str(row['tag_shippingfee_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfee']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING FEE CURRENCY(currency6)
			start=str(row['tag_shippingfeecurrency_start'])
			end=str(row['tag_shippingfeecurrency_end'])
			output=str(self.xml).split(start)[6].split(end)[0]	
			if output == row['data_shippingfeecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX (price7)
			start=str(row['tag_shippingtax_start'])
			end=str(row['tag_shippingtax_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtax']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING TAX CURRENCY(currency7)
			start=str(row['tag_shippingtaxcurrency_start'])
			end=str(row['tag_shippingtaxcurrency_end'])
			output=str(self.xml).split(start)[7].split(end)[0]	
			if output == row['data_shippingtaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE
			start=str(row['tag_vatrate_start'])
			end=str(row['tag_vatrate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrate']:
				pass

			else:
				i=i+1


		#CHECK FOR VAT RATE SHIPPING
			start=str(row['tag_vatrateshipping_start'])
			end=str(row['tag_vatrateshipping_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_vatrateshipping']:
				pass

			else:
				i=i+1


		#CHECK FOR REFUNDED AMOUNT (price8)
			start=str(row['tag_refundedamount_start'])
			end=str(row['tag_refundedamount_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamount']:
				pass

			else:
				i=i+1

		#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
			start=str(row['tag_refundedamountcurrency_start'])
			end=str(row['tag_refundedamountcurrency_end'])
			output=str(self.xml).split(start)[8].split(end)[0]	
			if output == row['data_refundedamountcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR PAYMENT TRANSACTION ID
			start=str(row['tag_paymenttransactionid_start'])
			end=str(row['tag_paymenttransactionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymenttransactionid']:
				pass

			else:
				i=i+1

		#CHECK FOR PAYMENT STATUS
			start=str(row['tag_paymentstatus_start'])
			end=str(row['tag_paymentstatus_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_paymentstatus']:
				pass

			else:
				i=i+1

		#CHECK FOR OPTIONAL FEATURE PRICE (price9)
			start=str(row['tag_optionalfeatureprice_start'])
			end=str(row['tag_optionalfeatureprice_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeatureprice']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
			start=str(row['tag_optionalfeaturepricecurrency_start'])
			end=str(row['tag_optionalfeaturepricecurrency_end'])
			output=str(self.xml).split(start)[9].split(end)[0]	
			if output == row['data_optionalfeaturepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX (price10)
			start=str(row['tag_optionalfeaturetax_start'])
			end=str(row['tag_optionalfeaturetax_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetax']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
			start=str(row['tag_optionalfeaturetaxcurrency_start'])
			end=str(row['tag_optionalfeaturetaxcurrency_end'])
			output=str(self.xml).split(start)[10].split(end)[0]	
			if output == row['data_optionalfeaturetaxcurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TYPE
			start=str(row['tag_optionalfeaturetype_start'])
			end=str(row['tag_optionalfeaturetype_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetype']:
				pass

			else:
				i=i+1


		#CHECK FOR OPTIONAL FEATURE TEXT
			start=str(row['tag_optionalfeaturetext_start'])
			end=str(row['tag_optionalfeaturetext_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_optionalfeaturetext']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM PROMOTION ID
			start=str(row['tag_itempromotionid_start'])
			end=str(row['tag_itempromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itempromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
			start=str(row['tag_itempromotiondiscountprice_start'])
			end=str(row['tag_itempromotiondiscountprice_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
			start=str(row['tag_itempromotiondiscountpricecurrency_start'])
			end=str(row['tag_itempromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[11].split(end)[0]	
			if output == row['data_itempromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION ID
			start=str(row['tag_shippromotionid_start'])
			end=str(row['tag_shippromotionid_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_shippromotionid']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
			start=str(row['tag_shippromotiondiscountprice_start'])
			end=str(row['tag_shippromotiondiscountprice_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
			start=str(row['tag_shippromotiondiscountpricecurrency_start'])
			end=str(row['tag_shippromotiondiscountpricecurrency_end'])
			output=str(self.xml).split(start)[12].split(end)[0]	
			if output == row['data_shippromotiondiscountpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR ITEM NOTE
			start=str(row['tag_itemnote_start'])
			end=str(row['tag_itemnote_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemnote']:
				pass

			else:
				i=i+1

		#CHECK FOR ITEM CONDITION
			start=str(row['tag_itemcondition_start'])
			end=str(row['tag_itemcondition_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_itemcondition']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE (price13)
			start=str(row['tag_shippingcredittosellerprice_start'])
			end=str(row['tag_shippingcredittosellerprice_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerprice']:
				pass

			else:
				i=i+1


		#CHECK FOR SHIPPING CREDIT TO SELLER PRICE CURRENCY (Currency13)
			start=str(row['tag_shippingcredittosellerpricecurrency_start'])
			end=str(row['tag_shippingcredittosellerpricecurrency_end'])
			output=str(self.xml).split(start)[13].split(end)[0]	
			if output == row['data_shippingcredittosellerpricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR SPECIAL COMMENTS
			start=str(row['tag_specialcomments_start'])
			end=str(row['tag_specialcomments_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_specialcomments']:
				pass

			else:
				i=i+1



		#CHECK FOR INSURANCE YES OR NO
			start=str(row['tag_insuranceyesno_start'])
			end=str(row['tag_insuranceyesno_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_insuranceyesno']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE (price14)
			start=str(row['tag_insuranceprice_start'])
			end=str(row['tag_insuranceprice_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insuranceprice']:
				pass

			else:
				i=i+1


		#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
			start=str(row['tag_insurancepricecurrency_start'])
			end=str(row['tag_insurancepricecurrency_end'])
			output=str(self.xml).split(start)[14].split(end)[0]	
			if output == row['data_insurancepricecurrency']:
				pass

			else:
				i=i+1


		#CHECK FOR CONFIRMATION DATE
			start=str(row['tag_confirmationdate_start'])
			end=str(row['tag_confirmationdate_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_confirmationdate']:
				pass

			else:
				i=i+1

		#CHECK FOR IS BUSINESS ORDER
			start=str(row['tag_isbusinessorder_start'])
			end=str(row['tag_isbusinessorder_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isbusinessorder']:
				pass

			else:
				i=i+1

		#CHECK FOR PURCHASE ORDER NUMBER	
			start=str(row['tag_purchaseordernumber_start'])
			end=str(row['tag_purchaseordernumber_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_purchaseordernumber']:
				pass

			else:
				i=i+1

		#CHECK FOR IS LOYALTY MEMBER	
			start=str(row['tag_isloyalty_start'])
			end=str(row['tag_isloyalty_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_isloyalty']:
				pass

			else:
				i=i+1


		#CHECK FOR PRICE DESIGNATION	
			start=str(row['tag_pricedesignation_start'])
			end=str(row['tag_pricedesignation_end'])
			output=str(self.xml).split(start)[1].split(end)[0]	
			if output == row['data_pricedesignation']:
				pass

			else:
				i=i+1



			
			return i
		

		except Exception as ex:
			print ("WARNING !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))

#method4
	def getorderbystatuscheck(self):

#		with open('/home/sala/Salaudeen/Pythonscripts/Python-API/Test_Report.rtf','a+') as outfile:
		with open('Test_Report.rtf','a') as outfile:
			outfile.write("\n")
			outfile.write("\n")

			try:
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

			#CHECK FOR ORDER_ID
				start=str(row['tag_orderid_start'])
				end=str(row['tag_orderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderid']:
					outfile.write(row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


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


			#CHECK FOR ITEM_NAME

				start=str(row['tag_itemname_start'])
				end=str(row['tag_itemname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemname']:
					outfile.write(row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDER ITEM ID

				start=str(row['tag_orderitemid_start'])
				end=str(row['tag_orderitemid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderitemid']:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderitemid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderitemid_start']+" "+output+" => IS WRONG - FAILED")
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

				
			#CHECK FOR ORDER_STATUS
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

			#CHECK FOR SHIPPING TYPE (type1)
				start=str(row['tag_shippingtype_start'])
				end=str(row['tag_shippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingtype']:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING TYPE (type2)
				start=str(row['tag_billingtype_start'])
				end=str(row['tag_billingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingtype']:
					outfile.write(row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING NAME
				start=str(row['tag_shippingname_start'])
				end=str(row['tag_shippingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippingname']:
					outfile.write(row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR BILLING NAME
				start=str(row['tag_billingname_start'])
				end=str(row['tag_billingname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billingname']:
					outfile.write(row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billingname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billingname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BUYER NICKNAME
				start=str(row['tag_buyernickname_start'])
				end=str(row['tag_buyernickname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyernickname']:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyernickname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyernickname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP COMPANY NAME
				start=str(row['tag_shipcompany_start'])
				end=str(row['tag_shipcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcompany']:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR BILL COMPANY NAME
				start=str(row['tag_billcompany_start'])
				end=str(row['tag_billcompany_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcompany']:
					outfile.write(row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcompany_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcompany_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PHONE
				start=str(row['tag_shipphone_start'])
				end=str(row['tag_shipphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipphone']:
					outfile.write(row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR USER PHONE
				start=str(row['tag_userphone_start'])
				end=str(row['tag_userphone_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_userphone']:
					outfile.write(row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_userphone_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_userphone_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BUYER EMAIL
				start=str(row['tag_buyeremail_start'])
				end=str(row['tag_buyeremail_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_buyeremail']:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_buyeremail_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_buyeremail_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING ADDRESS - STREET 1
				start=str(row['tag_shipstreet1_start'])
				end=str(row['tag_shipstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet1']:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 1
				start=str(row['tag_billstreet1_start'])
				end=str(row['tag_billstreet1_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet1']:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet1_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet1_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING ADDRESS - STREET 2
				start=str(row['tag_shipstreet2_start'])
				end=str(row['tag_shipstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstreet2']:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING ADDRESS - STREET 2
				start=str(row['tag_billstreet2_start'])
				end=str(row['tag_billstreet2_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstreet2']:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstreet2_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstreet2_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - ZIPCODE
				start=str(row['tag_shipzipcode_start'])
				end=str(row['tag_shipzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipzipcode']:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - ZIPCODE
				start=str(row['tag_billzipcode_start'])
				end=str(row['tag_billzipcode_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billzipcode']:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billzipcode_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billzipcode_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - CITY
				start=str(row['tag_shipcity_start'])
				end=str(row['tag_shipcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcity']:
					outfile.write(row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - CITY
				start=str(row['tag_billcity_start'])
				end=str(row['tag_billcity_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcity']:
					outfile.write(row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcity_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcity_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - STATE
				start=str(row['tag_shipstate_start'])
				end=str(row['tag_shipstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipstate']:
					outfile.write(row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - STATE
				start=str(row['tag_billstate_start'])
				end=str(row['tag_billstate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billstate']:
					outfile.write(row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billstate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billstate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIPPING - COUNTRY
				start=str(row['tag_shipcountry_start'])
				end=str(row['tag_shipcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shipcountry']:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shipcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shipcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR BILLING - COUNTRY
				start=str(row['tag_billcountry_start'])
				end=str(row['tag_billcountry_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_billcountry']:
					outfile.write(row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_billcountry_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_billcountry_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR INVOICE URL
				start=str(row['tag_invoiceurl_start'])
				end=str(row['tag_invoiceurl_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceurl']:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceurl_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceurl_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR MKP NAME
				start=str(row['tag_mkpname_start'])
				end=str(row['tag_mkpname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_mkpname']:
					outfile.write(row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_mkpname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_mkpname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT (price1)
				start=str(row['tag_orderinfoamount_start'])
				end=str(row['tag_orderinfoamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamount']:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - AMOUNT CURRENCY (currency1)
				start=str(row['tag_orderinfoamountcurrency_start'])
				end=str(row['tag_orderinfoamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_orderinfoamountcurrency']:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfoamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ORDERINFO - TOTAL AMOUNT (price2)
				start=str(row['tag_orderinfototalamount_start'])
				end=str(row['tag_orderinfototalamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamount']:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ORDERINFO - TOTAL AMOUNT CURRENCY (currency2)
				start=str(row['tag_orderinfototalamountcurrency_start'])
				end=str(row['tag_orderinfototalamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_orderinfototalamountcurrency']:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_orderinfototalamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PURCHASE DATE
				start=str(row['tag_purchasedate_start'])
				end=str(row['tag_purchasedate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchasedate']:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchasedate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchasedate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT NAME
				start=str(row['tag_transportname_start'])
				end=str(row['tag_transportname_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportname']:
					outfile.write(row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportname_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportname_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRANSPORT AMOUNT (price3)
				start=str(row['tag_transportamount_start'])
				end=str(row['tag_transportamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamount']:
					outfile.write(row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR TRANSPORT AMOUNT CURRENCY (currency3)
				start=str(row['tag_transportamountcurrency_start'])
				end=str(row['tag_transportamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_transportamountcurrency']:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_transportamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TYPE (Rapid , etc..)
				start=str(row['tag_realshippingtype_start'])
				end=str(row['tag_realshippingtype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_realshippingtype']:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_realshippingtype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_realshippingtype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR TRACKING NUMBER
				start=str(row['tag_trackingnumber_start'])
				end=str(row['tag_trackingnumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_trackingnumber']:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_trackingnumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_trackingnumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR DELIVERY INSTRUCTIONS
				start=str(row['tag_deliveryinstruction_start'])
				end=str(row['tag_deliveryinstruction_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_deliveryinstruction']:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_deliveryinstruction_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR INVOICE AVAILABILITY
				start=str(row['tag_invoiceavailability_start'])
				end=str(row['tag_invoiceavailability_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_invoiceavailability']:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_invoiceavailability_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TYPE (type3)
				start=str(row['tag_paymenttype_start'])
				end=str(row['tag_paymenttype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[3].split(end)[0]
				if output == row['data_paymenttype']:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT DATE (date2)
				start=str(row['tag_paymentdate_start'])
				end=str(row['tag_paymentdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[2].split(end)[0]
				if output == row['data_paymentdate']:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EAN
				start=str(row['tag_ean_start'])
				end=str(row['tag_ean_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_ean']:
					outfile.write(row['tag_ean_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_ean_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_ean_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRODUCT ID
				start=str(row['tag_productid_start'])
				end=str(row['tag_productid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_productid']:
					outfile.write(row['tag_productid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_productid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_productid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR LISTING ID
				start=str(row['tag_listingid_start'])
				end=str(row['tag_listingid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_listingid']:
					outfile.write(row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_listingid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_listingid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR EXTERNAL ORDER ID
				start=str(row['tag_externalorderid_start'])
				end=str(row['tag_externalorderid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_externalorderid']:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_externalorderid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_externalorderid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR UPC
				start=str(row['tag_upc_start'])
				end=str(row['tag_upc_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_upc']:
					outfile.write(row['tag_upc_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_upc_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_upc_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PRICE (price4)
				start=str(row['tag_itemprice_start'])
				end=str(row['tag_itemprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itemprice']:
					outfile.write(row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PRICE CURRENCY (curency4)
				start=str(row['tag_itempricecurrency_start'])
				end=str(row['tag_itempricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[4].split(end)[0]
				if output == row['data_itempricecurrency']:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM TAX (price5)
				start=str(row['tag_itemtax_start'])
				end=str(row['tag_itemtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtax']:
					outfile.write(row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR ITEM TAX CURRENCY (curency5)
				start=str(row['tag_itemtaxcurrency_start'])
				end=str(row['tag_itemtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[5].split(end)[0]
				if output == row['data_itemtaxcurrency']:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE (price6)
				start=str(row['tag_shippingfee_start'])
				end=str(row['tag_shippingfee_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfee']:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfee_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfee_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING FEE CURRENCY (curency6)
				start=str(row['tag_shippingfeecurrency_start'])
				end=str(row['tag_shippingfeecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[6].split(end)[0]
				if output == row['data_shippingfeecurrency']:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingfeecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIPPING TAX (price7)
				start=str(row['tag_shippingtax_start'])
				end=str(row['tag_shippingtax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtax']:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR SHIPPING TAX CURRENCY (curency7)
				start=str(row['tag_shippingtaxcurrency_start'])
				end=str(row['tag_shippingtaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[7].split(end)[0]
				if output == row['data_shippingtaxcurrency']:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingtaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR VAT RATE
				start=str(row['tag_vatrate_start'])
				end=str(row['tag_vatrate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrate']:
					outfile.write(row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR VAT RATE SHIPPING
				start=str(row['tag_vatrateshipping_start'])
				end=str(row['tag_vatrateshipping_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_vatrateshipping']:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_vatrateshipping_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR REFUNDED AMOUNT (price8)
				start=str(row['tag_refundedamount_start'])
				end=str(row['tag_refundedamount_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamount']:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamount_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamount_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR REFUNDED AMOUNT CURRENCY (currency8)
				start=str(row['tag_refundedamountcurrency_start'])
				end=str(row['tag_refundedamountcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[8].split(end)[0]
				if output == row['data_refundedamountcurrency']:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_refundedamountcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PAYMENT TRANSACTION ID
				start=str(row['tag_paymenttransactionid_start'])
				end=str(row['tag_paymenttransactionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymenttransactionid']:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymenttransactionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR PAYMENT STATUS
				start=str(row['tag_paymentstatus_start'])
				end=str(row['tag_paymentstatus_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_paymentstatus']:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_paymentstatus_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_paymentstatus_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE PRICE (price9)
				start=str(row['tag_optionalfeatureprice_start'])
				end=str(row['tag_optionalfeatureprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeatureprice']:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeatureprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")

			#CHECK FOR OPTIONAL FEATURE PRICE CURRENCY (currency9)
				start=str(row['tag_optionalfeaturepricecurrency_start'])
				end=str(row['tag_optionalfeaturepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[9].split(end)[0]
				if output == row['data_optionalfeaturepricecurrency']:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TAX (price10)
				start=str(row['tag_optionalfeaturetax_start'])
				end=str(row['tag_optionalfeaturetax_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetax']:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetax_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR OPTIONAL FEATURE TAX CURRENCY (Currency10)
				start=str(row['tag_optionalfeaturetaxcurrency_start'])
				end=str(row['tag_optionalfeaturetaxcurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[10].split(end)[0]
				if output == row['data_optionalfeaturetaxcurrency']:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetaxcurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TYPE
				start=str(row['tag_optionalfeaturetype_start'])
				end=str(row['tag_optionalfeaturetype_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetype']:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetype_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR OPTIONAL FEATURE TEXT
				start=str(row['tag_optionalfeaturetext_start'])
				end=str(row['tag_optionalfeaturetext_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_optionalfeaturetext']:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_optionalfeaturetext_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION ID
				start=str(row['tag_itempromotionid_start'])
				end=str(row['tag_itempromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itempromotionid']:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE (price11)
				start=str(row['tag_itempromotiondiscountprice_start'])
				end=str(row['tag_itempromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountprice']:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR ITEM PROMOTION DISCOUNT PRICE CURRENCY (Currency11)
				start=str(row['tag_itempromotiondiscountpricecurrency_start'])
				end=str(row['tag_itempromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[11].split(end)[0]
				if output == row['data_itempromotiondiscountpricecurrency']:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itempromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SHIP PROMOTION ID
				start=str(row['tag_shippromotionid_start'])
				end=str(row['tag_shippromotionid_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_shippromotionid']:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotionid_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotionid_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE (price12)
				start=str(row['tag_shippromotiondiscountprice_start'])
				end=str(row['tag_shippromotiondiscountprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountprice']:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP PROMOTION DISCOUNT PRICE CURRENCY (Currency12)
				start=str(row['tag_shippromotiondiscountpricecurrency_start'])
				end=str(row['tag_shippromotiondiscountpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[12].split(end)[0]
				if output == row['data_shippromotiondiscountpricecurrency']:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippromotiondiscountpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
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

			#CHECK FOR ITEM CONDITION
				start=str(row['tag_itemcondition_start'])
				end=str(row['tag_itemcondition_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_itemcondition']:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_itemcondition_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_itemcondition_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE (price13)
				start=str(row['tag_shippingcredittosellerprice_start'])
				end=str(row['tag_shippingcredittosellerprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerprice']:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR SHIP CREDIT TO SELLER PRICE CURRENCY (Currency13)
				start=str(row['tag_shippingcredittosellerpricecurrency_start'])
				end=str(row['tag_shippingcredittosellerpricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[13].split(end)[0]
				if output == row['data_shippingcredittosellerpricecurrency']:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_shippingcredittosellerpricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR SPECIAL COMMENTS
				start=str(row['tag_specialcomments_start'])
				end=str(row['tag_specialcomments_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_specialcomments']:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_specialcomments_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_specialcomments_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE YES OR NO
				start=str(row['tag_insuranceyesno_start'])
				end=str(row['tag_insuranceyesno_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_insuranceyesno']:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceyesno_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE (price14)
				start=str(row['tag_insuranceprice_start'])
				end=str(row['tag_insuranceprice_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insuranceprice']:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insuranceprice_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insuranceprice_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR INSURANCE PRICE CURRENCY (Currency14)
				start=str(row['tag_insurancepricecurrency_start'])
				end=str(row['tag_insurancepricecurrency_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[14].split(end)[0]
				if output == row['data_insurancepricecurrency']:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_insurancepricecurrency_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR CONFIRMATION DATE
				start=str(row['tag_confirmationdate_start'])
				end=str(row['tag_confirmationdate_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_confirmationdate']:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_confirmationdate_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_confirmationdate_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			#CHECK FOR IS BUSINESS ORDER
				start=str(row['tag_isbusinessorder_start'])
				end=str(row['tag_isbusinessorder_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isbusinessorder']:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isbusinessorder_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PURCHASE ORDER ORDER
				start=str(row['tag_purchaseordernumber_start'])
				end=str(row['tag_purchaseordernumber_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_purchaseordernumber']:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_purchaseordernumber_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR IS LOYALTY MEMBER
				start=str(row['tag_isloyalty_start'])
				end=str(row['tag_isloyalty_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_isloyalty']:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_isloyalty_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_isloyalty_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")


			#CHECK FOR PRICE DESIGNATION
				start=str(row['tag_pricedesignation_start'])
				end=str(row['tag_pricedesignation_end'])
				#result1 = xml.partition(Sku)[0]
				output=str(self.xml).split(start)[1].split(end)[0]
				if output == row['data_pricedesignation']:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")		
					print (row['tag_pricedesignation_start']+" "+output+" => Verified and it is PASSED")
					print ("\n")
					outfile.write("\n")
					#print((xml.split(start))[1].split(end)[0])
				else:
					outfile.write(row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")		
					print (row['tag_pricedesignation_start']+" "+output+" => IS WRONG - FAILED")
					print ("\n")
					outfile.write("\n")



			except Exception as ex:
				print ("WARNING/FAILED !!! MAY BE THE COLUMN/DATA ARE MISSING IN YOUR INPUT FILE. PLEASE FILL THE REQUIRED TEST DATA AND TRY AGAIN.." + str(ex))

			#outfile.close()

