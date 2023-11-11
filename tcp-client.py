import socket

IP = input("Server address: ")
TCP_PORT = 5000  # 포트 번호를 5000으로 변경
BUFFER_SIZE = 1024

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, TCP_PORT))
            MESSAGE = input('Write to server: ')

            if MESSAGE == 'q':
                break

            s.send(MESSAGE.encode('utf-8'))
            print('Sending data:', MESSAGE)
            data = s.recv(BUFFER_SIZE)
            print('Data from server:', data.decode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")
        break


# import socket
#
# IP = input("Server address: ")
# TCP_PORT = 5005
# BUFFER_SIZE = 1024
# MESSAGE = ''
#
# while True:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((IP, TCP_PORT))
#     MESSAGE = input('Write to server : ')
#     if(MESSAGE=='q'):
#         break
#     s.send(MESSAGE.encode('utf-8'))
#     print('Sending data:', MESSAGE)
#     data = s.recv(BUFFER_SIZE)
#     print('Data from server:', data.decode('utf-8'))
#
#
# s.close()
