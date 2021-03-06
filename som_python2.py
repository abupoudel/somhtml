import math
import sys

MAX_CLUSTERS = 3
VECTORS = 4
VEC_LEN = 8
DECAY_RATE = 0.96
MIN_ALPHA = 0.01

training_patterns = [[1, 1, 0, 0],
                     [0, 0, 0, 1],
                     [1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [1, 0, 1, 0],
                     [0, 0, 0, 0],
                     [1, 0, 0, 0],
                     [0, 1, 1, 1]]

tests = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [1, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 0, 0, 1],
         [1, 1, 1, 0],
         [0, 1, 1, 1],
         [0, 1, 0, 1],]

class SOM_Class1:
    def __init__(self, numVectors, maxClusters, alphaStart, minimumAlpha, decayRate, vectorLength):
        self.mVectors = numVectors
        self.mVecLen = vectorLength
        self.mAlpha = alphaStart
        self.minAlpha = minimumAlpha
        self.decayRate = decayRate
        self.mIterations = 0
        self.maxClusters = maxClusters
        self.mD = [[]] * maxClusters
        self.w = [[0.2, 0.6, 0.5, 0.9],
                  [0.8, 0.4, 0.7, 0.3],
                  [0.1, 0.2, 0.1, 0.2]]
    
    def compute_input(self, vectorNumber, trainingTests):
        self.mD[0] = 0.0
        self.mD[1] = 0.0
        self.mD[2] = 0.0
        
        for i in range(self.maxClusters):
            for j in range(self.mVectors):
                self.mD[i] += math.pow((self.w[i][j] - trainingTests[vectorNumber][j]), 2)
        
        return
    
    def train(self, patterns, trainingTests):
        self.mIterations = 0
        
        while self.mAlpha > self.minAlpha:
            self.mIterations += 1
            for i in range(self.mVectors):
                self.compute_input(i, trainingTests)
                
            # See which is smaller, mD(0) or mD(1)?
            dMin = 0 if self.mD[0] < self.mD[1] else 1
            dMin = dMin if self.mD[2] < dMin else 2
			
            # Update the weights on the winning unit.
            for j in range(self.mVectors):
                self.w[dMin][j] = self.w[dMin][j] + (self.mAlpha * (patterns[i][j] - self.w[dMin][j]))
            
            # Reduce the learning rate.
            self.mAlpha = self.decayRate * self.mAlpha
        
        return
    
    def test(self, patterns, trainingTests):
        # Print clusters created.
        sys.stdout.write("Clusters for training input:\n")
        
        for i in range(self.mVectors):
            self.compute_input(i, trainingTests)
            
            dMin = 1 if self.mD[0] > self.mD[1] else 0
            
            sys.stdout.write("\nVector ( ")
            
            for j in range(self.mVectors):
                sys.stdout.write(str(patterns[i][j]) + ", ")
            
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        # Print weight matrix.
        sys.stdout.write("\n")
        for i in range(self.maxClusters):
            sys.stdout.write("Weights for Node " + str(i) + " connections:\n")
            
            for j in range(self.mVecLen):
                sys.stdout.write("{:03.3f}".format(self.w[i][j]) + ", ")
            
            sys.stdout.write("\n\n")
        
        # Print post-training tests.
        sys.stdout.write("Categorized test input:\n")
        for i in range(self.mVectors):
            self.compute_input(i, trainingTests)
            
            dMin = 0 if self.mD[0] < self.mD[1] else 1
            dMin = dMin if self.mD[2] < dMin else 2
            
            sys.stdout.write("\nVector ( ")
            
            for j in range(self.mVectors):
                sys.stdout.write(str(trainingTests[i][j]) + ", ")
            
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        return
    
    def get_iterations(self):
        return self.mIterations

if __name__ == '__main__':
    Alpha = 0.6
    som = SOM_Class1(VECTORS, MAX_CLUSTERS, Alpha, MIN_ALPHA, DECAY_RATE, VEC_LEN)
    som.train(training_patterns, tests)
    som.test(training_patterns, tests)
    
    sys.stdout.write("\nIterations: " + str(som.get_iterations()) + "\n")
    
    
