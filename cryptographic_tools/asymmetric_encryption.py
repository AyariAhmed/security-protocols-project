import rsa
from simple_term_menu import TerminalMenu
from elgamal import elgamal


class Asymmetric:

    @staticmethod
    def gen_rsa_keys():
        """Returns a tuple of (pubkey,privkey)"""
        return rsa.newkeys(512)

    @staticmethod
    def gen_elgamal_keys():
        """Returns a tuple of (pubkey,privkey)"""
        keys = elgamal.generate_keys(128)
        return keys["publicKey"], keys["privateKey"]

    @staticmethod
    def rsa_encrypt(data, pubkey):
        return rsa.encrypt(data.encode(), pubkey).hex()

    @staticmethod
    def rsa_decrypt(data, privkey):
        return rsa.decrypt(bytes.fromhex(data), privkey).decode("utf-8").strip()

    @staticmethod
    def elgamal_encrypt(data, pubkey):
        return elgamal.encrypt(pubkey, data)

    @staticmethod
    def elgamal_decrypt(data, privkey):
        return elgamal.decrypt(privkey, data)

    @staticmethod
    def menu():
        while True:
            print("====> Asymmetric Encryption")
            m_choices = ['RSA', 'Elgamal', 'Go back']
            terminal = TerminalMenu(m_choices)
            entry = terminal.show()
            if entry == 0:
                print('generating RSA pair of keys...')
                pub, priv = Asymmetric.gen_rsa_keys()
                message = None
                while message is None:
                    message = str(input("-Message to encrypt: "))
                print(f'Encrypting the message using the public key: {pub}')
                encrypted = Asymmetric.rsa_encrypt(message, pub)
                print(f'Encrypted message: {encrypted}')
                print('Proceeding to decryption using the private key...')
                decrypted = Asymmetric.rsa_decrypt(encrypted, priv)
                print(f'Decrypted message: {decrypted}')
                print('\t------------------------')
            elif entry == 1:
                print('generating Elgamal pair of keys...')
                pub, priv = Asymmetric.gen_elgamal_keys()
                message = None
                while message is None:
                    message = str(input("-Message to encrypt: "))
                print(f'Encrypting the message using the public key: {pub}')
                encrypted = Asymmetric.elgamal_encrypt(message, pub)
                print(f'Encrypted message: {encrypted}')
                print('Proceeding to decryption using the private key...')
                decrypted = Asymmetric.elgamal_decrypt(encrypted, priv)
                print(f'Decrypted message: {decrypted}')
                print('\t------------------------')
            else:
                break
