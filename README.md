# SPH Angle Conversion

This repository contains a simple Python script that reads SPH particle output files and adds longitude and latitude for each particle based on its (x, y, z) position. This is useful for visualizing particle distributions on a sphere and for analyzing planetary impact simulations.

## Files
- Angle_conversion.py : Main script that performs the coordinate conversion
- target_SPH.txt : Example input file (target particles)
- target_SPHwAngles.txt : Output file with added longitude/latitude
- impactor_SPH.txt : Example input file (impactor particles)
- impactor_SPHwAngles.txt : Output file with added longitude/latitude

## Input Format
The expected input file has five columns:
x   y   z   r   p
where x, y, and z are Cartesian coordinates (meters), r is the particle distance from the origin (meters), and p is any scalar property (such as pressure).

## Output Format
The script produces a new file with the original five columns plus two new ones:
longitude   latitude
Both angles are in radians. Longitude is computed as atan2(y, x), and latitude is computed as arcsin(z / r). The script also includes commented-out lines that can output degrees instead if preferred.

## Usage
Run the script with:
python Angle_conversion.py
By default, it converts:
target_SPH.txt → target_SPHwAngles.txt
impactor_SPH.txt → impactor_SPHwAngles.txt
You can edit the filenames inside the script to process additional files.

## Notes
- Only NumPy is required.
- The origin should correspond to the center of the body being mapped onto a sphere.
- The script structure is simple and easy to modify.

