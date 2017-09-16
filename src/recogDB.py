import numpy as np
class recogDB:
	def __init__(self):
		self.k = 4096
		self.F = []
		self.maxreps = 3 
		self.threshold = 0.5
	def predict(self,Fcap):
		for i in xrange(len(self.F)):
			if(i==0):
				Fbar = np.zeros(self.F[0].shape)
			Fbar = np.sum(Fbar,(2**(self.maxreps-i-1))*F[i])
		Fbarnorm = Fbar / np.linalg.norm(Fbar,axis=0)[:,None]
		Fpredict = np.dot(Fcap.T,Fbarnorm)
		ind = np.argmax(Fpredict)
		if(Fpredict[ind]>self.threshold):
			print("We have a matching")
		else:
			print("We don't have a matching")

	# def addingfeature(Fcap):
	# 	for i in xrange(len(self.F)):
	# 		if(i<Fcap.shape[1])
	# 			np.concatenate((F[i],Fcap[:,i]),axis=1)
	# 		else:
	# 			np.concatenate((F[i],np.zeros((F[i].shape[0],1))),axis=1)