# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from threading import Thread
import socket
import sys
server_addr = ('127.0.0.1', 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
sock.sendto(my_name.encode(), server_addr)
def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(1024)
        if not data: break
        print(data.decode())

x = Thread(target=output_recvfrom, args=(sock, ))
x.start()
for line in sys.stdin:
    sock.sendto(line.strip().encode(), server_addr)
sock.close()
x.join()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
