import socket
import time

HOST = socket.gethostname()
PORT = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'''{"type": "login", "StudentNum": "1234", "password": "1234"}''')
r = s.recv(1024)
print(r)
s.close()
s.connect((HOST, PORT))
r = s.recv(1024)
print(r)
s.close()
time.sleep(5)
s.connect((HOST, PORT))
s.send(b'{"type":"postOrder","Taddress":"yangbojia","Gaddress":"YANGBOJIA","Item":"YANGBO","Time":"30","phoneNum":"1234","StudentNum":"2018081301007"}')
r = s.recv(1024)
print(r)
s.close()
time.sleep(5)
s.connect((HOST, PORT))
s.send(b'{"type":"postOrder","Taddress":"yangbojia","Gaddress":"YANGBOJIA","Item":"YANGBO","Time":"30","phoneNum":"1234","StudentNum":"2018081301007"}')
r = s.recv(1024)
print(r)
s.close()
time.sleep(5)
time.sleep(5)
s.connect((HOST, PORT))
s.send(b'{"type":"cancelTicket", "TicketNum":"202011221721517307"}')
r = s.recv(1024)
print(r)
s.close()
