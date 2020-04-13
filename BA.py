import random
from math import sqrt
import math 

def Dis(x1,y1,x2,y2):  
     dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist 
def objective(x1,x2):
    return 0

MaxIterations=500
NumberOfBats = 5
Fmin = 0
Fmax = 100
fitness = [0] * NumberOfBats
Best = [0] * 2
Bats = [[0]*6 for i in range(NumberOfBats)]
R = [0] * NumberOfBats
j=0
SumA=0
Alpha = 0.9
Gamma = 0.9 
#initializing the bat population
for i in Bats:
    #x
    i[0]=random.random()*255
    #y
    i[1]=random.random()*255
    #f
    i[2]=random.random()*100
    #v
    i[3]=random.random()*50
    #r
    i[4]=random.random()
    #A
    i[5]=random.random()
    #calculating fitness
    fitness[j] = objective(i[0],i[1])
    #sum of loudness
    SumA = SumA + i[5]
    #saving the initial R
    R[j] = i[4] 
    j = j + 1
#calculating the average loudness    
A = SumA / NumberOfBats 

#getting the global best
for f in range(NumberOfBats):
    if( max(fitness) == fitness[f]):
        Best[0] = Bats[f][0]
        Best[1] = Bats[f][1]

for t in range(MaxIterations):
    SumA = 0
    j=0
    for i in Bats:
        i[2] = Fmin + (Fmax-Fmin) * random.random()
        i[3] = i[3] + Dis( i[0] , i[1] , Best[0] , Best[1] ) * i[2]
        i[0] = i[0] + i[3]
        i[1] = i[1] + i[3]
        if(random.random()>i[4]):
            i[0] = Best[0] + random.random() * A
            i[1] = Best[1] + random.random() * A
        i[0] = i[0] + random.random() * A
        i[1] = i[1] + random.random() * A    
        if( random.random() < i[5] and objective(i[0],i[1]) < objective(Best[0],Best[1]) ):
            #updating the best
            Best[0]=i[0]
            Best[1]=i[1]
            #decreasing the loudness
            i[5] = Alpha * i[5]
            #increasing the rate
            i[4] =  R[i] * ( 1 - math.exp( -Gamma * t) )
        fitness[j] = objective( i[0] , i[1] )
        SumA = SumA + i[5]
        j =+1
    #to be a fonction
    for f in range(NumberOfBats):
        if( max(fitness) == fitness[f]):
            Best[0] = Bats[f][0]
            Best[1] = Bats[f][1]
    A = SumA / NumberOfBats    
