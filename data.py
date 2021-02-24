import os
import numpy as np

directory = './data/openclose/Stocks'


def get_files_content():
    number_of_files = len(os.listdir(directory))
    paths = np.empty([1, number_of_files], dtype=object)

    for index in range(2):
        filename = directory + "/" + os.listdir(directory)[index]
        print(filename)

        with open(filename) as curr_file:
            print(curr_file.readlines())
            file_lines = curr_file.readlines()
            lines_len = len(file_lines)
            param_len = 7

            file_content = np.empty([lines_len, param_len], dtype=object)

            for line_idx in range(lines_len):
                file_content[line_idx] = file_lines[line_idx].split(",")


get_files_content()
