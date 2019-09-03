# Ammended code for Exercise 1
comsci_10b = [{'FirstName':'Mark','Surname':'Davies','Form':'10H','AssScores':[87,67,72, 82]},
              {'FirstName':'Ahad','Surname':'Ferar','Form':'10H','AssScores':[72,68,65, 23]},
              {'FirstName':'James','Surname':'Howard','Form':'10B','AssScores':[47,35,52, 14]},
              {'FirstName':'Bob','Surname':'Martin','Form':'10B','AssScores':[82,78,79, 85]},
              {'FirstName':'Jon','Surname':'Smith','Form':'10H','AssScores':[67,68,82]},
              {'FirstName':'Michelle','Surname':'Sorin','Form':'10W','AssScores':[91,88,93, 75]},
              {'FirstName':'Lucy','Surname':'Tucker','Form':'10W','AssScores':[48,30,52, 37]}]

# Write your code for Exercise 2 a), b) and c) below:

# Write your code for Exercise 3 below:

# Write your code and comments for Exercise 4 below:
for pupil in comsci_10b:
    total_score = 0
    for score in pupil['AssScores']:
        total_score = total_score + score
    average = total_score / len(pupil['AssScores'])
    pupil['Av'] = average
    
# Write your solution to the challenge task below:

for pupil in comsci_10b:
    print("Name:{0} {1} ({2})".format(pupil['FirstName'], pupil['Surname'], pupil['Form']))
    print()
    print("Assignment scores:")
    print("------------------")
    score_counter = 0
    for score in pupil['AssScores']:
        score_counter += 1
        print("Assignment {0}: {1}".format(score_counter, score))
    print("Average score: {0:0.2f}".format(pupil['Av']))
    print("\n\n")
