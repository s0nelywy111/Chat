import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.137.57', 1111))
flag = True
while flag:
    request = input("Me: ")
    client.send(request.encode('utf-8'))
    if request == 'opera' or request == 'Opera':
            search = client.send(input("Enter yout request: ").encode('utf-8'))

client.close()

