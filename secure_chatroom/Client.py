import socket, pickle
import threading
import time
from simple_term_menu import TerminalMenu
import rsa
from cryptographic_tools.hashing import Hash


class Client:

    def __init__(self):

        self.public_key, self.private_key = rsa.newkeys(512)

        self.id = int(input("Enter your id : "))

        host = '127.0.0.1'
        port = 4000 + self.id

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))

    def start_discussion(self):

        receiving_thread = threading.Thread(target=self.receiver)
        sending_thread = threading.Thread(target=self.sender)

        receiving_thread.start()
        sending_thread.start()

        receiving_thread.join()
        sending_thread.join()

        print("To exit the room type exit() .")

    def menu(self):

        terminal = TerminalMenu(
            ['0- Connect to another client ', '1- Wait for connection  ', '2- Go back']
        )
        entry = terminal.show()

        if entry == 0:
            self.init_handshake()
            self.start_discussion()
        elif entry == 1:
            self.wait_for_handshake()
            self.start_discussion()
        else:
            self.quit()

    def init_handshake(self):

        self.receiver_id = int(input("Enter the receiver's id : "))
        receiver_address = ('127.0.0.1', 4000 + self.receiver_id)

        print("_____________________________________________")
        print('Starting handshake...')
        self.socket.sendto(str.encode("hello"), receiver_address)  # init hello
        hello, address = self.socket.recvfrom(1024)  # waiting for hello back
        if hello.decode("utf-8") != 'hello' or address != receiver_address:
            exit()
        data, _ = self.socket.recvfrom(1024)  # waiting for public key
        self.receiver_public_key = pickle.loads(data)
        self.socket.sendto(pickle.dumps(self.public_key), receiver_address)  # send public key
        finish, _ = self.socket.recvfrom(1024)  # waiting for finish
        if finish.decode("utf-8") != 'finish':
            exit()

        print('Handshake done ...')
        self.running = True
        print('Secure connection with {id} on {address}'.format(id=self.receiver_id, address=receiver_address))
        print("_____________________________________________")

    def wait_for_handshake(self):

        print("_____________________________________________")
        print("Waiting for connection...")

        hello, receiver_address = self.socket.recvfrom(1024)  # waiting for hello

        print('Starting handshake...')
        if hello.decode("utf-8") != 'hello':
            exit()
        self.receiver_id = receiver_address[1] - 4000  # getting the other client's id
        self.socket.sendto(str.encode("hello"), receiver_address)  # hello back
        self.socket.sendto(pickle.dumps(self.public_key), receiver_address)  # send public key
        data, _ = self.socket.recvfrom(1024)  # waiting for public key
        self.receiver_public_key = pickle.loads(data)
        self.socket.sendto(str.encode("finish"), receiver_address)  # confirm finish

        print('Handshake done ...')
        self.running = True
        print('Secure connection with {id} on {address}'.format(id=self.receiver_id, address=receiver_address))
        print("_____________________________________________")

    def sender(self):

        receiver_address = ('127.0.0.1', 4000 + self.receiver_id)

        while self.running:

            message = input()

            encrypted_message = rsa.encrypt(message.encode(), self.receiver_public_key)
            signature = rsa.sign(message.encode(), self.private_key, "SHA-1")

            # sending both the encrypted message and its signature
            self.socket.sendto(encrypted_message, receiver_address)
            self.socket.sendto(signature, receiver_address)

            if message == "exit()":
                self.exit()

    def receiver(self):

        while self.running:

            # receiving both the encrypted message and its signature
            encrypted_message, _ = self.socket.recvfrom(1024)
            signature, _ = self.socket.recvfrom(1024)

            message = rsa.decrypt(encrypted_message, self.private_key)
            used_hash = rsa.verify(message, signature, self.receiver_public_key)  # verify signature

            message = message.decode("utf-8").strip()

            if used_hash != "SHA-1":
                print("error while verifying message signature : ", message)
            else:
                print("From Client {0} :".format(self.receiver_id), message)

            if message == "exit()":
                self.exit()

    def exit(self):
        print("Quitting ... Press enter to exit ")

        self.running = False
        receiver_address = ('127.0.0.1', 4000 + self.receiver_id)
        encrypted_message = rsa.encrypt("exit()".encode(), self.receiver_public_key)
        self.socket.sendto(encrypted_message, receiver_address)
        self.socket.close()
