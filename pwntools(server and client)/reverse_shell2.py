#!/usr/bin/env python
from pwn import *
import random

s = server(1337)
server_conn = s.next_connection()
username = server_conn.recvline().decode("utf-8").rstrip('\n')
password = server_conn.recvline().decode("utf-8").rstrip('\n')


if(username == 'root' and password == 'root'):
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)

    server_conn.sendline(bytes(str(number2),'utf-8'))
    server_conn.sendline(bytes(str(number1),'utf-8'))
    suma = str(number1 + number2)
    usersum = server_conn.recvline().decode('utf-8').rstrip('\n')
    if(usersum == suma):
        server_conn.sendline(b'Your answer was correct!')
    else:
        server_conn.sendline(b'Your answer was sadly incorrect :(')

else:
    print('invalid auth')
