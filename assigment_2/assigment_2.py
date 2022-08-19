import pandas as pd
from os import listdir
from os.path import isfile, join
from funix.assigment_2 import folder_path, folder_grade_path, local_dir


def get_file_path_in_folder(file_path: str):
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    # Chỉ lấy ra file txt
    valid_file_path = []
    for i in files:
        if 'class' in i:
            k = file_path + f"/{i}"
            valid_file_path.append(k)
    return valid_file_path


# Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
def main_part2():
    list_file_path = get_file_path_in_folder(file_path=folder_path)
    with open(f"{local_dir}/part2_output.txt", "w", encoding='utf-8', buffering=1) as f:
        for file_path in list_file_path:
            file_error = []
            file = open(file_path, "r")
            f.write(f"Successfully opened: {file_path} \n")
            lines = file.readlines()
            for line in lines:
                list_line = list(line.split(","))
                if len(list_line) != 26:
                    file_error.append(line)
            # trường hợp có line lỗi, print dòng bị lỗi
            if file_error:
                f.write(f"Invalid line of data: does not contain exactly 26 values: \n")
                for k in file_error:
                    f.write(k + '\n')
            else:
                f.write("No errors found!" + '\n')
            #         # Report file_error
            f.write(f"Total valid lines of data: {len(lines)}" + '\n')
            f.write(f"Total invalid lines of data: {len(file_error)}" + '\n')
            f.write("================================ RESTART ================================\n\n")


# Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo

def main_part3():
    list_file_grade_path = get_file_path_in_folder(file_path=folder_grade_path)
    with open(f"{local_dir}/part3_output.txt", "w", encoding='utf-8', buffering=1) as f:
        for file_grade_path in list_file_grade_path:
            f.write(f"Successfully opened {file_grade_path}" + '\n\n')

            class_name = file_grade_path.split('/')[-1].split('.')[0].split('_')[0]
            class_path = f"{local_dir}/sources/Data Files/{class_name}.txt"
            file_error = []
            file = open(class_path, "r")
            lines = file.readlines()
            for line in lines:
                list_line = list(line.split(","))
                if len(list_line) != 26:
                    file_error.append(line)
            # trường hợp có line lỗi, print dòng bị lỗi
            if file_error:
                f.write(f"Invalid line of data: does not contain exactly 26 values: \n")
                for k in file_error:
                    f.write(k + '\n')
            else:
                f.write("No errors found!" + '\n')
            #         # Report file_error
            f.write(f"Total valid lines of data: {len(lines)}" + '\n')
            f.write(f"Total invalid lines of data: {len(file_error)}" + '\n\n')

            file = open(file_grade_path, "r")
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
            f.write(f"Mean (average) score:, {df['grade'].mean()}\n")
            f.write(f"Highest score: {df['grade'].max()}\n")
            f.write(f"Lowest score: {df['grade'].min()}\n")

            f.write(f"Median score: {df['grade'].max()}\n")
            f.write("================================ RESTART ================================\n\n")


if __name__ == "__main__":
    # main_part2()
    main_part3()
