import math
import random
import sys

A1 = [0, 0, 1, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 1, 1, 1]

B1 = [1, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C1 = [0, 0, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 0, 1, 1, 1, 1, 0]

D1 = [1, 1, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 1, 1, 0, 0]

E1 = [1, 1, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 1, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 1]

J1 = [0, 0, 0, 1, 1, 1, 1, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K1 = [1, 1, 1, 0, 0, 1, 1, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 0, 1, 1]

A2 = [0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0]

B2 = [1, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C2 = [0, 0, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

D2 = [1, 1, 1, 1, 1, 0, 0, 
      1, 0, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 1, 0, 
      1, 1, 1, 1, 1, 0, 0]

E2 = [1, 1, 1, 1, 1, 1, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 1, 1, 1, 1, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 1, 1, 1, 1, 1, 1]

J2 = [0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K2 = [1, 0, 0, 0, 0, 1, 0, 
      1, 0, 0, 0, 1, 0, 0, 
      1, 0, 0, 1, 0, 0, 0, 
      1, 0, 1, 0, 0, 0, 0, 
      1, 1, 0, 0, 0, 0, 0, 
      1, 0, 1, 0, 0, 0, 0, 
      1, 0, 0, 1, 0, 0, 0, 
      1, 0, 0, 0, 1, 0, 0, 
      1, 0, 0, 0, 0, 1, 0]

A3 = [0, 0, 0, 1, 0, 0, 0, 
      0, 0, 0, 1, 0, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 0, 1, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 1, 1, 1, 1, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 1, 0, 0, 0, 1, 1]

B3 = [1, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 1, 1, 1, 1, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 0]

C3 = [0, 0, 1, 1, 1, 0, 1, 
      0, 1, 0, 0, 0, 1, 1, 
      1, 0, 0, 0, 0, 0, 1, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 0, 
      1, 0, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

D3 = [1, 1, 1, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      1, 1, 1, 1, 0, 0, 0]

E3 = [1, 1, 1, 1, 1, 1, 1, 
      0, 1, 0, 0, 0, 0, 1, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 1, 1, 1, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 0, 
      0, 1, 0, 0, 0, 0, 1, 
      1, 1, 1, 1, 1, 1, 1]

J3 = [0, 0, 0, 0, 1, 1, 1, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 0, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 0, 1, 1, 1, 0, 0]

K3 = [1, 1, 1, 0, 0, 1, 1, 
      0, 1, 0, 0, 0, 1, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 1, 0, 0, 0, 0, 
      0, 1, 0, 1, 0, 0, 0, 
      0, 1, 0, 0, 1, 0, 0, 
      0, 1, 0, 0, 0, 1, 0, 
      1, 1, 1, 0, 0, 1, 1]

NAMES = ["A1", "B1", "C1", "D1", "E1", "J1", "K1", "A2", "B2", "C2", "D2", "E2", "J2", "K2", "A3", "B3", "C3", "D3", "E3", "J3", "K3"]

MAX_CLUSTERS = 25
INPUT_PATTERNS = 21
VEC_LEN = 63
VEC_XLEN = 5
VEC_YLEN = 5
DECAY_RATE = 0.96 # About 100 iterations.
MIN_ALPHA = 0.01
RADIUS_REDUCTION_POINT = 0.023 # Last 20% of iterations.

class SOM_Class3:
    def __init__(self, vectorLength, maxClusters, numPatterns, xLength, yLength, minimumAlpha, decayRate, reductionPoint, patternArray, namesArray):
        self.mVectorLen = vectorLength
        self.mMaxClusters = maxClusters
        self.mNumPatterns = numPatterns
        self.mXLength = xLength
        self.mYLength = yLength
        self.mMinAlpha = minimumAlpha
        self.mDecayRate = decayRate
        self.mReductionPoint = reductionPoint
        self.mAlpha = 0.6
        self.d = []
        self.w = []
        self.mPatterns = patternArray
        self.mNames = namesArray
        return

    def initialize_arrays(self):
        # create 2D array of random values between 0.0 and 1.0.
        for i in range(self.mMaxClusters):
            newArray = []
            for j in range(self.mVectorLen):
                newArray.append(random.random())

            self.w.append(newArray)

        return
    
    def compute_input(self, vectorArray):
        self.d = [0.0] * self.mMaxClusters
        
        for i in range(self.mMaxClusters):
            for j in range(self.mVectorLen):
                self.d[i] += math.pow((self.w[i][j] - vectorArray[j]), 2)
        
        return
    
    def get_minimum(self, nodeArray):
        minimum = 0
        foundNewMinimum = False
        done = False
    
        while not done:
            foundNewMinimum = False
            for i in range(self.mMaxClusters):
                if i != minimum:
                    if nodeArray[i] < nodeArray[minimum]:
                        minimum = i
                        foundNewMinimum = True
    
            if foundNewMinimum == False:
                done = True
    
        return minimum
    
    def update_weights(self, vectorNumber, dMin):
        y = 0
        pointA = 0
        pointB = 0
        done = False
        
        for i in range(self.mVectorLen):
            # Only include neighbors before radius reduction point is reached.
            if self.mAlpha > self.mReductionPoint:
                y = 1
                while not done:
                    if y == 1: # Top row of 3
                        if dMin > self.mXLength - 1:
                            pointA = dMin - self.mXLength - 1
                            pointB = dMin - self.mXLength + 1
                        else:
                            y = 2
                    
                    if y == 2: # Middle row of 3.
                        PointA = dMin - 1
                        # DMin is like an anchor position right between these two.
                        PointB = dMin + 1
                    
                    if y == 3: # Bottom row of 3.
                        if dMin < (self.mXLength * (self.mYLength - 1)):
                            pointA = dMin + self.mXLength - 1
                            pointB = dMin + self.mXLength + 1
                        else:
                            done = True
                    
                    if not done:
                        for j in range(pointA, pointB):
                            # Check if anchor is at left side.
                            if math.fmod(dMin, self.mXLength) == 0:
                                # Check if anchor is at top.
                                if j > pointA:
                                    self.w[j][i] = self.w[j][i] + (self.mAlpha * (self.mPatterns[vectorNumber][i] - self.w[j][i]))
                            
                            # Check if anchor is at right side.
                            elif math.fmod((dMin + 1), self.mXLength) == 0:
                                # Check if anchor is at top.
                                if j < pointB:
                                    self.w[j][i] = self.w[j][i] + (self.mAlpha * (self.mPatterns[vectorNumber][i] - self.w[j][i]))
                            
                            # Otherwise, anchor is not at either side.
                            else:
                                self.w[j][i] = self.w[j][i] + (self.mAlpha * (self.mPatterns[vectorNumber][i] - self.w[j][i]))
                    
                    if y == 3:
                        done = True
                    
                    y += 1
            
            elif self.mAlpha <= self.mReductionPoint:
                # Update only the winner.
                self.w[dMin][i] = self.w[dMin][i] + (self.mAlpha * (self.mPatterns[vectorNumber][i] - self.w[dMin][i]))
        
        return

    def training(self):
        iterations = 0
        reductionFlag = False
        reductionPoint = 0
        
        while self.mAlpha > self.mMinAlpha:
            iterations += 1
            sys.stdout.write("Training iteration: " + str(iterations) + "\n")
            
            for i in range(self.mNumPatterns):
                self.compute_input(self.mPatterns[i])
                
                dMin = self.get_minimum(self.d)
                
                self.update_weights(i, dMin)
            
            # Reduce the learning rate.
            self.mAlpha = self.mDecayRate * self.mAlpha
            
            # Reduce radius at specified point.
            if self.mAlpha < self.mReductionPoint:
                if reductionFlag == False:
                    reductionFlag = True
                    reductionPoint = iterations
        
        sys.stdout.write("Iterations: " + str(iterations) + "\n")
        
        sys.stdout.write("Neighborhood radius reduced after " + str(reductionPoint) + " iterations.\n")
        
        return
    
    def print_results(self):
        sys.stdout.write("Clusters for training input:\n")
        
        for i in range(self.mNumPatterns):
            self.compute_input(self.mPatterns[i])
            
            dMin = self.get_minimum(self.d)
            
            sys.stdout.write("Vector (")
            sys.stdout.write("Pattern " + str(i) + ", " + self.mNames[i])
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        return


if __name__ == '__main__':
    pattern = []
    pattern.append(A1)
    pattern.append(B1)
    pattern.append(C1)
    pattern.append(D1)
    pattern.append(E1)
    pattern.append(J1)
    pattern.append(K1)
    pattern.append(A2)
    pattern.append(B2)
    pattern.append(C2)
    pattern.append(D2)
    pattern.append(E2)
    pattern.append(J2)
    pattern.append(K2)
    pattern.append(A3)
    pattern.append(B3)
    pattern.append(C3)
    pattern.append(D3)
    pattern.append(E3)
    pattern.append(J3)
    pattern.append(K3)

    som = SOM_Class3(VEC_LEN, MAX_CLUSTERS, INPUT_PATTERNS, VEC_XLEN, VEC_YLEN, MIN_ALPHA, DECAY_RATE, RADIUS_REDUCTION_POINT, pattern, NAMES)
    som.initialize_arrays()
    som.training()
    som.print_results()
    
