import socket
from cryptographic_tools.asymmetric_encryption import Asymmetric
from Crypto.PublicKey import RSA


def client1():
    priv = RSA.generate(1024)
    pub = priv.publickey()
    host = '127.0.0.1'
    port = 4005  # client1 port

    client2 = ('127.0.0.1', 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Client1 Started..")
    message = pub.exportKey(format='PEM', passphrase=None, pkcs=1)
    s.sendto(message, client2)
    data, _ = s.recvfrom(1024)
    client2_pub = RSA.importKey(data, passphrase=None)
    print("Public key Received from client2: " + client2_pub)
    message = input('-> ')
    while message != 'q':
        message = Asymmetric.rsa_encrypt(message, client2_pub)
        s.sendto(message, client2)
        data, _ = s.recvfrom(1024)
        data = Asymmetric.rsa_decrypt(data, priv)
        print("Received from client2: " + data)
        message = input("-> ")
    s.close()


if __name__ == '__main__':
    client1()