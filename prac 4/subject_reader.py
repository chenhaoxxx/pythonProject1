"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    big=[]
    for i in input_file:
        i = i.strip()
        parts = i.split(',')
        parts[2] = int(parts[2])
        big.append(parts)
    input_file.close()

    return big

def display(big):
    for list in big:
        print("{0} is taught by {1} and has {2} students".format(list[0],list[1],list[2]))


main()



        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        #line = line.strip()  # Remove the \n
       # parts = line.split(',')  # Separate the data into its parts
       # print(parts)  # See what the parts look like (notice the integer is a string)
        #parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        #print("----------")



