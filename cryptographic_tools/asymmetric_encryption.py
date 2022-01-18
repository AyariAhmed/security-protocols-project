import rsa
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
