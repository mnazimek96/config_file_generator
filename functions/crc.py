import zlib
from cryptography.fernet import Fernet


def crc_calc(file_name):
    prev = 0
    for eachLine in open(file_name, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def encrypt(crc):
    key = Fernet.generate_key()  # this is your "password"
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(crc)
    # decoded_text = cipher_suite.decrypt(encoded_text)
    print(encoded_text)