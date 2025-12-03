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
    r = data[:,3]  
    p = data[:,4]
    ID = data[:,5].astype(int)

 
    phi = np.arctan2(y, x) #longitude
    lat = np.arcsin(z / r) # latitude
    theta = np.arccos(z / r) # colatitutde

    # if you prefer in degrees

    # deg = 180/np.pi
    #phi = np.arctan2(y, x) * deg #longitude
    #lat = np.arcsin(z / r) * deg # latitude
    #theta = np.arccos(z / r) * deg # colatitutde



    # stack columns together
    out = np.column_stack([ID, x, y, z, r, p, phi, lat])
    
    
    fmt = ["%d", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e"]

    np.savetxt(outfile, out, fmt=fmt,
           header="ID x y z r p longitude latitude")

#    np.savetxt(outfile, out, fmt="%.8e", header="ID, x y z r p longitude latitude")


# the target and impactors


read_files("target_SPH.txt","target_SPHwAngles.txt")
read_files("impactor_SPH.txt","impactor_SPHwAngles.txt")





def select_disk_particles(disk_file, sph_file, outfile):
    # 1. Read disk IDs (first column), convert to int
    disk_ids = np.loadtxt(disk_file, usecols=0)
    disk_ids = disk_ids.astype(int)

    # 2. Read SPH file: ID x y z r p lon lat
    sph = np.loadtxt(sph_file)
    IDs = sph[:, 0].astype(int)

    # 3. Boolean mask: keep rows whose ID is in disk_ids
    mask = np.isin(IDs, disk_ids)
    selected = sph[mask]

    # 4. Save out: ID x y z r p lon lat
    fmt = ["%d", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e", "%.8e"]
    np.savetxt(outfile, selected, fmt=fmt,
               header="ID x y z r p longitude latitude")

# Examples:
select_disk_particles("disk.txt",
                      "target_SPHwAngles.txt",
                      "target_disk_particles.txt")

select_disk_particles("disk.txt",
                      "impactor_SPHwAngles.txt",
                      "impactor_disk_particles.txt")




# below - just for testing

def visualize_3d(filename, filename_disk, title=None):
    # File format: x y z r p longitude latitude  (angles in radians)
    data = np.loadtxt(filename)
    ID, x, y, z, r, p, lon, lat = data.T
    
    data_disk = np.loadtxt(filename_disk)
    ID_d, x_d, y_d, z_d, r_d, p_d, lon_d, lat_d  = data_disk.T

    # Reconstruct from (r, lon, lat)
    x2 = r * np.cos(lat) * np.cos(lon)
    y2 = r * np.cos(lat) * np.sin(lon)
    z2 = r * np.sin(lat)

    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Original points
    ax.scatter(x, y, z, s=1, label="original", alpha=0.3,c='blue')

    ax.scatter(x_d, y_d, z_d, s=10, label="disk particles", alpha=1,c='red')

    # Reconstructed points
   # ax.scatter(x2, y2, z2, s=4, marker='x', label="reconstructed", alpha=0.6,c='orange')

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
visualize_3d("target_SPHwAngles.txt",    "target_disk_particles.txt",  "Target: original vs disk particles")
visualize_3d("impactor_SPHwAngles.txt", "impactor_disk_particles.txt" , "Impactor: original vs disk particles")