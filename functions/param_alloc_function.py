import pandas as pd
import numpy as np
import shutil
import math
from functions import crc
from functions.create_structure import create_dirs
from functions import log_gen
error = 0


def make_spacing(data, i):
    if not np.isnan(data["ID"].iloc[i]):
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
    else:
        pass


def generate_and_process_data_param_alloc():
    global error
    create_dirs()
    try:
        input_file = "input/parameters_list.csv"
        data = pd.read_csv(input_file, sep=";")
        log_gen.write_log("\n\n---> param_alloc.h generation <---")
        sw_define_name = data[["SW_DEFINE_NAME"]]
        output_file = "output/param_alloc.h"
        f = open(output_file, "w+")
        for i in range(len(sw_define_name)):
            tab = make_spacing(data, i)
            group = data["GRUPA"].iloc[i]
            _id = data["ID"].iloc[i]
            if not math.isnan(_id):
                _id = int(_id)
            if i == 0:
                f.write("/*\n"
                        " * NO INCLUDE GUARD AS THE FILE IS ONLY INCLUDED IN DIAGNOSIS.H\n"
                        " * */\n\n")
                f.write(f'/* {group} */\n')
                f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{_id}\n')
            elif data["OPIS"].iloc[i] == "CTRL_CRC_PARAM_LIST":
                f.write(f'\n#define {data["SW_DEFINE_NAME"].iloc[i]}\t{crc.crc_calc(input_file)}\n')
            else:

                if group == "SPARE":
                    f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{_id}\n')
                elif group == "FEATURE":
                    l += 1
                    f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}({data["SW_DEFINE_NAME"].iloc[i-l]} + {l})\n')
                else:
                    if group != data["GRUPA"].iloc[i-1]:
                        l = 0
                        f.write(f'\n/* {group} */\n')
                        f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{_id}\n')
                    else:
                        f.write(f'#define {data["SW_DEFINE_NAME"].iloc[i]}{tab}{_id}\n')

        f.close()
        if np.os.path.isfile(output_file):
            log_gen.write_log('\nFile ' + output_file + ' successfully created!')
        else:
            head, tail = np.os.path.split(output_file)
            log_gen.write_log(f'\nNew file {tail} generated! --> dir: ./{output_file}')
        return output_file
    except FileNotFoundError:
        log_gen.write_log("\nError: INPUT file does not exists or wrong dir![param_alloc_info]\n"
                          "!!! place parameters_list.csv to /input !!!")
        error += 1


def save_and_make_backup_h(file):
    if not np.os.path.isfile(file):
        generate_and_process_data_param_alloc()
    else:
        head, tail = np.os.path.split(file)
        name, ext = tail.split(".")
        shutil.copy(file, f'output/backup/{name}_backup.bkp')
        np.os.remove(file)
        generate_and_process_data_param_alloc()
        log_gen.write_log('\nBackup successfully created!')


def generate_param_alloc():
    save_and_make_backup_h("output/param_alloc.h")
