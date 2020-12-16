STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print("{} is {}" .format(state, STATE_NAMES[state]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()