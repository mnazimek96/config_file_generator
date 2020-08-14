from functions.param_alloc_function import generate_param_alloc
from functions.parameters_function import generate_parameters
from functions.defaults_function import generate_defaults
from functions import log_gen
from functions.config_function import generate_config
from functions.crc import encrypt
from functions.create_structure import create_dirs
from functions.parameters_function import error
import pandas as pd


if __name__ == "__main__":
    # create_dirs()
    log_gen.start_log()
    generate_parameters()
    generate_param_alloc()
    generate_defaults()
    generate_config()
    # test
    encrypt("0x58CED029")
    # crc.encrypt(b'0xDB46076C')
    # 514F4942414255564652573079396F614945325848413D3D
