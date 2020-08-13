import pandas as pd
import numpy as np
import shutil
from functions import crc
from functions.create_structure import create_dirs
from functions import log_gen

error = 0


def generate_and_process_data(input_file):
    global error
    log_gen.write_log("---> general info <---\n")
    try:
        _crc = crc.crc_calc(input_file)
        log_gen.write_log(f"INPUT CSV file CRC: 0x{_crc}\n")
        data = pd.read_csv(input_file, sep=';')
        log_gen.write_log("INPUT CSV file columns: ")
        for col in data.columns:
            log_gen.write_log(f'{col}, ')

        log_gen.write_log("\n\n---> parameters.csv generation <---")
        data = data[data["CONFIG"] >= 0]
        parameters = data[["GRUPA", "ID", "OPIS", "FORMAT", "MIN", "MAX"]]
        log_gen.write_log("\nOUTPUT CSV file columns: ")
        for col in parameters.columns:
            log_gen.write_log(f'{col}, ')
        empty = pd.DataFrame({"GRUPA": [None, None, f'CHECKSUM: {_crc}'],
                              "ID": [None, None, None],
                              "OPIS": ["", "", ""],
                              "FORMAT": [None, None, None],
                              "MIN": [None, None, None],
                              "MAX": ["", "", ""]})

        parameters["ID"] = parameters["ID"].astype(int)
        parameters["MIN"] = parameters["MIN"].astype(int)
        parameters = parameters.append(empty, ignore_index=True)
        return parameters
    except FileNotFoundError:
        log_gen.write_log("Error: INPUT file does not exists or it is corrupted!")
        error += 1


def save_and_make_backup_csv(file_path, parameters):
    if error == 0:
        files_present = np.os.path.isfile(file_path)
        if not files_present:
            parameters.to_csv(file_path, sep=";", index=False)
            log_gen.write_log('\nfile ' + file_path + ' successfully created!')
        else:
            head, tail = np.os.path.split(file_path)
            name, ext = tail.split(".")
            shutil.copy(file_path, f'backup/{name}_backup.csv')
            np.os.remove(file_path)
            parameters.to_csv(file_path, sep=";", index=False)
            log_gen.write_log(f'\nNew file {tail} generated! --> dir: ./{file_path} \nBackup successfully created!')
    else:
        pass


def generate_parameters():

    create_dirs()
    input_file = "input/parameters_list.csv"
    output_file = "output/parameters.csv"
    data = generate_and_process_data(input_file)
    save_and_make_backup_csv(output_file, parameters=data)
