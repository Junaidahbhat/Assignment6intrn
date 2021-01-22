# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:21:33 2021

@author: JUNAID AHMAD BHAT
"""
import numpy as np
import matplotlib.pyplot as plt


def dir_vec(L,D):
  return D-L


#Generate line points
def line_gen(L,D):
  len =10
  dim = L.shape[0]
  x_LD = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = L + lam_1[i]*(D-L)
    x_LD[:,i]= temp1.T
  return x_LD


def line_dir_pt(m,O, dim):
  len = 10
  dim = O.shape[0]
  x_OL = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = O + lam_1[i]*m
    x_OL[:,i]= temp1.T
  return x_OL


#Quadrilateral vertices

L = np.array([0,0])
D = np.array([5,0])
G = np.array([2.5,5.45])
O = np.array([-1.876,7.26])

#Generating all lines

x_LD = line_gen(L,D)
x_DG = line_gen(D,G)
x_GO = line_gen(G,O)
x_OL = line_gen(O,L)
x_LG = line_gen(L,G)
x_DO = line_gen(D,O)

#Plotting all lines

plt.plot(x_LD[0,:],x_LD[1,:],label='$LD$')
plt.plot(x_DG[0,:],x_DG[1,:],label='$DG$')
plt.plot(x_GO[0,:],x_GO[1,:],label='$GO$')
plt.plot(x_OL[0,:],x_OL[1,:],label='$OL$')
plt.plot(x_LG[0,:],x_LG[1,:],label='$LG$')
plt.plot(x_DO[0,:],x_DO[1,:],label='$DO$')

plt.plot(L[0], L[1], 'o')
plt.text(L[0] * (1 - 0.2), L[1] * (1) , 'L')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(G[0], G[1], 'o')
plt.text(G[0] * (1 + 0.03), G[1] * (1 - 0.1), 'G')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')