import socket
from Crypto.PublicKey import RSA

from cryptographic_tools.asymmetric_encryption import Asymmetric


def client2():
    priv = RSA.generate(1024)
    pub = priv.publickey()
    host = '127.0.0.1'
    port = 4000  # client2 port

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    client1 = ('127.0.0.1', 4005)

    print("Client2 Started")
    message = pub.exportKey(format='PEM', passphrase=None, pkcs=1)
    s.sendto(message, client1)
    data, _ = s.recvfrom(1024)
    client1_pub = RSA.importKey(data, passphrase=None)
    print("Public key Received from client1: " + client1_pub)
    while message != 'q':
        message = Asymmetric.rsa_encrypt(message, client1_pub)
        s.sendto(message.encode('utf-8'), client1)
        data, _ = s.recvfrom(1024)
        data = data.decode('utf-8')
        data = Asymmetric.rsa_decrypt(data, priv)
        print("Received from client1: " + data)
        message = input("-> ")
    s.close()


if __name__ == '__main__':
    client2()