string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
counter = 0

list1 = list(string1) #This will turn each of the strings into a list
list2 = list(string2)
l = len(list2) #this will take the sizes of the list/string and store it for comparision
w = len(list1)

if l > w:  #What to do if the second string/list is bigger
    d = l - w
    m = 0
    while m != d:
        list1.append("0")
        m += 1
    for i in range(l):
      t = list1[i]
      f = list2[i]
      if t != f:
        list1[i] = list2[i]
        counter += 1
elif w > l: #What to do when the first string/list is larger
    p = w - l
    q = 0
    while q != p:#This will append a zero string to the shorter string/list so that both lists will become the same size
        list2.append("0")
        q += 1
    for j in range(w):
        t = list1[j]
        f = list2[j]
        if t != f:
            list1[j] = list2[j]
            counter += 1
else: #what to do when the strings are the same size
  for k in range(l): #This will go through each characters of each string and check if they match.
      t = list1[k]
      f = list2[k]
      if t != f: #If they dont match then the character of the first string will be changed to match the second string
        list1[k] = list2[k]
        counter += 1 #Each time a character is changed the counter will go up by 1

print(counter)







