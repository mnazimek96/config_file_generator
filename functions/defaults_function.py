import pandas as pd
from datetime import datetime
import getpass

input_file = "input/parameters_list.csv"
output_file = "output/defaults.h"
data = pd.read_csv(input_file, sep=';')
sw_define_name = data[["SW_DEFINE_NAME"]]
max = data[["MAX"]]
min = data[["MIN"]]
default = data[["DEFAULT"]]
rw = data[["RW"]]
config = data[["CONFIG"]]
id = data[["ID"]]

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
* ->  Must include configuration.h and GENERAL_CONFIG.h before this one */""")
    f.close()


def tail_add():
    print(0)
