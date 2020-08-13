from functions.param_alloc_function import generate_param_alloc
from functions.parameters_function import generate_parameters
from functions.defaults_function import generate_defaults
from functions import log_gen
from functions.create_structure import create_dirs


if __name__ == "__main__":
    create_dirs()
    log_gen.start_log()
    generate_parameters()
    generate_param_alloc()
    generate_defaults()
    # crc.encrypt(b'0xDB46076C')
