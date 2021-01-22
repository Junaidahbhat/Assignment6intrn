# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:34:55 2021

@author: JUNAID AHMAD BHAT
"""
import numpy as np
import matplotlib.pyplot as plt


def dir_vec(O,K):
  return K-O


#Generate line points
def line_gen(O,K):
  len =10
  dim = O.shape[0]
  x_OK = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = O + lam_1[i]*(K-O)
    x_OK[:,i]= temp1.T
  return x_OK



def line_dir_pt(m,Y, dim):
  len = 10
  dim = Y.shape[0]
  x_YO = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = Y + lam_1[i]*m
    x_YO[:,i]= temp1.T
  return x_YO


#Quadrilateral vertices

O = np.array([0,0])
K = np.array([7,0])
A = np.array([7,5])
Y = np.array([0,5])

#Generating all lines

x_OK = line_gen(O,K)
x_KA = line_gen(K,A)
x_AY = line_gen(A,Y)
x_YO = line_gen(Y,O)

#Plotting all lines

plt.plot(x_OK[0,:],x_OK[1,:],label='$OK$')
plt.plot(x_KA[0,:],x_KA[1,:],label='$KA$')
plt.plot(x_AY[0,:],x_AY[1,:],label='$AY$')
plt.plot(x_YO[0,:],x_YO[1,:],label='$YO$')


plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 - 0.2), O[1] * (1) , 'O')
plt.plot(K[0], K[1], 'o')
plt.text(K[0] * (1 + 0.03), K[1] * (1 - 0.1) , 'K')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1), 'A')
plt.plot(Y[0], Y[1], 'o')
plt.text(Y[0] * (1 + 0.1), Y[1] * (1 - 0.1) , 'Y')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')