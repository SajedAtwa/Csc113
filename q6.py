string1 = input("Enter in some numbers(,in between): ")
tuple1 = tuple(float(i) for i in string1.split(",")) #This will take user input and turn it to a tuple
t = 'false'
if len(tuple1) < 3:
    t = "false"

for j in range(len(tuple1)):  #This will go through the tuple by bruteforce method and check if there is a combination in which the expression is true
    for k in range(len(tuple1)):
        for h in range(len(tuple1)):
            if (tuple1[j] ** 2 == (tuple1[k]) ** 2 + (tuple1[h]) ** 2):
                t = "true"

if t == "true": #will print true if a combination in which the expression is true will be found
    print(True)
else:
    print(False)
