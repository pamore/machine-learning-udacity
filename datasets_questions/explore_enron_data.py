#!/usr/bin/python

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
count = 0
count2 = 0
count3 = 0
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
for key in enron_data:
    if enron_data[key]["salary"]==1:
        count+=1
print enron_data["SKILLING JEFFREY K"]
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN" and enron_data[key]["poi"]:
        count+=1
    if enron_data[key]["total_payments"] == "NaN":
        count2+=1
    count3+=1

    # if enron_data[key]["salary"]!="NaN":
    #     count2+=1
    # if enron_data[key]["email_address"]!="NaN":
    #     count3+=1
print "count=",count
print "count2=",count2
print "count3=",count3
print "per=",(count2*100/count3)
    # if key.startswith("LAY"):
    #     print enron_data[key]["total_payments"]
    # if key.startswith("SKILLING"):
    #     print enron_data[key]["total_payments"]
    # if key.startswith("FASTOW"):
    #     print enron_data[key]["total_payments"]