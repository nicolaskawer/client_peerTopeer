import time
import socket
import struct
import threading


def convertData(messageType, subtype, data, pData=b''):
    msg = struct.pack('>bbhh', messageType, subtype, len(data) + len(pData), len(pData))
    return msg + pData + data


def getData():
    while True:
        data = sock.recv(6)
        msgtype, subtype, msglen, sublen = struct.unpack('>bbhh', data)
        msg = sock.recv(msglen)

        if msgtype == 3:
            name1, msg = msg[0:sublen], msg[sublen:]
            sender, receiver = name1.decode().split('\0')
            if name == receiver:
                print('Message from', sender, 'to', receiver, ':', msg.decode())
        else:
            print('Error', msgtype)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    ip = input('Enter IP address: ')
    port = int(input('Enter port number: '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect((ip, port))
    name = input('Enter your user name:')
    sock.send(convertData(messageType=2, subtype=1, data=name.encode()))
    threading.Thread(target=getData).start()

    while True:
        rec = input('Enter message receiver: ').strip()
        msg = input('Enter message: ').strip()
        reply = convertData(messageType=3, subtype=0, data=msg.encode(), pData=rec.encode())
        sock.send(reply)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
