import os, csv

csv_path = os.path.join('Resources', 'budget_data.csv')
analysis_path = os.path.join('analysis', "analysis.txt")

row_ct = 0
total = 0
pl_max = ['', 0]
pl_min = ['', 0]
pl_change = 0
pl_last = 0
pl_current = 0
pl_first = 0

# splitting out the for loop contents into a method
# makes grabbing only the first value much easier
# since calling next(csv_read) is a destructive process
def check_row(row):
    # setting these to global because it makes the code easier to digest
    global row_ct, total, pl_max, pl_min, pl_change, pl_last, pl_current, pl_first
    # number of rows, being used to count months
    row_ct += 1
    # get current value
    pl_current = int(row[1])
    # calculate change as current value minus last
    pl_change = pl_current - pl_last
    # adding to total
    total += pl_current
    # check profit/loss change value with existing max and min variables
    if (pl_change > pl_max[1]):
        pl_max = [row[0], pl_change]
    if (pl_change < pl_min[1]):
        pl_min = [row[0], pl_change]
    # set up the next iteration by assigning previous row's P/L value to the current row's P/L after all the math is done
    pl_last = pl_current
    return

#both prints to console and writes to file
def write_and_print(output_str, file):
    print(output_str)
    file.write(output_str + "\n")
    return

with open(csv_path) as csv_file:

    csv_read = csv.reader(csv_file)
    # remove header from csv (file has already been checked to confirm header exists)
    csv_header = next(csv_read)
    
    #iterate first row to grab first value for average change calculation
    check_row(next(csv_read))
    pl_first = pl_current

    #iterate through remaining rows
    for row in csv_read:
        check_row(row)

#calculate average change (LaTeX $\frac{f(t_f) - f(t_0)}{t_f - t_0}$)
pl_avg = (pl_current - pl_first) / (row_ct - 1)

with open(analysis_path, "w") as a_file:
    write_and_print('Financial Analysis\n----------------------------', a_file)
    write_and_print(f'Total Months: {row_ct}\nTotal: ${total}\nAverage Change: ${pl_avg:.2f}', a_file)
    write_and_print(f'Greatest Increase in Profits: {pl_max[0]} (${pl_max[1]})', a_file)
    write_and_print(f'Greatest Decrease in Profits: {pl_min[0]} (${pl_min[1]})', a_file)