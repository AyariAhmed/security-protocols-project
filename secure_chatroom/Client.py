import socket,pickle
import threading
import time
from simple_term_menu import TerminalMenu
import rsa

class Client:


    def __init__(self):
       
        self.public_key,self.private_key = rsa.newkeys(512)

      
        
        
        self.id=x = int(input("Enter your id : "))
                
        host = '127.0.0.1'
        port = 4000+self.id  

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))


        return

        self.receiver_id=int(input("Enter the receiver's id : "))


        receiving_thread = threading.Thread(target=self.receiving_thread)
        sending_thread = threading.Thread(target=self.sending_thread)

        receiving_thread.start()
        sending_thread.start()
        



        receiving_thread.join()
        sending_thread.join()
        



    def menu(self):

        terminal = TerminalMenu(
            ['0- Connect to another client ','1- Wait for connection  ','2- Quit' ]
        )
        entry = terminal.show()


        if entry == 0:
            self.init_handshake()
        elif entry == 1:
            self.wait_for_handshake()
        else:
            exit()

        print("mine =" ,self.public_key)
        print("his = ", self.receiver_public_key)


    def init_handshake(self):

        self.receiver_id=int(input("Enter the receiver's id : "))
        receiver_address=('127.0.0.1', 4000+self.receiver_id)
        self.socket.sendto(str.encode("hello"), receiver_address) # init hello
        hello, address = self.socket.recvfrom(1024) # waiting for hello back
        if(hello.decode("utf-8")!='hello' or address!=receiver_address):
            exit()
        data,_=self.socket.recvfrom(1024) # waiting for public key
        self.receiver_public_key=pickle.loads(data)
        self.socket.sendto(pickle.dumps(self.public_key), receiver_address) # send public key 
        finish, _ = self.socket.recvfrom(1024) # waiting for finish
        if(finish.decode("utf-8")!='finish' ):
            exit()

    def wait_for_handshake(self):
        print("waiting for connection...")
        hello, receiver_address = self.socket.recvfrom(1024) # waiting for hello
        if(hello.decode("utf-8")!='hello'):
            exit()
        self.receiver_id=receiver_address[1]-4000 # getting the other client's id 
        self.socket.sendto(str.encode("hello"), receiver_address) # hello back
        self.socket.sendto(pickle.dumps(self.public_key), receiver_address) # send public key 
        data,_=self.socket.recvfrom(1024) # waiting for public key
        self.receiver_public_key=pickle.loads(data)
        self.socket.sendto(str.encode("finish"), receiver_address) # confirm finish

    def sending_thread(self):

        receiver_address=('127.0.0.1', 4000+self.receiver_id)
    
        while True :
            message=input()
            self.socket.sendto(str.encode(message), receiver_address)



    def receiving_thread(self):

        while True :
            data, _ = self.socket.recvfrom(1024)
            print(data.decode("utf-8") )

    

    def test_thread(self):

        while True :
            time.sleep(2)
            print("test")
        

