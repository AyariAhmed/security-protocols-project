import hashlib
import os

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
