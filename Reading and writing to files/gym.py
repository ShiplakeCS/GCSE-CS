members = []
member_file = open("gym_members2.csv", "r")

member_file.readline()  # ignore header row

for row in member_file:
    row = row.rstrip("\n")
    data = row.split(",")
    member = {'membership_number': data[0], 'first_name': data[1], 'last_name': data[2], 'email': data[3],
              'gender': data[4], 'active_member': data[5], 'cc_number': data[6]}
    members.append(member)

member_file.close()


# membership_number,first_name,last_name,email,gender,active_member,cc_number

def main_menu():
    """

    """
    print("\nMAIN MENU")
    print("1. Show details of all members")
    print("2. Search for a member by number")
    print("3. Show inactive members")
    print("4. Update a member's details")
    print("5. Add details of a new member")
    print("6. Save data back to file")
    print("0. Quit")
    print()

    option = ""

    while option not in ['1', '2', '3', '4', '5', '6', '0']:
        option = input("Please select an option (1-6) from the menu: ")

    if option == '0':
        confirm = input("Are you sure (y/n)? ")
        if confirm.lower() == 'y':
            print("Bye!")
            quit()

    elif option == "1":
        show_all_members()

    elif option == "2":
        search_for_member()

    elif option == "3":
        show_inactive_members()

    elif option == "4":
        update_member()

    elif option == "5":
        add_new_member()

    elif option == "6":
        save_to_file()


def show_all_members():
    global members

    for member in members:
        print("Membership Number:", member['membership_number'])
        print("First name:", member['first_name'])
        print("Last name:", member['last_name'])
        print("Gender:", member['gender'])
        print("Email address:", member['email'])
        print("Active member?", member['active_member'])
        print("Credit Card number:", member['cc_number'])
        print("-----------------------------------------")


def search_for_member():
    global members

    member_num = input("\nEnter the membership number to search for: ")

    found = False

    for member in members:

        if member['membership_number'] == member_num:
            found = True

            print("\nMembership Number:", member['membership_number'])
            print("First name:", member['first_name'])
            print("Last name:", member['last_name'])
            print("Gender:", member['gender'])
            print("Email address:", member['email'])
            print("Active member?", member['active_member'])
            print("Credit Card number:", member['cc_number'])
            print("-----------------------------------------")
            break

    if found == False:
        print("Member not found!")
        input("\nPress Enter to continue...")


def update_member():
    global members

    member_num = input("\nEnter the membership number to update for: ")

    found = False

    for member in members:

        if member['membership_number'] == member_num:

            found = True

            print("\n*** Leave blank to retain existing data! ***\n")

            firstname = input("Update first name (currently {0}): ".format(member['first_name']))
            lastname = input("Update last name (currently {0}): ".format(member['last_name']))
            gender = input("Update gender (Male/Female) (currently {0}): ".format(member['gender']))
            email = input("Update email address (currently {0}): ".format(member['email']))
            cc_num = input("Update credit card number (currently {0}): ".format(member['cc_number']))
            active = input("Update active status (currently {0}): ".format(member['active_member']))

            if firstname != "":
                member['first_name'] = firstname

            if lastname != "":
                member['last_name'] = lastname

            if gender != "":
                member['gender'] = gender

            if email != "":
                member['email'] = email

            if cc_num != "":
                member['cc_number'] = cc_num

            if active != "":
                member['active_member'] = active

            print("\nDetails updated!")

            break

    if found == False:
        print("Member not found!")
        input("\nPress Enter to continue...")


def show_inactive_members():
    global members

    print("\nINACTIVE MEMBERS:\n")

    for member in members:

        if member['active_member'] == "false":
            print("\nMembership Number:", member['membership_number'])
            print("First name:", member['first_name'])
            print("Last name:", member['last_name'])
            print("Email address:", member['email'])
            print("-----------------------------------------")


def get_new_membership_number():
    global members

    return len(members) + 1


def add_new_member():
    global members

    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    gender = input("Enter gender (m/f): ")
    email = input("Enter email address: ")
    cc_num = input("Enter credit card number: ")

    active = "true"

    membership_number = str(get_new_membership_number())

    new_member = {'membership_number': membership_number, 'first_name': firstname, 'last_name': lastname,
                  'gender': gender, 'active_member': 'true', 'cc_number': cc_num, 'email': email}

    members.append(new_member)


def save_to_file():
    """
    Saves dictionary objects stored in global members list to a CSV file.

    """
    global members

    confirm = input("This will overwrite the existing datafile. Are you sure you wish to do this (y/n)? ")
    if confirm.lower() == "y":

        save_file = open('gym_members.csv', 'w')

        save_file.write("membership_number,first_name,last_name,email,gender,active_member,cc_number\n")

        for item in members:
            csv_row = item['membership_number'] + ',' + item['first_name'] + "," + item['last_name'] + ',' + item[
                'email'] + ',' + item['gender'] + ',' + item['active_member'] + ',' + item['cc_number'] + "\n"
            save_file.write(csv_row)

        save_file.close()

        print("\nDatafile updated!\n")


while True:
    main_menu()
