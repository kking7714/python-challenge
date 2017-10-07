import os
import csv
# Define name of CSV files as variables
file_1 = 'budget_data_1.csv'
file_2 = 'budget_data_2.csv'

def budget(file):
    file = user


    # Create file path
    csvdata_path = os.path.join('files', file)
    max = 0
    rev = 0
    min = -1

    with open(csvdata_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        totalrows=0

        for row in csvreader:
            rev = int(row[1]) + rev 
            totalrows += 1 #counting rows 
            if int(row[1]) < min: # Determine greatest decrease
                min = int(row[1])
                min_month = row[0]
                if len(min_month) == 8:
                    min_month = min_month.replace('-20', '-')   
            if int(row[1]) > max:   # Determine greatest increase
                max = int(row[1])
                max_month = row[0]
                if len(max_month) == 8:
                    max_month = max_month.replace('-20','-')

    totalmonths=totalrows #total rows minus header
    avg_rev = rev//totalmonths #is this for the whole average or just between months and then averaged?


    first_3 = "\nFinancial Analysis \n----------------------\nTotal Months: " + str(totalmonths) + "\nTotal Revenue: $" + str(rev) + "\nAverage Revenue: $" + str(avg_rev)
    min_rev_line = "\nGreatest Decrease in Revenue: " + min_month + " ($" + str(min) + ")\n"
    max_rev_line = "\nGreatest Increase in Revenue: " + max_month + " ($" + str(max) + ")"

    report = first_3 + max_rev_line + min_rev_line
    print(report)


    # Write text file with results
    if file == file_1:
        file = file_1.replace(".csv","")
    else:
        file = file_2.replace(".csv","")

    f = open('Pybank_Output' + '_' + file + '.txt','w')
    f.write(report)
    f.close()

user = input("Analyze file_1 (1) or file_2 (2)? ")

if user == "1":
    user = file_1
    budget(user)
    
elif user == "2":
    user = file_2
    budget(user)    

