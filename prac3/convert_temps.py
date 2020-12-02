Temps = input("please enter the temperature value with sign")
if Temps[-1] in ['F','f']:
    C = (eval(Temps[0:-1])-32)/1.8
    print("The converted temperature value is{:.2f}C".format(C))
elif Temps[-1] in ['C','c']:
    F = 1.8*eval(Temps[0:-1])+32
    print("The converted temperature value is{:.2f}F".format(F))
else:
    print("Invalid number")