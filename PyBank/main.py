# import defeciencies
import os
import csv
# create the file path
path = os.path.join("..",'Resources','budget_data.csv')
#Open csv file using with open function
with open(path) as csvfile:
# Use csv.reader to read csv file and use the comma as the delimiter 
    csv_reader = csv.reader(csvfile,delimiter=",")
# Use next ('filename') to store the header row
    header = next(csv_reader)
#Store variables that will be used as counters
    count=0
    net=0
#The next  function allows the viewing of one row at a time
    line1=next(csv_reader)
#The variable previous  will be used in the for loop to determine the the month to month change in income, by storing the previous row value 
    previous=float(line1[1])
# These are all counters and variable holders
    count += 1
    net += previous
    change_sum=0
    reigning_max=0
    reigning_min=0
#The for loop is used to extract information from the column indexed as 1 and allows for the month to month change in profit and loss column
    for row in csv_reader:
        change=float(row[1]) - previous
# The if statement is triggered when the change is greater than reigning max, and the new reigning max is stored in the change variable
        if change > reigning_max:
            reigning_max=change
# The  rmax identifies the corresponding date of the reigning max in the data 
            rmax_date=row[0]
#The if statement is triggered when the change is less than reigning min, and the new reigning min is stored in the change variable
        if change < reigning_min:
            reigning_min=change
# The  rmin identifies the corresponding date of the reigning min in the data 
            rmin_date=row[0]
        reigning_max
# This counter is summing the monthly change for later use in determination of the average change
        change_sum += change
# The countr is used to keep track of the total number of rows in the new average change column
        count += 1
# A counter used to keep track of the net  total amount of "Profit/Losses" over the entire period
        net += float(row[1])
# A counter used to store the previous amount of "Profit/Losses" 
        previous=float(row[1]) 
# print function is used to print out the results of the analysis performed by the code       
        print("Row:", row, "Net:", net, "Change:", change, "Net Change:", change_sum, "Reigning Max:", reigning_max)
    av_change= change_sum/(count-1)
    print("Total Months: ", count)
    print("Total: $", net)
    print("Average Change:", av_change)
    print("Greatest Increase in Profits: ", rmax_date, " $", reigning_max)
    print("Greatest Decrease in Profits: ", rmin_date, " $", reigning_min)
# I hope the explanations were clear, but if you are confused please feel free to reach out via tolaniafolabi24@gmail.com
    