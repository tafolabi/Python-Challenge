# import defeciencies
import os
import csv
# create the file path
path = os.path.join("..",'Resources','election_data.csv')
#Open csv file using with open function
with open(path) as csvfile:
# Use csv.reader to read csv file and use the comma as the delimiter 
    csv_reader = csv.reader(csvfile,delimiter=",")
# Use next ('filename') to store the header row
    header = next(csv_reader)
# Create empty list to store new information from the csv file
# create a counter to keep track of the total number of votes
    count=0
    Cand_list =[] 
    Vote_totals=[]
    Percent_votes=[] 
# Use a for loop to view each row in the csv file  
    for row in csv_reader:
        #if count <10: # use this during troubleshoot to reduce processing time
            count += 1
            # print(row) # view the row with print row
        # The if to identify the unique candidate names present in the indexed column #2
            if row[2] not in Cand_list:
            #Next append the unique candidate name to the initially empty cand_list[]
                Cand_list.append(row[2])
            #Use vote_totals.append(1) to count the first vote received by a candidate
                Vote_totals.append(1)
            else:
            # The Z=Cand_list.index(row[2]) is used to identify the  location of a particalar candidate 
                Z=Cand_list.index(row[2])
            # Vote_totals[Z]+=1 is the counter that tallies the votes for each candiate in the list
                Vote_totals[Z]+=1
    #Is the variable that will be used to as a proxy to determine the highest vote received by a candidate in %
    winner=0
    #A new for loop is used to calculate the percentage of each candidate's vote
    for wins in Vote_totals:
    # x is using the percentage equation of part/whole *100
        x=100*wins/count
    # The results of the percentage of votes for each candidate is the appended into the empty percent_vote list created previously.
        Percent_votes.append(x)
    # An if statement is used to identify the winning candidate by using the loogical operator. Rememeber winner = 0
        if x>winner:
            winner=x 
    # This is where the position of the winner is indexed to match the position of the percent_votes
        Z=Percent_votes.index(winner)
    # The position index from z enables us to find the position of the winning candidate and declare a winner. 
        winning_name=Cand_list[Z]

# The print statement enables the viewing of final results from the election
    print("Election Results")
    print('---------------------------------------------')
    print('Total vote cast: ', count)
    print('---------------------------------------------')
    #The for loop applied here used the idx,enumerate syntax as an inner counter in the for loop to concatenate the candidates with their total votes and percent vote.
    for idx, candidates in enumerate(Cand_list):
        print(candidates,": ", int(Percent_votes[idx]),"% (",Vote_totals[idx],")")
    print('---------------------------------------------')
    print('Winner :' , winning_name)

# I hope the explanations were clear, but if you are confused please feel free to reach out via tolaniafolabi24@gmail.com
#print('Total vote cast: ', count)
#print('Total list of Candidates :',Cand_list)
#print('Vote Tallies', Vote_totals)
#print('Percent of Vote', Percent_votes)
#print('Winner', winning_name)