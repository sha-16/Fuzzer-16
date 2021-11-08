#!/usr/bin/python3

import os, requests, sys, signal
from threading import Thread
from pwn import *
from tqdm.auto import tqdm


# Controling the exiting of the program
def ctrl_c(sig, frame):
    print("\n[!] Exiting...")
    os._exit(1)

signal.signal(signal.SIGINT, ctrl_c)


def banner():
    print(
        """\n 
        ███████╗██╗   ██╗███████╗███████╗███████╗██████╗        ██╗ ██████╗ 
        ██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗      ███║██╔════╝ 
        █████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝█████╗╚██║███████╗ 
        ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗╚════╝ ██║██╔═══██╗
        ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║       ██║╚██████╔╝
        ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝ ╚═════╝                                                                             
        """
    )

requests_errors = 0
valid_status_code = [200, 301, 302, 403, 500] 


def testing_request(target):
    counter = True
    for i in range(2):
        try: 
            req_test = requests.get(target, timeout=5)            
        except: 
            counter = False
    return counter


# Requests to the target
def make_request(word):

    url = f'{sys.argv[2]}/{word}'

    try: 
        req = requests.get(url, timeout=5)
    
        if req.status_code in valid_status_code: 
            print(f"\t-> {url} [Status: {req.status_code}]")

    except: 
        requests_errors += 1
        if requests_errors == 10:
            print('\n[!] Error: there too many errors with requests, please check your target!')
            os.system('tput cnorm')
            os._exit(2)


# Main program
if __name__ == '__main__': 

    banner()

    # Checking params
    if len(sys.argv) == 3:

        # Getting params     
        dic = sys.argv[1]
        target = sys.argv[2]


        if testing_request(target):
            # Open wordlist
            try:
                with open(dic, 'r') as wordlist: 
                                        
                    print(f"\n[*] Starting fuzz to {sys.argv[2]}\n")

                    thread_list = []
                    fuzz_status = log.progress('Testing')

                    print('\n[~] Results:\n')
                    
                    # Starting process            
                    for word in wordlist: 

                        fuzz_status.status(word.rstrip())

                        thread = Thread(target=make_request, args=[word.rstrip()])
                        thread.start()
                        thread_list.append(thread)


                    # Waiting for finish all of the process
                    for _ in thread_list: 
                        thread_list[-1].join()    


                    print('\n[*] Finished...')

            except:
                print("[!] Error: there are problems openning your wordlist, please check if it exists...")
                os._exit(2)

        else:
            print("[!] Error: check your target, there are problems requesting")
            os._exit(2)

            
    else:
        print(f"\n[*] Use: {sys.argv[0]} <wordlist> <target>")
        print("\n~ Examples: ")
        print(f"\n\t-> {sys.argv[0]} dictionary.txt http://127.0.0.1/")
        print(f"\t-> {sys.argv[0]} dictionary.txt http://127.0.0.1:8080/")
        print(f"\t-> {sys.argv[0]} /usr/share/wordlist/rockyou.txt http://target-to-fuzz.com/")
        os.system('tput cnorm')
        os._exit(0)
        
