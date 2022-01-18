from Crypto.Cipher import AES, DES
from simple_term_menu import TerminalMenu
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
        key = getpass('Enter your passphrase: ')

        if algorithm.upper() == 'AES':
            encoded_text = encode_text(text, 16)  # text size = multiple of 16
            key = encode_key(key, 16)  # key size = 128 bits
            cipher = AES.new(key, AES.MODE_ECB)
            encrypted_text = cipher.encrypt(encoded_text)
            print(f"Encrypted text: {encrypted_text.hex()}")
            return encrypted_text.hex()

        elif algorithm.upper() == 'DES':
            encoded_text = encode_text(text, 8)  # text size = multiple of 8
            key = encode_key(key, 8)  # key size = 64 bits
            cipher = DES.new(key, DES.MODE_ECB)
            encrypted_text = cipher.encrypt(encoded_text)
            print(f"Encrypted text: {encrypted_text.hex()}")
            return encrypted_text.hex()

        else:
            print("Algorithm not supported")

    @staticmethod
    def decrypt(encrypted_text: hex, algorithm: str):
        key = getpass('Enter your passphrase: ')

        if algorithm.upper() == 'AES':
            key = encode_key(key, 16)  # key size = 128 bits
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text)).decode("utf-8").strip()
            print(f"Decrypted text: {decrypted_text}")
            return decrypted_text

        elif algorithm.upper() == 'DES':
            key = encode_key(key, 8)  # key size = 64 bits
            cipher = DES.new(key, DES.MODE_ECB)
            decrypted_text = cipher.decrypt(bytes.fromhex(encrypted_text)).decode("utf-8").strip()
            print(f"Decrypted text: {decrypted_text}")
            return decrypted_text

        else:
            print("Algorithm not supported")

    @staticmethod
    def menu():
        while True:
            print("====> Symmetric Encryption")
            m_choices = ['Encrypt a message', 'Decrypt a message', 'Go back']
            terminal = TerminalMenu(m_choices)
            entry = terminal.show()
            if entry == 0:
                while True:
                    message = None
                    while message is None:
                        message = str(input("-Message to encrypt: "))
                    print("---choose an encryption algorithm---")
                    choices = ['0- AES', '1- DES', '3- Go back']
                    terminal = TerminalMenu(choices)
                    menu_entry_index = terminal.show()
                    encrypted = None
                    if menu_entry_index == 0:
                        encrypted = Symmetric.encrypt(message, 'aes')
                    elif menu_entry_index == 1:
                        encrypted = Symmetric.encrypt(message, 'des')
                    else:
                        break

                    print('Decrypt the cipher ?')
                    yn_choices = ['Yes', 'No']
                    terminal = TerminalMenu(yn_choices)
                    resp = terminal.show()
                    if resp == 1:
                        print('No')
                        break
                    if menu_entry_index == 0:
                        Symmetric.decrypt(encrypted, 'aes')
                    elif menu_entry_index == 1:
                        Symmetric.decrypt(encrypted, 'des')

                    print('\t------------------------')
                    break

            elif entry == 1:
                encrypted = None
                while encrypted is None:
                    encrypted = str(input("- Cipher: "))
                print("---choose the encryption algorithm---")
                choices = ['0- AES', '1- DES', '3- Go back']
                terminal = TerminalMenu(choices)
                menu_entry_index = terminal.show()
                if menu_entry_index == 0:
                    # encrypted = encode_text(encrypted.decode(),16)
                    Symmetric.decrypt(encrypted, 'aes')
                elif menu_entry_index == 1:
                    Symmetric.decrypt(encrypted, 'des')
                else:
                    break
            else:
                break
