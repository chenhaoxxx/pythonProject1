"""
Replace the contents of this module docstring with your own details
Name:Haoxian Chen
Date started:11/12/2020
GitHub URL:https://github.com/chenhaoxxx/pythonProject1/tree/master/HaoxianChen
"""
from typing import List

"""5 movies loaded"""


list_of_moive = open('movies.csv', 'r')
FILE = list_of_moive.readlines()
Remainder = [1]
TOTAL_PLACES = [0]


"""Define main, print system information and boot menu"""
def main():
    print("Movies To Watch 1.0 - by HaoxianChen")
    print("5 movies loaded")
    menu()

"""Define, design the menu and exit the program"""
def menu():
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("W - - Watch a movie")
    print("Q - Quit")
    menu = input(">>>").upper()
    while menu not in ["L","A","W","Q"]:
        menu = input("Invalid menu choice").upper()

    if menu == "L":
        List()

    if menu == "A":
        Adding_place()

    if menu == "W":
        Mark_function()


    else:
        confirm = input("Do you want to quit this program? -Yes, No ").upper()
        while confirm not in ["Y", "N"]:
            confirm = input("Invalid, please re-enter your option: Y or N").upper()
        if confirm == "Y":
            with open('movies.csv', 'w') as list_of_moive:
                for item in FILE:
                    list_of_moive.write("{}".format(item))
            print("6 movies saved to movies.csv")
            print(" Have a nice day:) ")
            quit()
        else:
            menu()


def List():
    visited = 0
    unvisited = 0
    list = []
    for lines in FILE:
        visited += 1
        line = lines.split(',')
        input_name = line[0]
        input_places = line[1]
        priority = line[2]
        visit = line[3].replace("l", "*").replace("u", "").replace("\n", "")
        list.append(visited)
        display = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(visited,visit, input_name, input_places,priority))
        print(display)

        if "*" in visit:
            unvisited += 1
    print("-" * 100)
    print(max(list))
    visited_need = (max(list) - unvisited)
    Remainder.append(visited_need)
    print("You still want to visit", max(list) - unvisited, "places")
    TOTAL_PLACES.append(max(list))
    print("-" * 100)
    menu()


def Adding_place():

    name = input("Title:")
    while name == "":
        print("Input can not be blank")
        name = input("Title:")
    input_Category = input("Category:")
    while input_Category == "":
        print("Input can not be blank ")
        input_Category == input("Category:")

    test = True
    while test == True:
        try:
            input_year = int(input("Year:"))
            test = False
        except ValueError:

            print("Invalid input; enter a valid number")
    while input_year < 0:
        print("Number must be > 0")
        test = True
        while test == True:
            try:
                input_year = int(input("Year:"))
                test = False
            except ValueError:
                print("Invalid input; enter a valid number")

    if Remainder[-1] ==0:
        Remainder.remove(Remainder[-1])
        final_result = ("{},{},{},".format(name,input_Category,input_year))
        FILE.append(final_result)
        print("{} in {} from ({}) added to movie list".format(name, input_Category, input_year))
        return
    menu()

def Mark_function():
    visit_status = "l\n"
    if min(Remainder) == 0:
        print("No more places to watch")
        menu()

    test  =True
    while test == True:
        try:
            number = int(input("Enter the number of a place to be marked as watched: "))
            test = False
        except ValueError:
            print("Invalid input, please enter a number again")
    if max(TOTAL_PLACES)==0:
        print("please choose L in the maim menu")
        menu()
    while number > max(TOTAL_PLACES):
        print("Input the value!")
        number = int(input("Enter the number of a place to be marked as watched: "))
    while number <= 0:
        print("Input the value!")
        number = int(input("Enter the number of a place to be marked as watched: "))


    rows = FILE[number - 1]
    new_list = rows.split(",")
    place_name = new_list[0]
    country_name = new_list[1]
    priority = new_list[2]
    result = ("{},{},{},{}".format(place_name,country_name,priority, visit_status))
    result_2 = ("5 movies watched, 1 movies still to watch")
    FILE.append(result)
    FILE.remove(FILE[number - 1])
    print(result_2)
    print('-'*100)
    menu()





if __name__ == '__main__':
    main()
