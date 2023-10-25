# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:00:27 2022

@author: hansd
"""
import numpy as np
import pylab as pl
from matplotlib.artist import Artist
#%%
#f = pl.axes(xlim=(-100, 100), ylim=(-100, 100))
patch_array = np.array([])
patch_array = np.append(patch_array,pl.Circle([0, 0], 10, fc='r'))
patch_array = np.append(patch_array,pl.Circle([-50, 20.444], 4, fc='black'))
ax = pl.axes(xlim=(-100, 100), ylim=(-100, 100))
ax.add_patch(patch_array[0])
ax.add_patch(patch_array[1])
pl.pause(1)
patch_array[0].remove()
pl.show()
#%%
patch1.remove()
ax.add_patch(patch2)
pl.show()
#%%
f = pl.figure()
patch = pl.Circle([2, -5], 4, ec='b', fill=False, ls='solid')
ax = pl.axes(xlim=(-10, 10), ylim=(-10, 10))
ax.add_patch(patch)
pl.show()
#%%
f = pl.figure()
patch = pl.Circle([-4., -4.], 3, fc='r')
ax = pl.axes(xlim=(-10, 10), ylim=(-10, 10))
ax.add_patch(patch)

pl.pause(1)
patch.center = [8, 2]
pl.pause(1)
pl.show()
#%%
f = pl.figure()
patch = pl.Circle([-10., -10.], 1, fc='r')
ax = pl.axes(xlim=(-10, 10), ylim=(-10, 10))
ax.add_patch(patch)

for i in range(-10, 10):
    patch.center = [i, i]
    pl.pause(0.001)
pl.show()