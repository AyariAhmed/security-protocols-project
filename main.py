from cryptographic_tools.asymmetric_encryption import Asymmetric

pub , priv = Asymmetric.gen_elgamal_keys()

t = Asymmetric.elgamal_encrypt('ahmed',pub)
print(t)
print(Asymmetric.elgamal_decrypt(t,priv))
