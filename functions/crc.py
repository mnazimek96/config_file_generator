import zlib
import pyaes, pbkdf2, binascii, os, secrets
from cryptography.fernet import Fernet


def crc_calc(file_name):
    prev = 0
    for eachLine in open(file_name, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def encrypt(crc):
    password = "letmein"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(16)
    print('AES encryption key:', binascii.hexlify(key))

    iv = secrets.randbits(128)
    plaintext = "Text for encryption"
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext))