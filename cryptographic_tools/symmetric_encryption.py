from Crypto.Cipher import AES, DES
from stdiomask import getpass


def encode_key(key: str, length: int):
    key = str.encode(key)
    if len(key) < length:
        key = key + str.encode(str((length - len(key)) * "*"))
    elif len(key) > length:
        key = key[:length]
    return key


def encode_text(text: str, mod: int):
    text = text.encode()
    to_add = mod - (len(text) % mod)
    return text + str.encode(" " * to_add)


class Symmetric:
    @staticmethod
    def encrypt(text: str, algorithm: str):
        print('Enter your passphrase: ')
        key = getpass()

        if algorithm.upper() == 'AES':
            encoded_text = encode_text(text, 16)  # text size = multiple of 16
            key = encode_key(key, 16)  # key size = 128 bits
            cipher = AES.new(key, AES.MODE_ECB)
            encrypted_text = cipher.encrypt(encoded_text)
            print(f"Encrypted text: {encrypted_text}")
            return encrypted_text

        elif algorithm.upper() == 'DES':
            encoded_text = encode_text(text, 8)  # text size = multiple of 8
            key = encode_key(key, 8)  # key size = 64 bits
            cipher = DES.new(key, DES.MODE_ECB)
            encrypted_text = cipher.encrypt(encoded_text)
            print(f"Encrypted text: {encrypted_text}")
            return encrypted_text

        else:
            print("Algorithm not supported")

    @staticmethod
    def decrypt(encrypted_text: str, algorithm: str):
        print('Enter your passphrase: ')
        key = getpass()

        if algorithm.upper() == 'AES':
            key = encode_key(key, 16)  # key size = 128 bits
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted_text = cipher.decrypt(encrypted_text).decode("utf-8").strip()
            print(f"Decrypted text: {decrypted_text}")
            return decrypted_text

        elif algorithm.upper() == 'DES':
            key = encode_key(key, 8)  # key size = 64 bits
            cipher = DES.new(key, DES.MODE_ECB)
            decrypted_text = cipher.decrypt(encrypted_text).decode("utf-8").strip()
            print(f"Decrypted text: {decrypted_text}")
            return decrypted_text

        else:
            print("Algorithm not supported")
