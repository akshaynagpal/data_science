>>> from numpy import *

>>> random.rand(4,4)
array([[ 0.79509808,  0.19335871,  0.98598061,  0.8024657 ],
       [ 0.59136923,  0.34615494,  0.68378882,  0.6309914 ],
       [ 0.53365134,  0.37850601,  0.10067898,  0.06932015],
       [ 0.66356218,  0.37288525,  0.41526366,  0.29023837]])

>>> randMat = mat(random.rand(4,4)) #converting array to matrix

>>> randMat
matrix([[ 0.60113398,  0.5006341 ,  0.79068104,  0.53310908],
        [ 0.78389641,  0.08556004,  0.33583135,  0.9013885 ],
        [ 0.64956891,  0.7810938 ,  0.700817  ,  0.25559546],
        [ 0.66090946,  0.92180052,  0.62672922,  0.52688238]])

>>> randMat.I #inverse of a matrix
matrix([[-2.71795221,  1.75783871,  4.33461581, -2.35999296],
        [-0.82219657, -0.61536594, -0.81764464,  2.28132605],
        [ 2.94525717, -0.93947136, -0.38526834, -1.18592281],
        [ 1.34440414, -0.01088185, -3.54846644,  2.27767461]])
>>> invRandMat = randMat.I
>>> randMat*invRandMat #matrix multiplication
matrix([[  1.00000000e+00,   6.24649059e-18,  -3.77877211e-17,
           5.22968978e-16],
        [  6.47772436e-17,   1.00000000e+00,  -5.89643265e-16,
           2.11029227e-16],
        [  2.14578387e-16,  -4.03832563e-17,   1.00000000e+00,
           1.80473748e-16],
        [  5.34523414e-16,  -8.45867418e-17,  -2.18358209e-16,
           1.00000000e+00]])
>>> eye(4) #eye(4) creates an identity matrix of size 4