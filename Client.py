import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host=socket.gethostname()
Port=1235
client.connect((Host, Port))
username = input("u joined the chat room , plz enter ur username: \n ")

def receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        if message == 'connected':

            client.send(username.encode('utf-8'))
        else:
            print(message)

def typing():
    while True:
        msg = f'{username}: {input("")}'
        client.send(msg.encode('utf-8'))

t_rec=threading.Thread(target=receive)
t_rec.start()
t_typ=threading.Thread(target=typing)
t_typ.start()