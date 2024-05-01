# Lidar-Las-Visualise
Lider Las file to CSV conversion and the visualisation of LAS file using python.

**LAS (Lidar Data Exchange) is a widely used file format for storing lidar data. It typically contains three-dimensional point cloud data, which consists of x, y, and z coordinates representing the location of points in space, as well as additional attributes such as intensity and classification.**

***Script 1: LAS to CSV Conversion***
This script converts LAS files to CSV format, making it easier to work with the data in various applications. It utilizes the pylas library to read LAS files and csv library to write the data to a CSV file.

***Script 2: LAS File Visualization***
This script visualizes LAS files using the laspy library for reading LAS files and mayavi for 3D visualization. It extracts x, y, and z coordinates from the LAS file and visualizes the points in a 3D plot using Mayavi.

***Instructions for Usage***
Script 1: LAS to CSV Conversion
Ensure you have the required libraries installed (pylas).
Modify the las_input_file variable to point to your LAS file.
Run the script, and it will convert the LAS file to a CSV file.
Script 2: LAS File Visualization
Ensure you have the required libraries installed (laspy, mayavi).
Modify the las_file_path variable to point to your LAS file.
Run the script, and it will visualize the LAS file in a 3D plot.
