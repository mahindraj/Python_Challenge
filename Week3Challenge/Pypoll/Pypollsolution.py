# Creating the path file 
import os
# Reading the CSV files
import csv
# Setting a path for the  file
filepath = os.path.join('Week3Challenge', 'Pypoll','Resources', 'election_data.csv')

# Opening the CSV
with open(filepath, newline='') as csvfile:

    # CSV reader specifiing the delimiter and variable that holds contents within the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]
    
# Calculating the number of total votes
total_votes = len(candidate_list)

# Creating a unique list of the candidates with the corresponding number of votes
candidates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Sorting the list so that the first candidate becomes the winner 
canditates_info = sorted(candidates_info, key=lambda x: x[1], reverse=True)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


#  Printing the  election results to text file 
# Set path for file
filepath = os.path.join('Week3Challenge', 'Pypoll', 'Analysis', 'results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in candidates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {candidates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)