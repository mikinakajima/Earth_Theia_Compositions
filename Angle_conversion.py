# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

# original SPH data were stored at /mikinakajima/work/exomoon/g7016
"""

import numpy as np
import matplotlib.pyplot as plt


def read_files(infile,outfile):
    data = np.loadtxt(infile)

    # (5 columns: x, y, z, r, p)

    x = data[:,0]
    y = data[:,1]
    z = data[:,2]
    r = data[:,3]   # already included, good
    p = data[:,4]

 
    phi = np.arctan2(y, x) #longitude
    lat = np.arcsin(z / r) # latitude
    theta = np.arccos(z / r) # colatitutde

    # if you prefer in degrees

    # deg = 180/np.pi
    #phi = np.arctan2(y, x) * deg #longitude
    #lat = np.arcsin(z / r) * deg # latitude
    #theta = np.arccos(z / r) * deg # colatitutde



    # stack columns together
    out = np.column_stack([x, y, z, r, p, phi, lat])

    np.savetxt(outfile, out, fmt="%.8e", header="x y z r p longitude latitude")


# the target and impactors


read_files("target_SPH.txt","target_SPHwAngles.txt")
read_files("impactor_SPH.txt","impactor_SPHwAngles.txt")

# below - just for testing

def visualize_3d(filename, title=None):
    # File format: x y z r p longitude latitude  (angles in radians)
    data = np.loadtxt(filename)
    x, y, z, r, p, lon, lat = data.T

    # Reconstruct from (r, lon, lat)
    x2 = r * np.cos(lat) * np.cos(lon)
    y2 = r * np.cos(lat) * np.sin(lon)
    z2 = r * np.sin(lat)

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Original points
    ax.scatter(x, y, z, s=4, label="original", alpha=0.2,c='blue')

    # Reconstructed points
    ax.scatter(x2, y2, z2, s=4, marker='x', label="reconstructed", alpha=0.6,c='orange')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    if title is None:
        title = filename
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.show()

# Call for target and impactor
visualize_3d("target_SPHwAngles.txt",   "Target: original vs reconstructed")
visualize_3d("impactor_SPHwAngles.txt", "Impactor: original vs reconstructed")