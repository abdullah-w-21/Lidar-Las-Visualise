import laspy
from mayavi import mlab

# pip install laspy
# pip install mayavi
def visualize_las_file(las_file_path):
    # Opening the .las file
    las = laspy.read(las_file_path)

    # x, y, z coordinates from the .las file
    x = las.x
    y = las.y
    z = las.z

    # Visualize the points using mayavi
    fig = mlab.figure(bgcolor=(1, 1, 1), size=(800, 600))
    mlab.points3d(x, y, z, mode="point", color=(0, 0, 1), scale_factor=1)
    mlab.show()

las_file_path = "1.Las"  # Modify this path to match your file
visualize_las_file(las_file_path)
