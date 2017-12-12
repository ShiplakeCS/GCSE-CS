pupils_list = []

pupil_file = open('people.csv', 'r')

pupil_file.readline()

for row in pupil_file:
    row = row.rstrip("\n")
    data = row.split(",")
    pupil = {'first_name':data[0], 'surname':data[1], 'age':data[2]}
    pupils_list.append(pupil)

pupil_file.close()

for p in pupils_list:
    print(p)