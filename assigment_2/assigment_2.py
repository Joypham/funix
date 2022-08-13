import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

folder_path = "/Users/phamhanh/Documents/Funix/Data Files"
folder_grade_path = "/Users/phamhanh/Documents/Funix/Data Files/Expected Output"


def get_file_path_in_folder():
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    # Chỉ lấy ra file txt
    valid_file_path = []
    for i in files:
        if 'txt' in i:
            k = folder_path + f"/{i}"
            valid_file_path.append(k)
    return valid_file_path


def get_file_grade_path_in_folder():
    files = [f for f in listdir(folder_grade_path) if isfile(join(folder_grade_path, f))]
    # Chỉ lấy ra file txt
    valid_file_path = []
    for i in files:
        if 'grades' in i:
            k = folder_grade_path + f"/{i}"
            valid_file_path.append(k)
    return valid_file_path


# Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
def main_2():
    list_file_path = get_file_path_in_folder()
    with open("/Users/phamhanh/Documents/Funix/Data Files/main_2.txt", "a+", encoding='utf-8', buffering=1) as f:
        # list_file_path = ["/Users/phamhanh/Documents/Funix/Data Files/class1.txt"]
        for file_path in list_file_path:
            file_error = []
            print(f"Successfully opened {file_path}")
            # f.write(f"Successfully opened {file_path}" + '\n')
            file = open(file_path, "r")
            lines = file.readlines()
            for line in lines:
                list_line = list(line.split(","))
                if len(list_line) != 26:
                    file_error.append(line)

            # trường hợp có line lỗi, print dòng bị lỗi
            if file_error:
                for k in file_error:
                    print(k)
                    # f.write(k + '\n')

            else:
                # f.write("No errors found!" + '\n')
                print("No errors found!")

            # Report file_error
            # f.write(f"Total valid lines of data: {len(lines)}" + '\n')
            # f.write(f"Total invalid lines of data: {len(file_error)}" + '\n')
            # f.write("================================ RESTART ================================\n\n")
            print(f"Total valid lines of data: {len(lines)}")
            print(f"Total invalid lines of data: {len(file_error)}")
            print("================================ RESTART ================================\n\n")


# Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo

def main_3():
    list_file_path = get_file_grade_path_in_folder()
    with open("/Users/phamhanh/Documents/Funix/Data Files/main_3.txt", "a+", encoding='utf-8', buffering=1) as f:
        for file_path in list_file_path:
            print(file_path)
            f.write(f"Successfully opened {file_path}" + '\n')
            file = open(file_path, "r")
            lines = file.readlines()
            id = []
            grade = []
            for line in lines:
                list_line = list(line.split(","))
                id.append(list_line[0])
                grade.append(int(list_line[1].strip()))
            data = {'id': id,
                    'grade': grade}
            df = pd.DataFrame(data)
            print("Mean (average) score:", df['grade'].mean())
            print("Lowest score:", df['grade'].min())
            print("Highest score: ", df['grade'].max())
            print("Median score:", df['grade'].max())


if __name__ == "__main__":
    # main_2()
    # main_2()
    main_3()
    # get_file_grade_path_in_folder()
