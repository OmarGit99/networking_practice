from pwn import *

client_conn = remote('localhost', 1337)
client_conn.sendline(b'root')
client_conn.sendline(b'root')
number1 = int(client_conn.recvline().decode("utf-8").rstrip('\n'))
number2 = int(client_conn.recvline().decode("utf-8").rstrip('\n'))

usersum = input('What is the sum of '+ str(number1)+' and '+str(number2)+'?\n')
client_conn.sendline(usersum.encode('utf-8'))

response = client_conn.recvline().decode("utf-8").rstrip('\n')
print(response)
