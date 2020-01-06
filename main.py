
# Import CSV file
import csv
from pathlib import Path

csvpath = Path('PyBank','budget_data.csv')

# Variables

count_month = 1
total_pnl = 0
worst_performance = 0
best_performance = 0
list_of_changes = []
pnl = 0

with open(csvpath, 'r') as csvfile:
    

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    skip_row = next(csvreader)
    pnl = int(skip_row[1])
    total_pnl+= int(skip_row[1])
    print(skip_row[1])
    print(csv_header)
    

# The total number of months included in the dataset.   
        
    for row in csvreader:
        print(row)
        count_month += 1
        
# Cumulative Profits/Loss
 
        total_pnl = total_pnl + int(row[1])
        print(total_pnl)
        
# Greatest Increase in Profits
        
        change = int(row[1]) - pnl
        pnl = int(row[1])
        print(pnl)
        
        if change > best_performance:
            best_performance = change
            best_month = row[0]
            
# Greatest Decrease in Profits
       
        if change < worst_performance:
            worst_performance = change
            worst_month = row[0]
# Average Change in Profits
        
        list_of_changes.append(change)
        avg_change = sum(list_of_changes) / (count_month - 1)
        
              
print('Financial Analysis:')
print("----------------------------------------------")
print('Total Months:', count_month)
print('Total Cumulative Profits/Loss:', format(total_pnl))
print('Average Change:', avg_change)
print('Greatest Increase in Profits:', best_month, best_performance)
print('Greatest Decrease in Profits:', worst_month, worst_performance)
print('Finally finished this PyBank Assigment!!!!')
print('Now I have to figure out how to write it to a text file hahahaha!!!')
print("If you are seeing this in the text file then I succeeded!!")

with open('PyBank_Its_DONE', "w") as txt_file:
    txt_file.write("Financial Analysis:\n")
    txt_file.write("----------------------------------------------\n")
    txt_file.write(f"Total Months: {count_month}\n")
    txt_file.write(f"Total Cumulative Profits/Loss: {total_pnl}\n")
    txt_file.write(f"Average Change: {avg_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {best_month} {best_performance}\n")
    txt_file.write(f"Greatest Decrease in Profits: {worst_month} {worst_performance}\n")
    txt_file.write("Finally finished this PyBank Assigment!!!!\n")
    txt_file.write("If you are seeing this in the text file then I succeeded!")
