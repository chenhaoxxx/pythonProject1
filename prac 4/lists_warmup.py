numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0]#output 3
print(numbers[0])

numbers[-1]# output 2
print(numbers[-1])

numbers[3] #output 1
print(numbers[3])
numbers[:-1] # output 3,1,4,1,5,9
print(numbers[:-1])
numbers[3:4] #output 1
print(numbers[3:4])

5 in numbers # output True
print(5 in numbers)
7 in numbers # output False
print(7 in numbers)
"3" in numbers # output False
print("3" in numbers)
numbers + [6, 5, 3] #output [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers + [6, 5, 3])

numbers[0]="ten"
print(numbers)

numbers[-1]=1
print(numbers)

del numbers[0:2]
print(numbers)

print(9 in numbers)