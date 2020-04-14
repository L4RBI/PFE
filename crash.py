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