from functions.param_alloc_function import generate_param_alloc
from functions.parameters_function import generate_parameters
from functions.defaults_function import head_add
from functions.create_structure import create_dirs
from functions import crc


if __name__ == "__main__":
    create_dirs()
    generate_parameters()
    generate_param_alloc()
    head_add()
    # crc.encrypt(b'0xDB46076C')
