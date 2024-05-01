import pylas
import csv
import os

# to run this use this command in the terminal to firstly install all the required library
# pip install pylas
# pip install csv
# pip install os

def convert_las_to_csv(las_file_path, output_csv_name):
    las = pylas.read(las_file_path)
    points = las.points
    output_csv_path = os.path.join(os.path.dirname(__file__), output_csv_name)
    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['X', 'Y', 'Z'])
        for point in points:
            writer.writerow([point[0], point[1], point[2]]) # arrays of x,y,z axis (3d data) --> las file content
    return output_csv_path


def main():
    # enter the file path of the las file
    las_input_file = "1.Las"


    if not os.path.exists(las_input_file):
        print("Input file(s) not found!")
        return

    output_csv_las = convert_las_to_csv(las_input_file, 'output_las.csv')
    print(f"LAS to CSV conversion successful. CSV file saved at: {output_csv_las}")


if __name__ == "__main__":
    main()
