import numpy as np

class recogDB:
	
	def __init__(self):
		self.k = 4096
		
		self.F_bar = np.array([])
		self.F = {}
		self.weight = {}
		self.name = {}					# index to name

		self.name_inv = {}			# name to index
		self.maxreps = 3 
		self.num_people = 0
		self.threshold = 0.4

		self.score_imp = 1
		self.confidence_imp = 3

	def predict(self, F_, score=1):
		
		F_hat = np.dot(F_.T, self.F_bar)

		index = np.argmax(F_hat)
		
		if(F_hat[index] > self.threshold):
			return self.name[index]
			self.add_to_DB(F_hat, self.name[index], score=score, confidence=F_hat[index])
		else:
			return None

	def add_to_DB(self, F, name, score=1, confidence=1) :
		if name not in self.name.values() : # New Element
			index = self.num_people
			self.name[index] = name
			self.name_inv[name] = index
			self.F[index] = [F]
			self.weight[index] = score*score_imp + confidence*confidence_imp
			self.num_people += 1
		else :
			index = self.name_inv[name]
			self.F[index] = [F] + self.F[index][0:(self.maxreps-1)]			## Weight Based

		T = np.zeros(self.K)
		for j in range(self.confidence[i]) :
			T += self.weight[i][j]*F[j]
		self.F_bar[i,:] = T / np.linalg.norm(T)


