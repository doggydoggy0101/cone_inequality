import numpy as np

def inCone(vector, theta):
    if vector[0] + 1e-10 >= np.linalg.norm(vector[1:])*(1/np.tan(theta)):
        return True
    else:
        return False

class mean:
    def __init__(self, vector1, vector2, theta):
        self.vec1 = vector1
        self.vec2 = vector2
        self.theta = theta

        self.A =  self.A_mean()
        self.H =  self.H_mean()
        self.max = self.max_mean()
        self.min = self.min_mean()

    def spec_inv(self, vec):
        ''' spectral decomposition inverse '''
        norm = np.linalg.norm(vec[1:])
        lambda_1 = 1/(vec[0] - norm*(1/np.tan(self.theta)))
        lambda_2 = 1/(vec[0] + norm*np.tan(self.theta))
        x_1 = lambda_1*np.sin(self.theta)**2+lambda_2*np.cos(self.theta)**2
        if norm == 0:
            w = np.zeros(len(vec[1:]))
            w[0] = 1
            x_2 = (lambda_2-lambda_1)*(np.sin(self.theta)*np.cos(self.theta))*w
        else:
            x_2 = (lambda_2-lambda_1)*(np.sin(self.theta)*np.cos(self.theta))*(vec[1:]/norm)
        return np.insert(x_2, 0, x_1, axis=0)

    def spec_abs(self, vec):
        ''' spectral decomposition absolute '''
        norm = np.linalg.norm(vec[1:])
        lambda_1 = np.abs(vec[0] - norm*(1/np.tan(self.theta)))
        lambda_2 = np.abs(vec[0] + norm*np.tan(self.theta))
        x_1 = lambda_1*np.sin(self.theta)**2+lambda_2*np.cos(self.theta)**2
        if norm == 0:
            w = np.zeros(len(vec[1:]))
            w[0] = 1
            x_2 = (lambda_2-lambda_1)*(np.sin(self.theta)*np.cos(self.theta))*w
        else:
            x_2 = (lambda_2-lambda_1)*(np.sin(self.theta)*np.cos(self.theta))*(vec[1:]/norm)
        return np.insert(x_2, 0, x_1, axis=0)

    def A_mean(self):
        A = (self.vec1 + self.vec2)/2
        return A
        
    def H_mean(self):
        self.vec1_inv = self.spec_inv(self.vec1)
        self.vec2_inv = self.spec_inv(self.vec2)
        H = self.spec_inv((self.vec1_inv + self.vec2_inv)/2)
        return H

    def max_mean(self):
        M = (self.vec1 + self.vec2 + self.spec_abs(self.vec1 - self.vec2))/2
        return M

    def min_mean(self):
        M = self.vec1 + self.vec2 - self.spec_abs(self.vec1 - self.vec2)
        # return M/2
        if inCone(M, self.theta):
            return M/2
        else:
            return np.zeros(len(M))