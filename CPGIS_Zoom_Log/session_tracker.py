from openpyxl.workbook import Workbook
from openpyxl import  load_workbook
from datetime import timedelta 
import pandas as pd
import sys
import csv
import os

Subjects = {}

def main():
    if len(sys.argv)!=2:
        print("Usage ", sys.argv[0], " StudentName")
        exit(-1)

    student = sys.argv[1]

    if os.path.exists('subjects.csv') == False:
        print("Subject File Missing ")
        exit(-1)
       
    FilePath = '/mnt/g/My Drive/school_session_tracker.xlsx'

    with open('subjects.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if student==row[0]:
                subjects = list(row)
                subjects.pop(0)
                Subjects[student] = subjects
                print(student, Subjects[student])

    info = [pd.to_datetime("today").strftime('%Y-%m-%d')]

    for subject in Subjects[student][1:]:
        subjectMatter = input("Today in " + subject + " : ")
        if len(subjectMatter)>1:
            info.append(subjectMatter)
        else:
            info.append("N/A")    
    print(info)

    df = pd.DataFrame(info)
    writer = pd.ExcelWriter(FilePath, engine="openpyxl", mode='a', if_sheet_exists="overlay")
    df.transpose().to_excel(writer, student, startrow=writer.sheets[student].max_row, index=False, header=False)
    writer.save()

if __name__ == '__main__':
    main()