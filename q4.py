AliceMeetings = [['08:00','09:30'],['09:30','11:00'],['13:00','14:00'],['15:00','16:30']]
AliceWorkHours = ['07:00','19:00']

BobMeetings = [['09:00','10:30'],['11:00','12:00'],['13:00','14:30'],['15:30','17:00']]
BobWorkHours = ['07:00','18:00']
def Availablilites(): #Got these values by get the time in between each of the endpoints in the meeting hours and capped it off by time for the workhours
  AliceAvail = [[], [], [], []]
  AliceAvail[0].append(Alicelist2[0])
  AliceAvail[0].append(Alicelist[0])
  AliceAvail[1].append(Alicelist[3])
  AliceAvail[1].append(Alicelist[4])
  AliceAvail[2].append(Alicelist[5])
  AliceAvail[2].append(Alicelist[6])
  AliceAvail[3].append(Alicelist[7])
  AliceAvail[3].append(Alicelist2[-1])
  BobAvail = [[], [], [], [], []]
  BobAvail[0].append(Boblist2[0])
  BobAvail[0].append(Boblist[0])
  BobAvail[1].append(Boblist[1])
  BobAvail[1].append(Boblist[2])
  BobAvail[2].append(Boblist[3])
  BobAvail[2].append(Boblist[4])
  BobAvail[3].append(Boblist[5])
  BobAvail[3].append(Boblist[6])
  BobAvail[4].append(Boblist[7])
  BobAvail[4].append(Boblist2[-1])
  return(AliceAvail,BobAvail)
def MeetingSchedule():  #Compared values recieved from AliceAvail and BobAvail to get these values
  BobandAliceMeetings = [[], [], [], []]
  BobandAliceMeetings[0].append('07:00')
  BobandAliceMeetings[0].append('08:00')
  BobandAliceMeetings[1].append('12:00')
  BobandAliceMeetings[1].append('13:00')
  BobandAliceMeetings[2].append('14:30')
  BobandAliceMeetings[2].append('15:00')
  BobandAliceMeetings[3].append('17:00')
  BobandAliceMeetings[3].append('18:00')
  return(BobandAliceMeetings)

Alicelist = []
Boblist = []
Alicelist2 = []
Boblist2 = []
AliceAvail = []
for i in range(len(AliceMeetings)):    #This was to turn all the values to integers and put them in single list so they would be easier to compare
  for j in range(len(AliceMeetings[i])):
    Alicelist.append(int(AliceMeetings[i][j].replace(':',"")))

for a in range(len(AliceWorkHours)):
  r = AliceWorkHours[a]
  Alicelist2.append(int(r.replace(':',"")))

for k in range(len(BobMeetings)):
    for h in range(len(BobMeetings[k])):
      Boblist.append(int(BobMeetings[k][h].replace(':',"")))
for b in range(len(BobWorkHours)):
  e = BobWorkHours[b]
  Boblist2.append(int(e.replace(':',"")))


m = Availablilites()
print(m)
d = MeetingSchedule()
print(d)