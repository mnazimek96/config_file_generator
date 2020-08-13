from functions.param_alloc_function import generate_param_alloc
from functions.parameters_function import generate_parameters
from functions.defaults_function import generate_defaults


if __name__ == "__main__":
    generate_parameters()
    generate_param_alloc()
    generate_defaults()

    # crc.encrypt(b'0xDB46076C')
