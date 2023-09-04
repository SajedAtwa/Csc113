class Answer(object):
    def SwapItems(self,L,Lm):

        for i in range(1, len(L)):
            if L[i] == L[-1]: #this tells the code to just input the last number and a zero when u reach the end of the list
                Lm.append(L[i])
                Lm.append(0)
            else:    #this will take the largest integer in the spliced list and attach it to the new list
                Lm.append(max(L[i:-1]))
Instance1 = Answer()
L = [18,19,6,5,7,2]
Lm = []
Instance1.SwapItems(L,Lm) #calling the method to start swapping the lists.
print(Lm)

