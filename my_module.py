import random

import math

def i():
    for i in range(10):
        print(random.randint(25,35))


def elec():
    election = ["Trump", "Biden", "Kanye"]
    print(random.choice(election))



def n():
    for n in range(20):
        num = random.randint(0,100)
        if num % 2 == 1:
         print(num)
         break


def CalPyth():
    side1 = float(input("Please enter lenght of side 1: "))
    side2 = float(input("Please enter lenght of side 2: "))
    side3 = math.sqrt(side1 * side1 + side2 * side2)
    print("Third side length is :", side3)



    
                   





    



      


        
           
       
