language_data = { 'French' : ('Le monde de la réalité a ses limites; le monde de l\'imagination est sans frontières '
                                                  'L\’avenir est entre les mains de ceux qui explorent '
                                                  'Le monde est un livre dont chaque pas nous ouvre une page une page '
                                                  'Dans la vie on ne fait pas ce que l\’on veut mais on est responsable de ce que l\’on est '),
                  
                                  'English' : ('This above all to thine own self be true '
                                                  'Did my heart love till now? Forswear it, sight! For I never saw true beauty till this night '
                                                  'Another page of this missing book called the happiest moment of life'),
                  
                                  'German' : ('Ein jeder kehr’ vor seiner Tür, und rein ist jedes Stadtquartier'
                                                  'Zwei Dinge sind unendlich, das Universum und die menschliche Dummheit, '
                                                  'aber bei dem Universum bin ich mir noch nicht ganz sicher'
                                                  'Was mich nicht umbringt, macht mich stärker'),
                                }


##insert your code here


string1 = input("please enter a string: ")  #This will turn a user inputted string into a lowercase string
string12 = string1.lower()
d = language_data['French']
e = language_data['English']
a = language_data['German']
l1 = d.lower() #this will take all the strings from the dictionary and turn it lowercase
l2 = e.lower()
l3 = a.lower()
if string12 in l1: #this will check if the inputted string is a substring of the strings in the dictionary
  print("French")
elif string12 in l2:
  print("English")
elif string12 in l3:
  print("German")
else:  #will print out "No Matching languages" if the inputted string isnt a substring of the dictionaies strings
    print("No Matching Languages")
