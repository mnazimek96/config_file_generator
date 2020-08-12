import pandas as pd
from datetime import datetime
import getpass

input_file = "input/parameters_list.csv"
output_file = "output/defaults.h"
data = pd.read_csv(input_file, sep=';')
sw_define_name = data[["SW_DEFINE_NAME"]]
max_val = data[["MAX"]]
min_val = data[["MIN"]]
default_val = data[["DEFAULT"]]
rw_val = data[["RW"]]
config = data[["CONFIG"]]
_id = data[["ID"]]

# DEF_values
DEF_values = ["id", "def_val", "range_max", "range_min", "rw"]

# user info
user = getpass.getuser()


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
    f = open(output_file, "a+")
    for i in range(len(config)):
        if data["CONFIG"].iloc[i] == 0:
            param_id = i
            break
    f.write(f'#define CONFIG_PARAMETER_SIZE {param_id}\n\n')
    f.close()


def tail_add():
    f = open(output_file, "a+")
    f.write('#else\n'
            '#error "defaults.h file should be included only once!"\n'
            '#endif /* DEFAULTS_H_ */')
    f.close()


def generate_defaults():
    head_add()
    parameters_add()
    tail_add()

