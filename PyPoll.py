# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Clear Terminal console before executing code
def clear_console():
    os.system('clear')
clear_console()

# Assign a variable to load a file from a path.
#file_to_load = "/Users/brendenmertz/Documents/Bootcamp/03-Python/Election-Analysis/Resources/election_results.csv"
file_to_load = os.path.join("Election-Analysis","Resources", "election_results.csv")
#file_to_load = os.path.join("..","Resources", "election_results.csv")

# Assign a variable to save the file to a path.
#file_to_save = "/Users/brendenmertz/Documents/Bootcamp/03-Python/Election-Analysis/Analysis/election_analysis.txt"
file_to_save = os.path.join("Election-Analysis","Analysis", "election_analysis.txt")
#file_to_save = os.path.join("..","Analysis", "election_analysis.txt")

# initialize a total vote counter.
total_votes = 0

# Candidate Options List
candidate_options = []
# County Votes Dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County Options List
county_options = []
# County Votes Dictionary
county_votes = {}

#Track the highest turnout per county and percentage
highest_turnout_county = ""
highest_votes_county = 0
votes_per_county = 0
highest_votes_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # add to the total vote count.
        total_votes += 1

         # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Print the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add the candidate name to the candidate list.
            county_options.append(county_name)
            # Begin tracking that candidate's vote count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f" \n"
        f"County Votes:\n")

    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count of a county.
        votes = county_votes[county_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each county's name, vote count, and percentage of
        # votes to the terminal.
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the county's results to the text file.
        txt_file.write(county_results)

        # Determine winning vote count and county
        # Determine if the votes is greater than the winning count.
        if (votes > highest_votes_county) and (vote_percentage > highest_votes_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            highest_votes_count = votes
            highest_votes_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            highest_turnout_county = county_name
    
    # Summarize highest turnout county statistics
    highest_turnout_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_turnout_county}\n"
        f"-------------------------\n")
    # Print highest turnout county statistics
    print(highest_turnout_county_summary)
    
    # Save the winning candidate's name to the text file.
    txt_file.write(highest_turnout_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Summarize winning candidates statistics
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print winning candidates statistics
    print(winning_candidate_summary)
   
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

