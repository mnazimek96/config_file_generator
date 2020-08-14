import pandas as pd
from functions.log_gen import write_log

input_file = "input/parameters_list.csv"
output_file = "config/config.ini"
try:
    data = pd.read_csv(input_file, sep=";")
    # ALL CONFIG VALUES ==========================================
    config_data = {
        "baud_rate": 1000000,
        "error_id": data.loc[data["GRUPA"] == "ERRORS", "ID"],
        "error_history": 1400,
        "config_ids": data.loc[data["CONFIG"] == 1, "ID"],
        "version_ids": 1,
        "inout_ids": 1,
        "presswitch_bits": 1,
        "otherstable_bits": 1,
        "prescount_ids": 1,
        "indicators_ids": 0,
        "mm_ids": data.loc[data["TRANSFER"] == 1, "ID"],
        "mms_ids": data.loc[data["TRANSFER"] == 2, "ID"],
        "control_ids": data.loc[data["GRUPA"] == "CTRL", "ID"]
    }
    # ============================================================
except FileNotFoundError:
    write_log("\nError: INPUT file does not exists or it is corrupted![config_info]\n"
              "!!! place parameters_list.csv to /input !!!")


def generate_config():
    f = open(output_file, "w")
    f.write("[settings]\n")

    for item in config_data:
        i = 0
        if str(config_data[item]).isdigit():
            f.write(f'\n{item}={config_data[item]}')
        else:
            f.write(f'\n{item}=')
            for item_id in config_data[item]:
                if i == 0:
                    f.write(f'{int(item_id)}')
                    i += 1
                else:
                    f.write(f',{int(item_id)}')

    f.write("\nindicators ids: errors_id,errors_nr,null,"
            "din_id,din_nr,din_start_id,dout_id,dout_nr,"
            "dour_start_id,relay_id,relay_nr,relay_start_id,"
            "DCU_state_id,DCU_state_bits_limit,null,max door width,\n"
            "mm ids: ids that should be translated from encoder pulses to milimeters,\n"
            "mms ids ids that should be translated to milimeters/second.\n"
            "control ids: param_change_id, crc_id\n\n")
    f.write(f'CHECKSUM: {1313123123145151}')
