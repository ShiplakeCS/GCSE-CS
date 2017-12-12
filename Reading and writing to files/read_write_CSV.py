import csv

"""Method 1: Using a CSV reader"""
with open('gym_members.csv', 'r') as member_file:
    reader = csv.reader(member_file)
    member_list = list(reader)

print(member_list)

"""Method 2: Manually splitting the line"""

member_file = open("gym_members.csv", "r")

members = [] # Create an empty list, ready to fill with details of each member

member_file.readline() # read the first line, but don't do anything with it - it contains the headers, so we can skip it

for line in member_file:

    line = line.rstrip("\n") # removes the new line character from the end of the line

    data_row = line.split(",") # get a list made up of each item of data in the row, splitting the row every time a ',' is found

    member_details = {'member_number':data_row[0], 'first_name':data_row[1], 'surname':data_row[2]} # Create a dictionary that contains the details of this member

    members.append(member_details) # add that row of data to the members list

member_file.close()

print(members)

members.pop(0)  # Remove the first item from the list (the headers)

print(members)


"""Method 3: Use CSV reader with ordered dictionary"""

members = []

#with open("gym_members.csv", 'r') as member_file:
member_file = open("gym_members.csv", "r")

reader = csv.DictReader(member_file)

for row in reader:
    members.append(row)

member_file.close()

for m in members:
    print(m['first_name'], m['last_name'])


with open('out_file.csv','w') as output_file:
    writer = csv.DictWriter(output_file, ['first_name', 'surname', 'age'])
    writer.writeheader()
    writer.writerow({'first_name':'Adam', 'surname':'Dimmick','age':33})
    writer.writerow({'first_name': 'Louise', 'surname': 'Dimmick', 'age': 28})



"""
Tasks to perform

Ask the user for some details and save to a dictionary
Repeat for two or three sets of details
Save to a file in CSV format


Open a CSV file with a few details stored
Print to screen
Use to populate dictionary
Print specific details


Load all members from gym
Print all member's details on screen (check it works)
Ask to see only active members (value = true)
Ask user to enter name of a person - only print if name (surname) or membership number matches

Add a new member's details - append to end of CSV file

Update a user's details - search if they are present, if so, print existing details and ask user to enter new details


"""