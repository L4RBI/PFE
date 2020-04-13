from matplotlib.image import imread
import matplotlib.pyplot as plt 
from math import sqrt
import random




histogram = [0]*256
#reading the image
im = imread(".\jimmy.jpg")
#filling the histogram 
for i in im:
    for j in i:
        histogram[j]+=1
#printing the histogram
plt.plot( range(0,256) ,histogram)
plt.xlabel('grey intensity lvl')
plt.ylabel('frequency') 
plt.title('Histogram') 
plt.show()
#calculate the euclidian distance

def Dis(x1,y1,x2,y2):  
     dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
#declaration of variables
centers = []
m=2
eps=0.3
centers = [[8,histogram[8]+1] , [120,histogram[120]+1]]
U = [[0]*2 for i in range(257)]
#initialising the membership matrice randomly
for i in U:
    i[0]=random.random()
    i[1]=1-i[0]
#running FCM
for k in range(500):
    for i in range(len(centers)):
        x = 0 
        y = 0
        sumt = 0
        sumx = 0
        sumy = 0
        for j in range(256):
            sumx = sumx + (U[j][i]**m) * j
            sumy = sumy + (U[j][i]**m) * histogram[j]
            sumt = sumt + U[j][i]**m
        x= sumx/sumt
        y=sumy/sumt
        centers[i][0]=x
        centers[i][1]=y

    for i in range(256):
        for j in range(len(centers)):
            sumt=0
            for l in range(len(centers)):
                sumt = sumt + ((Dis(i,histogram[i],centers[j][0],centers[j][1])/Dis(i,histogram[i],centers[l][0],centers[l][1]))**(2/(m-1)))
            #sumt = sumt**(2/(m-1))
            U[i][j] = 1/sumt  
    print(centers)




#def PSO(numberOfClusters,m,constant1,constant2,weight,epsilon,numberMax,nErp,N):
    #random centers with random velocity
    #calculate the memebership
    #for i in range(numberMax):
        #for j in range (N):



