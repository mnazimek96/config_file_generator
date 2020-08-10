import zlib
import pandas as pd
import numpy as np
import shutil


def crc_calc(fileName):
    prev = 0
    for eachLine in open(fileName, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)


def generate_and_process_data(input_file):
    data = pd.read_csv(input_file, sep=';')
    data = data[data["CONFIG"] >= 0]
    parameters = data[["GRUPA", "ID", "OPIS", "FORMAT", "MIN", "MAX"]]
    parameters["ID"] = parameters["ID"].astype(int)
    parameters["MIN"] = parameters["MIN"].astype(int)

    return parameters


def save_and_make_backup_csv(file_path, parameters):

    files_present = np.os.path.isfile(file_path)
    if not files_present:
        parameters.to_csv(file_path, sep=";", index=False)
        print('file ' + file_path + ' successfully created!')
    else:
        head, tail = np.os.path.split(file_path)
        name, ext = tail.split(".")
        shutil.copy(file_path, f'backup/{name}_backup.csv')
        np.os.remove(file_path)
        parameters.to_csv(file_path, sep=";", index=False)

        print(f'New file {tail} generated! --> dir: /{file_path} \nBackup successfully created!')


def generate_parameters():
    input_file = "input/parameters_list.csv"
    output_file = "output/parameters.csv"
    data = generate_and_process_data(input_file)
    save_and_make_backup_csv(output_file, parameters=data)


if __name__ == "__main__":
    generate_parameters()





