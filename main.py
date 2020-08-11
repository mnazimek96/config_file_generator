import math
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


def make_spacing(data, name_len, i):
    if len(data["SW_DEFINE_NAME"].iloc[i]) > 23:
        tab = 2 * '\t'
    elif len(data["SW_DEFINE_NAME"].iloc[i]) > 19:
        tab = 3 * '\t'
    elif len(data["SW_DEFINE_NAME"].iloc[i]) >= 18:
        tab = 4 * '\t'
    elif len(data["SW_DEFINE_NAME"].iloc[i]) >= 13:
        tab = 5 * '\t'
    else:
        tab = 6 * '\t'
    return tab


def generate_and_process_data_param_alloc():
    input_file = "input/parameters_list.csv"
    data = pd.read_csv(input_file, sep=";")
    sw_define_name = data[["SW_DEFINE_NAME"]]
    output_file = "output/param_alloc.h"
    f = open(output_file, "w+")
    for i in range(len(sw_define_name)-3):
        tab = make_spacing(data, data["SW_DEFINE_NAME"].iloc[i], i)
        group = data["GRUPA"].iloc[i]
        id = data["ID"].iloc[i]
        if not math.isnan(id):
            id = int(id)
        if i == 0:
            f.write("/*\n"
                    " * NO INCLUDE GUARD AS THE FILE IS ONLY INCLUDED IN DIAGNOSIS.H\n"
                    " * */\n\n")
            f.write(f'/* {group} */\n')
            f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{id}\n')
        else:
            if group == "SPARE":
                f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{id}\n')
            else:
                if group != data["GRUPA"].iloc[i-1]:
                    f.write(f'\n/* {group} */\n')
                    f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{id}\n')
                else:
                    f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{id}\n')
    f.close()
    return output_file


def save_and_make_backup_h(file):
    if not np.os.path.isfile(file):
        generate_and_process_data_param_alloc()
        print('file ' + file + ' successfully created!')
    else:
        head, tail = np.os.path.split(file)
        name, ext = tail.split(".")
        shutil.copy(file, f'backup/{name}_backup.{ext}')
        np.os.remove(file)
        generate_and_process_data_param_alloc()
        print(f'New file {tail} generated! --> dir: /{file} \nBackup successfully created!')


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


def generate_param_alloc():
    save_and_make_backup_h("output/param_alloc.h")


if __name__ == "__main__":
    generate_parameters()
    generate_param_alloc()







