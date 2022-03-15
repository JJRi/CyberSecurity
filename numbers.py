# A sceipt for CTF in https://thenixuchallenge.com/
# A challenge from 2020 "numb3rs"
#
# Date: 15 march 2022
# There are time restictions with sleep on the script, because the server gives an error if you go too fast
# Not my best work, done while suffering flu but it get the job done.
# Printing while it works is useless
# 
'''
The challenge gives you a skull banner after first connection.
The it asks you for a number, if right it asks another. If wrong you get the right answer but it closes your connection.
You have to give the right numbers in the right order. After some iterations it gives you the flag.

SO:
Receveive the banner, give right number from your database, take the correct answer to the database after you run out the right answers. Repeat until you get the flag.
'''

import socket
import time

encoding = 'ASCII'
all_numbers = [0]
counter = 0
# Make a loop to get banner and after that send numbers and receive new until error or flag



def get_banner():        
    # Get banner
        try:
            for i in range(4):
                msg = s.recv(1024)
                if msg is False:
                    break
                print(msg.decode(encoding))
                time.sleep(0.5)
        except Exception as error:
            print(f'Banner error: {error}')
            
def send_receive_nmbr():
    global all_numbers

    # Sending numbers        
    #First iteration 
    print(f'All numbers that I have: {all_numbers}')
    if all_numbers[0] != 32:
        print('first transmission!')
        s.send(b'1\r\n')
        time.sleep(0.3)
        msg = s.recv(1024)
        msg_received = msg.decode(encoding)
        print('first message:')
        print(msg_received)
        getnmbr = msg_received[:4]
        new_nmbr = ''
        for g in getnmbr:
            if g.isdigit():
                new_nmbr = new_nmbr + g    
        all_numbers[0] = int(new_nmbr)
        print(f'First iterations number: {all_numbers}')
        
        return
        
    # Main loop to iterate numbers after the first number is checked
    else:
        counter = 0
        loop_range = len(all_numbers)+1  
        for i in range(loop_range):
        #send number
            try:
                data_to_send = str(all_numbers[counter])+'\n'
            except:
                data_to_send = str(313)+'\n'
            #print(f'sending from all:{data_to_send}\n')
            s.send(data_to_send.encode('ASCII'))
            time.sleep(0.3)
            msg = s.recv(1024)
            msg_received = msg.decode(encoding)
            #print(f'received:\n{msg_received}')

            #If it asks for the next number, go to the beginning of the loop
            if 'WR0NK' not in msg_received:
                #If the flag is in the message
                if 'NIXU' in msg_received:
                    print(f'\nFlag found:\n{msg_received}')
                    exit()
                print(f'\n Going iteration: {counter}')
                counter = counter + 1
                continue
            
            #Received message that the answer was wrong
            if 'WR0NK' in msg_received:
                getnmbr = msg_received[:4]  
                #get the number from the message
                new_nmbr = ''
                for g in getnmbr:
                    if g.isdigit():
                        new_nmbr = new_nmbr + g
                # Append the number to the database of numbers
                all_numbers.append(int(new_nmbr))
                print(f'All numbers that I have are: {all_numbers}')
                return


# MAIN SCRIPT HERE:
while True:

    # Start a socket
    #AF_INET is IPv4 SOCK_STREAM is TCP
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            #TODO: You could put here gethostname
            s.connect(('52.59.208.194',1337))
            print('Connection succes!')
        except socket.error as err:
            print(f'connection error: {err}')
        #TODO: Try playing with blocking to make it faster
        s.setblocking(False)
        s.settimeout(15)

        get_banner()
        print('banner done!')
        time.sleep(0.5)
        print('sending and receiving')
        send_receive_nmbr()
       
            

        
