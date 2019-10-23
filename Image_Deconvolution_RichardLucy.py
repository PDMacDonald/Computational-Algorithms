# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:39:24 2018

@author: Preston
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2

from scipy.ndimage.filters import gaussian_filter
# skimage.color contains a library of color space conversions.
# skimage.data contains a library of images for testing purposes.
# skimage.restoration ccontains a librayry of image restoration algorithms
# which includes our algorithm for richardson lucy.
from skimage import color, data, restoration



# ~~~~~~~~~~~~~~~~~~~~~ Starting Code ~~~~~~~~~~~~~~~~~~~

#Storing ORIGINAL image as a variable and converting to a gray colorspace.
originImage = color.rgb2gray(data.astronaut())
print(originImage.shape)




#Generates a point spread function
a = 250
b = 75
c = 20
d = 0
psf = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0], \
       [ 0, d, d, d, d, d, d, d, 0], \
       [ 0, d, c, c, c, c, c, d, 0], \
       [ 0, d, c, b, b, b, c, d, 0], \
       [ 0, d, c, b, a, b, c, d, 0], \
       [ 0, d, c, b, b, b, c, d, 0], \
       [ 0, d, c, c, c, c, c, d, 0], \
       [ 0, d, d, d, d, d, d, d, 0], \
       [ 0, 0, 0, 0, 0, 0, 0, 0, 0], \
       ]


psf = np.asarray(psf)
print(psf)


#Convolves 2 arrays
originImage = conv2(originImage, psf, 'same')


# Add Noise to Image
originImage_noisy = originImage.copy()
originImage_noisy += (np.random.poisson(lam=25, size=originImage.shape) - 10) / 255.

originImage_noisy = gaussian_filter(originImage_noisy, sigma=2.5)

# Restore Image using Richardson-Lucy algorithm
deconvolved_RL = restoration.richardson_lucy(originImage_noisy, psf, iterations=1, clip= False)

for i in range(1):
    #deconvolved_RL = restoration.richardson_lucy(deconvolved_RL, psf, iterations=5, clip= False)
    deconvolved_RL = restoration.richardson_lucy(deconvolved_RL, psf, iterations=10, clip= False)






    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("i =", i)
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(14, 8))
    plt.gray()
    
    for a in (ax[0], ax[1], ax[2]):
           a.axis('off')
    
    ax[0].imshow(originImage)
    ax[0].set_title('Original Data')
    
    ax[1].imshow(originImage_noisy)
    ax[1].set_title('Noisy data')
    
    ax[2].imshow(deconvolved_RL, vmin=originImage_noisy.min(), vmax=originImage_noisy.max())
    ax[2].set_title('Restoration using\nRichardson-Lucy')
    
    
    fig.subplots_adjust(wspace=0.02, hspace=0.2,
                        top=0.9, bottom=0.05, left=0, right=1)
    fig.savefig('ImageRest.png')
    plt.show()

# ~~~~~~~~~ Plot of different iterations ~~~~~~~~~

norm = 2

#Being that the restoration image is causing border noise we need to take the
#norm near the center of the image to get a proper idea of how the percent
#error between images are changing as iterations increase.
subgrid = np.ix_([246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256],\
                        [246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256])
subgrid[0].shape, subgrid[1].shape





originImageNorm = np.linalg.norm(originImage[subgrid], norm)


x = []
y = []

RL = restoration.richardson_lucy(originImage_noisy, psf, iterations=1, clip= False)

for i in range(20):
    RL = restoration.richardson_lucy(RL , psf, iterations=2, clip= False)
    re = abs(np.linalg.norm(originImage[subgrid] - RL[subgrid], norm)) / abs(originImageNorm)
    print("Richard Lucy i =", i, ":", re)
    
    x.append(i);
    y.append(re);
    
plt.scatter(x,y)
plt.xlabel('Iterations')
plt.ylabel('Relative Error')
plt.savefig('REvsIGraph.png')
plt.show()

reNoisy = np.linalg.norm(originImage[subgrid] - originImage_noisy[subgrid], norm) / originImageNorm
print("Relative Error between Noisy data and Original:", reNoisy)