import os, csv

csv_path = os.path.join('Resources', 'election_data.csv')
analysis_path = os.path.join('analysis', "analysis.txt")

# will be used to count votes in this case
row_ct = 0
# will contain candidate names as keys, and number of votes for candidate as value
candidates = {}
# stored as a tuple because it seemed appropriate to make immutable
winner = ("", 0)

# both prints to console and writes to file
def write_and_print(output_str, file):
    print(output_str)
    file.write(output_str + "\n")
    return

with open(csv_path) as csv_file:

    csv_read = csv.reader(csv_file)
    # remove header from csv (file has already been checked to confirm header exists)
    next(csv_read)

    # iterate through rows
    for row in csv_read:
        # count total rows (aka votes) + 1
        row_ct += 1
        # tick votes per candidate up if candidate already exists in variable
        if candidates.__contains__(row[2]):
            candidates[row[2]] += 1
        # give candidate first vote if they are a new variable entry
        else:
            candidates[row[2]] = 1


with open(analysis_path, "w") as a_file:
    # stored this line as a variable for character efficiency
    h_line = "-------------------------"
    # print header to console and file
    write_and_print(f"Election Results\n{h_line}\nTotal Votes: {row_ct}\n{h_line}", a_file)
    # iterate through candidates, assign percentages from total votes and write+print those to console/file
    # also determines winner by checking if vote count is higher than existing value in winner variable
    for can in candidates:
        candidates[can] = [candidates[can], round(candidates[can] / row_ct * 100, 3)]
        write_and_print(f"{can}: {candidates[can][1]}% ({candidates[can][0]})", a_file)
        if winner[1] < candidates[can][0]:
            winner = (can, candidates[can][0])
    # print footer with winner's name
    write_and_print(f"{h_line}\nWinner: {winner[0]}\n{h_line}", a_file)