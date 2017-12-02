#!/usr/bin/python
# coding: utf-8
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'no. of the dataset: ', len(enron_data.keys())

key = enron_data.keys()[0]
print 'no. of features: ', len(enron_data[key].keys())

num_of_POI = 0
for key, value in enron_data.items():
	if enron_data[key]['poi'] == True:
		num_of_POI = num_of_POI + 1
print 'no. of POI: ', num_of_POI

print '---------- All Names ----------'
for key in enron_data.keys():
	print key

print '---------- James Prentice 名下的股票总值 ----------'
print enron_data['PRENTICE JAMES']['total_stock_value']

print '---------- no. of email from Wesley Colwell to POI ----------'
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print '---------- Jeffrey Skilling 行使的股票期权价值 ----------'
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print '---------- Jeffrey Skilling 、 Kenneth Lay 、Andrew Fastow 谁拿的钱多 ----------'
print 'LAY KENNETH L: ', enron_data['LAY KENNETH L']['total_payments']
print 'SKILLING JEFFREY K: ', enron_data['SKILLING JEFFREY K']['total_payments']
print 'FASTOW ANDREW S: ', enron_data['FASTOW ANDREW S']['total_payments']

print '---------- 有多少雇员有量化的工资？已知的邮箱地址是否可用？ ----------'
num_of_effective_salary = 0
num_of_effective_email = 0
for key, value in enron_data.items():
	if enron_data[key]['salary'] != 'NaN':
		num_of_effective_salary = num_of_effective_salary + 1
	if enron_data[key]['email_address'] != 'NaN':
		num_of_effective_email = num_of_effective_email + 1

print 'no. of effective salary: ', num_of_effective_salary
print 'no. of effective email: ', num_of_effective_email

print '---------- 有多少人的薪酬总额为“NaN”？占比多少？ ----------'
num_of_NaN_total_payment = 0
for key, value in enron_data.items():
	if enron_data[key]['total_payments'] == 'NaN':
		num_of_NaN_total_payment = num_of_NaN_total_payment + 1

print 'no. of NaN total payments: ', num_of_NaN_total_payment, \
', the proportion is: ', round(1.0*num_of_NaN_total_payment/len(enron_data.keys()), 2)

print '---------- 有多少POI的薪酬总额为“NaN”？占比多少？ ----------'
num_of_POI_NaN_total_payment = 0
for key, value in enron_data.items():
	if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True:
		num_of_POI_NaN_total_payment = num_of_POI_NaN_total_payment + 1

print 'no. of POI in NaN total payments: ', num_of_POI_NaN_total_payment, \
', the proportion is: ', round(1.0*num_of_POI_NaN_total_payment/len(enron_data.keys()), 2)


