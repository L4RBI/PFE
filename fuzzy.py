from fcmeans import FCM
from matplotlib.image import imread
import matplotlib.pyplot as plt 
from math import sqrt
import random
import numpy as np
from scipy.spatial.distance import cdist
from scipy.linalg import norm

class Cluster:
    def __init__(self):
      pass  

    def Histogram(self,path):
        histogram = [0]*256
        image = np.array(imread( path ))
        for i in range(256):
            histogram[i]+=np.count_nonzero(image == i)
        return np.array(histogram)

    def ShowHistogram(self,histogram):
        plt.plot( range(0,256) ,histogram)
        plt.xlabel('Grey intensity lvl')
        plt.ylabel('Frequency') 
        plt.title('Histogram') 
        plt.show()

    def adapt(self,histogram):
        adapted_histogram = np.zeros((256,2))
        for i in range(256):
            adapted_histogram[i][0]=i
            adapted_histogram[i][1]=histogram[i]
        return adapted_histogram


    def Fcm(self,histogram):
        adapted_histogram = self.adapt(histogram)
        fcm = FCM(n_clusters=3)
        fcm.fit(adapted_histogram)
        return fcm


"""    def FuzzyCMeans(self, n_clusters, initial_centers , histogram , max_iter=250, m=2, error=1e-5 ):
        assert m > 1
        assert initial_centers.shape[0] == n_clusters
        self.U = None
        self.centers = initial_centers
        self.max_iter = max_iter
        self.m = m
        self.error = error

        def membership(self, histogram, centers):
            U_temp = cdist( histogram , centers , 'euclidean')
            U_temp = np.power(U_temp,2/(m-1))
            denominator_ = U_temp.reshape((histogram.shape[0], 1, -1)).repeat(U_temp.shape[-1], axis=1)
            denominator_ = U_temp[:, :, np.newaxis] / denominator_
            return 1 / denominator_.sum(2)

        def Centers(self,histogram,U):
            um = self.u ** self.m
            return (histogram.T @ um / np.sum(um, axis=0)).T
        
        self.U = membership( histogram , super.centers)

        past_U = np.copy(self.U)

        for i in range(max_iter):

            self.centers = Centers( self , histogram , self.U)
            self.U = membership( histogram , self.centers)

            if norm(self.U - past_U) < self.error:
                break
            past_U = np.copy(self.U)
            
        return self.centers """

        
class FuzzyCMeans:
        def __init__(self, n_clusters, initial_centers , histogram , max_iter=250, m=2, error=1e-5 ):
            assert m > 1
            assert initial_centers.shape[0] == n_clusters
            self.U = None
            self.centers = initial_centers
            self.max_iter = max_iter
            self.m = m
            self.error = error
            self.histogram=histogram

        def membership(self, histogram, centers):
            U_temp = cdist( histogram , centers , 'euclidean')
            U_temp = np.power(U_temp,2/(self.m - 1))
            denominator_ = U_temp.reshape((histogram.shape[0], 1, -1)).repeat(U_temp.shape[-1], axis=1)
            denominator_ = U_temp[:, :, np.newaxis] / denominator_
            return 1 / denominator_.sum(2)

        def Centers(self,histogram,U):
            um = U ** self.m
            return (histogram.T @ um / np.sum(um, axis=0)).T


        def compute(self):
            self.U = self.membership( self.histogram , self.centers)

            past_U = np.copy(self.U)

            for i in range(self.max_iter):

                self.centers = self.Centers( self.histogram , self.U)
                self.U = self.membership( self.histogram , self.centers)

                if norm(self.U - past_U) < self.error:
                    break
                past_U = np.copy(self.U)
                
            return self.centers 

F = Cluster()
fcm=F.Fcm(F.Histogram(".\Images\Images\T01.JPG"),)
Initial_centers= np.array([[ 4,13 ],[ 100,550 ],[250,160]])
f=FuzzyCMeans(n_clusters = 3, initial_centers=Initial_centers, histogram= F.adapt(F.Histogram(".\Images\Images\T01.JPG")))
print(f.compute(),"fc")
print("break")
print(fcm.centers ,"fcm")