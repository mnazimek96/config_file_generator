import shutil

import pandas as pd
from datetime import datetime
import getpass
import numpy as np
from functions import log_gen
error = 0

input_file = "input/parameters_list.csv"
output_file = "output/defaults.h"
try:
    data = pd.read_csv(input_file, sep=';')
    sw_define_name = data["SW_DEFINE_NAME"]
    max_val = data["MAX"]
    min_val = data["MIN"]
    default_val = data["DEFAULT"]
    rw_val = data["RW"]
    config = data["CONFIG"]
    _id = data["ID"]

    # DEF_values
    DEF_values = ["id", "def_val", "range_max", "range_min", "rw"]

    # user info
    user = getpass.getuser()
except FileNotFoundError:
    log_gen.write_log("Error: INPUT file does not exists or it is corrupted!\n")
    error += 1


def make_spacing(data_0, i):
    if len(data_0["SW_DEFINE_NAME"].iloc[i]) >= 23:
        tab = 2 * '\t'
    elif len(data_0["SW_DEFINE_NAME"].iloc[i]) >= 19:
        tab = 3 * '\t'
    elif len(data_0["SW_DEFINE_NAME"].iloc[i]) >= 15:
        tab = 4 * '\t'
    elif len(data_0["SW_DEFINE_NAME"].iloc[i]) >= 11:
        tab = 5 * '\t'
    else:
        tab = 6 * '\t'
    return tab


def save_and_make_backup_h(file):
    global error
    if error == 0:
        log_gen.write_log("\n\n---> defaults.h generation <---")
        if not np.os.path.isfile(file):
            gen_file()
            log_gen.write_log('File ' + file + ' successfully created!')
        else:
            head, tail = np.os.path.split(file)
            name, ext = tail.split(".")
            shutil.copy(file, f'backup/{name}_backup.bkp')
            np.os.remove(file)
            gen_file()
            log_gen.write_log(f'\nNew file {tail} generated! --> dir: ./{file} \nBackup successfully created!')


def head_add():
    now = datetime.now()
    dt_str = now.strftime("%d/%m/%Y %H:%M:%S")
    f = open(output_file, 'w+')

    f.write(f"""/*
*defaults.h
*
*
*generated on: {dt_str}
*Author: {user}
*/

""")

    f.write("#ifndef DEFAULTS_H_\n#define DEFAULTS_H_\n")
    f.write("""
/* Two important infos:
* ->  This header should be included only in configuration.c file
* ->  Must include configuration.h and GENERAL_CONFIG.h before this one */\n
""")
    f.write("struct DEF_value {\n")
    for param in DEF_values:
        # you can add more conditions for different params
        if param == "id" or param == "rw":
            f.write(f'\tunit8_t {param};\n')
        else:
            f.write(f'\tint16_t {param};\n')
    f.write("};\n\n")
    f.close()


def parameters_add():
    parameter = "CONFIG_PARAMETER_SIZE"
    param_id = 0
    f = open(output_file, "a+")
    for i in range(len(config)):
        if config.iloc[i] == 0:
            param_id = i
            break
        else:
            param_id = len(config)
    f.write(f'#define {parameter} {param_id}\n\n')
    f.write(f"const static struct DEF_value configParamsDefaults[{parameter}]=\n"+"{\n")
    for j in range(param_id):
        min_val_ = int(min_val.iloc[j])
        default_val_ = int(default_val.iloc[j])
        rw_val_ = int(rw_val.iloc[j])
        tab = make_spacing(data, j)
        f.write('\t{'+f'{sw_define_name.iloc[j]}{tab},'
                      f'{str(min_val_).ljust(7," ")},'
                      f'{str(max_val.iloc[j]).ljust(11," ")},'
                      f'{str(default_val_).ljust(7," ")},'
                      f'{str(rw_val_).ljust(7," ")}' + "},\n")
    f.write("};\n\n")
    f.close()


def tail_add():
    f = open(output_file, "a+")
    f.write('#else\n'
            '#error "defaults.h file should be included only once!"\n'
            '#endif /* DEFAULTS_H_ */')
    f.close()


def gen_file():
    global error
    try:
        head_add()
        parameters_add()
        tail_add()
    except FileNotFoundError:
        log_gen.write_log("Error: INPUT file does not exists or it is corrupted![defaults_generation]")
        error += 1


def generate_defaults():
    save_and_make_backup_h("output/defaults.h")
