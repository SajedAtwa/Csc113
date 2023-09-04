# question 1
import random
def randomizer(my_file,range_int):
    my_file = open("my_file.txt", "w")
    for i in range(0, range_int):
        print(random.randint(0, 1000), file=my_file)
    my_file.close()
def mean_of_numbers(my_file,range_int):
    my_file = open("my_file.txt", "r")
    sum_int = 0
    counter_int = 0
    for i in range(0, range_int):
       x_int = my_file.readline()
       if (x_int == " "):
           break
       sum_int += int(x_int)
       counter_int += 1
    my_file.close()
    y = sum_int/counter_int
    return(y)
filer = open("my_file.txt", "r")
filer.close()
range_int = random.randrange(10,100, 1)
randomizer(filer,range_int)
print(mean_of_numbers(filer,range_int))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# question 2
try:
  Months_file =open("Months.txt", "w+")
  for i in range(Months_file.seek(14)):
    z = Months_file.readline()
    s = z.split(" ")
    l = s[0]
    u = s[1]
    p = u.split("\n")
    n = float(p[0])
    r = round(n)
    o = str(r)
    h = l+" "+o
    print(h, file= Months_file)
  Months_file.close()
except:
  print("Months.txt does not exist")
#question 3
import random
def Fibanocci_triangle(Hi_file):
    Hi_file = open("triangle.txt", "w")
    n = random.radint(10, 30)

#question 4
a_int = 0
while (a_int == 0):
    try:
        n = input("enter an integer: ")
        d = list(n)
        sum = 0
        for i in d:
            w = int(i)
            sum += w
        print(sum)
    except:
        print("Invalid input please try again")

    start_stop = input("If you wish to continue type yes: ")
    if (start_stop == 'yes'):
        a_int = 0
    else:
        a_int = 1
#question 5
def string_trunctation_func(e):
    l = len(e)
    for i in range(l,0,-1):
        d = slice(i)
        print(e[d])
e = input("enter a word: ")
string_trunctation_func(e)

