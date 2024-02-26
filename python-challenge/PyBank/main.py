import csv
import os

# Function to analyze bank data
def analyze_financial_data(csv_file):
    month_count = 0
    profit_total = 0
    changes = []
    previous_profit = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the header row

        for row in csvreader:
            # Increment total months
            month_count += 1
            
            # Calculate net total
            profit_loss = int(row[1])
            profit_total += profit_loss

            # Calculate change in profit/loss
            if previous_profit != 0:
                change = profit_loss - previous_profit
                changes.append(change)

                # Update greatest increase/decrease
                if change > greatest_increase[1]:
                    greatest_increase = [row[0], change]
                if change < greatest_decrease[1]:
                    greatest_decrease = [row[0], change]

            previous_profit = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

    return month_count, profit_total, average_change, greatest_increase, greatest_decrease

# Path to the CSV file
csv_file = os.path.join('Resources', 'budget_data.csv')

# Analyze financial data
month_count, profit_total, average_change, greatest_increase, greatest_decrease = analyze_financial_data(csv_file)

output_path = os.path.join("analysis", "analysis_results.cvs")

#Output new text file with results
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {month_count}"])
    csvwriter.writerow([f"Total: ${profit_total}"])
    csvwriter.writerow([f"Average Change: ${average_change:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"])

# Print analysis results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${profit_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")