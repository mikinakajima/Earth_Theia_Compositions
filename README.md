# SPH disk particle selection and visualization

This script reads SPH output files, adds spherical coordinates, selects particles that belong to the moon‐forming disk, and makes simple 3D plots.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Input files

The script expects the following text files in the same directory.

1. `target_SPH.txt`  
2. `impactor_SPH.txt`  

Each of these SPH files has 6 columns

1. `x`  Cartesian x position  
2. `y`  Cartesian y position  
3. `z`  Cartesian z position  
4. `r`  Distance from the planet center  
5. `p`  Pressure (or another scalar quantity)  
6. `ID` Integer particle ID  

and

3. `disk.txt`  

This file lists the particles that belong to the disk.  
Only the first column is used and it is interpreted as integer particle ID.

## What the script does

1. **Add spherical coordinates and reorder columns**

   For each of `target_SPH.txt` and `impactor_SPH.txt` the function `read_files`  
   - reads `x, y, z, r, p, ID`  
   - computes longitude and latitude in radians  
     - `longitude = arctan2(y, x)`  
     - `latitude  = arcsin(z / r)`  
   - writes a new file with the columns  

     `ID  x  y  z  r  p  longitude  latitude`

   Output files  
   - `target_SPHwAngles.txt`  
   - `impactor_SPHwAngles.txt`

2. **Select disk particles**

   The function `select_disk_particles`  
   - reads the disk IDs from `disk.txt`  
   - reads `ID x y z r p longitude latitude` from the SPH+angle files  
   - keeps only rows whose `ID` appears in `disk.txt`  

   Output files  
   - `target_disk_particles.txt`  
   - `impactor_disk_particles.txt`  

   These files have the same 8 columns as above.  
   The first column (`ID`) is written as an integer.  
   All other columns use `%.8e` format.

3. **Visualize the result**

   The function `visualize_3d`  
   - reads one of the full SPH files with angles  
   - reads the matching disk subset file  
   - plots all SPH particles in blue  
   - overplots disk particles in red  

   The script calls  
   - `visualize_3d("target_SPHwAngles.txt", "target_disk_particles.txt", "Target original vs disk particles")`  
   - `visualize_3d("impactor_SPHwAngles.txt", "impactor_disk_particles.txt", "Impactor original vs disk particles")`

## How to run

From the command line

```bash
python sph_disk_analysis.py
