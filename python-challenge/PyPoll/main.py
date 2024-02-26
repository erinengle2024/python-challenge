import csv
import os

# Function to analyze election data
def analyze_election_data(csv_file):
    total_votes = 0
    candidates_votes = {}
    winner = ""
    winner_votes = 0

    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the header row

        for row in csvreader:
            # Increment total votes
            total_votes += 1
            
            # Count votes for each candidate
            candidate = row[2]
            if candidate in candidates_votes:
                candidates_votes[candidate] += 1
            else:
                candidates_votes[candidate] = 1

    # Calculate percentage of votes for each candidate
    candidates_percentages = {}
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        candidates_percentages[candidate] = percentage

        # Update winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    return total_votes, candidates_votes, candidates_percentages, winner

# Path to the CSV file
csv_file = os.path.join('Resources','election_data.csv')

# Analyze election data
total_votes, candidates_votes, candidates_percentages, winner = analyze_election_data(csv_file)


output_path = os.path.join("analysis", "analysis_results.cvs")

#Output new text file with results
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    for candidate, votes in candidates_votes.items():
        csvwriter.writerow([f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
    

# Print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")