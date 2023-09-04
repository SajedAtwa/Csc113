#question 1
def matri_sub(matrix_A, matrix_B):
  for element1 in range(len(matrix_A)):
    for element2 in range(len(matrix_A[element1])):
      print (matrix_A[element1][element2] - matrix_B[element1][element2])
matrix_A = [[2,3,4],
           [4,5,6],
           [6,7,8]]
matrix_B = [[1,2,3],
           [4,5,6],
           [7,8,9]]
matri_sub(matrix_A, matrix_B)

#question 2
asc_dictionary = {}
for i in range(65,127):
    d = chr(i)
    asc_dictionary[i] =d
print(asc_dictionary)

#question 3
class RaceCar(object):
    def __init__(self,type='',acceleration_value='',top_speed='',nitro='',color='', year='', number_of_doors='', speed = 0):
        self.type = type
        self.acceleration_value = acceleration_value
        self.top_speed = top_speed
        self.nitro = nitro
        self.color = color
        self.year = year
        self.number_of_doors = number_of_doors
        self.speed = speed
    def carinfo(self):
       print("""
       car information:
       
       car type: {}
       
       Acceleration Value: {}
       
       Top Speed: {}
       
       Nitro: {}
       
       Color: {}
       
       Year: {}
       
       Number Of Doors: {}
       
       Speed: {}
       """.format(self.type, self.acceleration_value, self.top_speed, self.nitro, self.color, self.year, self.number_of_doors, self.speed))
    def Accelerate(self):
        if self.speed + 10 <= self.top_speed:
            self.speed += 10
        else:
            d = self.top_speed - self.speed
            self.speed += d
    def Breaks(self):
        if self.speed - 10 >= 0:
            self.speed -= 10
        else:
            self.speed -= self.speed
    def turn_left(self):
        print("Turning Left")
    def turn_right(self):
        print("Turning Right")
    def reverse(self):
        print("Going in Reverse")
RaceCar1 = RaceCar('hyper',1720.5,8532.78,3689.64,'green',2003,4,300)
RaceCar1.Accelerate()
RaceCar1.Accelerate()
RaceCar1.Breaks()
RaceCar1.carinfo()
RaceCar1.turn_left()
RaceCar1.turn_right()
RaceCar1.reverse()