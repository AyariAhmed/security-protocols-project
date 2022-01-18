import hashlib
import os

from simple_term_menu import TerminalMenu


class Hash:

    @staticmethod
    def hash(message: str, algorithm: str, print_hashed=False):
        encoded_message = message.encode()
        hashed = None
        if algorithm.upper() == 'MD5':
            hashed = hashlib.md5(encoded_message).hexdigest()
        elif algorithm.upper() == 'SHA1':
            hashed = hashlib.sha1(encoded_message).hexdigest()
        elif algorithm.upper() == 'SHA256':
            hashed = hashlib.sha256(encoded_message).hexdigest()
        else:
            print('Hash algorith is not supported!')
        if print_hashed:
            print(f"Hashed message: {hashed}")
        return hashed

    @staticmethod
    def crack_hash(hashed_msg: str, algorithm: str, print_cracked=False):
        with open(f'{os.getcwd()}/utils/pentbox-wlist.txt', 'r+') as f:
            wordlist = f.read().splitlines()

        for word in wordlist:
            if Hash.hash(word, algorithm) == hashed_msg:
                if print_cracked:
                    print(f"Cracked message: {word}")
                return word
        print("The provided hashed message couldn't be found in the word list!")

    @staticmethod
    def menu():
        while True:
            print("====> Hashing")
            m_choices = ['Hash a message', 'Crack a hashed message','Go back']
            terminal = TerminalMenu(m_choices)
            entry = terminal.show()
            if entry == 0:
                while True:
                    message = None
                    while message is None:
                        message = str(input("-Message to hash: "))
                    print("---choose a hashing algorithm---")
                    choices = ['0- MD5', '1- SHA1', '2- SHA256', '3- Quit']
                    terminal = TerminalMenu(choices)
                    menu_entry_index = terminal.show()
                    hashed = None
                    if menu_entry_index == 0:
                        hashed = Hash.hash(message, 'md5', True)
                    elif menu_entry_index == 1:
                        hashed = Hash.hash(message, 'sha1', True)
                    elif menu_entry_index == 2:
                        hashed = Hash.hash(message, 'sha256', True)
                    else:
                        break

                    print('Crack the hashed message ?')
                    yn_choices = ['Yes', 'No']
                    terminal = TerminalMenu(yn_choices)
                    resp = terminal.show()
                    if resp == 1:
                        print('No')
                        break
                    if menu_entry_index == 0:
                        Hash.crack_hash(hashed, 'md5', True)
                    elif menu_entry_index == 1:
                        Hash.crack_hash(hashed, 'sha1', True)
                    elif menu_entry_index == 2:
                        Hash.crack_hash(hashed, 'sha256', True)

                    print('\t------------------------')
            elif entry == 1:
                hashed = None
                while hashed is None:
                    hashed = str(input("-hashed Message: "))
                print("---choose the hashing algorithm---")
                choices = ['0- MD5', '1- SHA1', '2- SHA256', '3- Quit']
                terminal = TerminalMenu(choices)
                menu_entry_index = terminal.show()
                if menu_entry_index == 0:
                    Hash.crack_hash(hashed, 'md5', True)
                elif menu_entry_index == 1:
                    Hash.crack_hash(hashed, 'sha1', True)
                elif menu_entry_index == 2:
                    Hash.crack_hash(hashed, 'sha256', True)
                else:
                    break
            else:
                break