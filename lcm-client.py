import socket
import sys
#ソケットに接続
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'
try:
    sock.connect(server_address)
except socket.error as err:
    #エラー確認
    print(err)
 
    sys.exit(1)

try:
    print("入力に対してランダムな文章を返します。")
    print('入力してください>>')
    message = input().encode()
    sock.sendall(message)


    sock.settimeout(1)

    try:
        while True:
            # サーバからのデータを受け取ります。
            # 受け取るデータの最大量は32バイトとします。
            data = sock.recv(32)

            # データがあればそれを表示し、なければループを終了します。
            if data:
                print('サーバーからの返信>>' + data.decode())
            else:
                break

    #タイムアウトエラー
    except(TimeoutError):
        print()

#ソケットを閉じる。
finally:
    print('closing socket')
    sock.close()
