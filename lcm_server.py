
import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass



sock.bind(server_address)

sock.listen(1)


while True:

    connection, client_address = sock.accept()
    try:

    
        while True:

            data = connection.recv(16)


            data_str =  data.decode('utf-8')


            if data:
                #fakeのテキストをClient側に送る。
                #最大10文字
                fake = Faker('ja_JP')
                text = fake.text(max_nb_chars=10) 
                response = text
               
                connection.sendall(response.encode())

            else:
                break

    # 最終的に接続を閉じる
    finally:
        print("Closing current connection")
        connection.close()
