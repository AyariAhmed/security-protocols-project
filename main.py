from cryptographic_tools.symmetric_encryption import Symmetric

a = Symmetric.encrypt('Ahmed', "DES")
Symmetric.decrypt(a, "DES")
