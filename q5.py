Str = "Johnson,1234,3.26,Ronald" #this will take a string turn it into a list
list1 = Str.split(",")
StrOutput = list1[1] + " " + list1[-1] + " " + list1[0]  #this will combine the needed components from the list into a string to be outputted
print(StrOutput)