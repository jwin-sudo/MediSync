import csv
import zulu
from datetime import datetime
import re


def openFile():
    with open('MediSync.csv', mode='r') as file:
        split_lines = file.read().split('\n')
    return split_lines


def extractPatient():
    array_of_strings = openFile()
    arr = []
    for i in range(0, len(array_of_strings), 1):
        if 'Patient' in array_of_strings[i]:
            get_names = array_of_strings[i].split(' ')
            arr.append(get_names[1])
    return arr


def countTreatment():
    array_of_strings = openFile()
    list_of_names = extractPatient()

    counter = 0
    treatment_arr = []
    for i in range(0, len(list_of_names), 1):
        for j in range(0, len(array_of_strings), 1):
            if list_of_names[i] in array_of_strings[j] and 'Treatment' in array_of_strings[j]:
                counter = counter + 1
        treatment_arr.append(counter)
        counter = 0
    return treatment_arr


def timeStayed():
    array_of_strings = openFile()
    list_of_names = extractPatient()

    arr = []
    date_arr = []
    time_arr = []

    final_arr = []

    start = 0
    end = 1

    for i in range(0, len(list_of_names), 1):
        for j in range(0, len(array_of_strings), 1):
            if list_of_names[i] in array_of_strings[j] and ('Action Intake' in array_of_strings[j] or 'Action Discharge' in array_of_strings[j]):
                get_times = array_of_strings[j].split(' ', 4)
                arr.append(get_times)

    for i in range(0, len(arr), 1):
        date_and_time = re.split('T|Z', arr[i][3])
        date_arr.append(date_and_time[0])
        time_arr.append(date_and_time[1])

    while start < len(date_arr) and start < len(time_arr):
        str_d1 = date_arr[start]
        str_d2 = date_arr[end]
        str_t1 = time_arr[start]
        str_t2 = time_arr[end]

        # convert string to date object
        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(str_d2, "%Y-%m-%d")

        t1 = datetime.strptime(str_t1, "%H:%M:%S")
        t2 = datetime.strptime(str_t2, "%H:%M:%S")

        delta = d2 - d1
        delta2 = t2 - t1

        final_arr.append({delta.days*24 + delta2.total_seconds()/(60*60)})

        start = start + 2
        end = end + 2
    return final_arr


names = extractPatient()
treatment = countTreatment()
time = timeStayed()

i = 0
while i < len(names):
    print('Patient ', names[i], 'stayed for ', time[i],
          'hours and received ', treatment[i], 'treatments')
    i = i+1
    if i == len(names):
        break
