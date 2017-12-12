def get_person_details():

    first_name = input("Enter first name: ")
    surname = input("Enter surname: ")
    age = int(input("Enter age: "))

    person = {'first_name':first_name, 'surname':surname, 'age':age}

    return person


def save_person_details(people):
    pass

keep_adding = True

list_of_people = []

while keep_adding:

    person = get_person_details()
    list_of_people.append(person)

    repeat_check = input("Do you want to add another person's details (y/n)? ")

    if repeat_check.lower() == 'n':
        keep_adding = False

print(list_of_people)