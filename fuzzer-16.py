#!/usr/bin/python3

import os, requests, sys
from concurrent.futures import ProcessPoolExecutor 
from pwn import *


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
timeout = 10

def checking_target(target):
    counter = True
    for i in range(2):
        try: 
            req_test = requests.get(target, timeout=timeout)            
        except: 
            counter = False
    return counter


def checking_wordlist(file):
    try: 
        with open(file, 'r') as dictionary: 
            return True
    except: 
        return False

# Requests to the target
def make_request(word):

    url = f'{sys.argv[2]}/{word}'

    try: 
        req = requests.get(url, timeout=timeout)
    
        if req.status_code in valid_status_code: 
            print(f"\t-> {url} [Status: {req.status_code}]")

    except: 
        requests_errors += 1
        if requests_errors == 10:
            print('\n[!] Error: there too many errors with requests, please check your target!')
            os.system('tput cnorm')
            os._exit(2)


# Main program
def main(file, target):

    # Open wordlist
    with open(file, 'r') as wordlist: 
                            
        dictionary = []
        for word in wordlist: 
            dictionary.append(word.rstrip())

        print(f"\n[*] Starting fuzz to {sys.argv[2]}\n")

        print('\n[~] Results:\n')

        # Starting process            
        with ProcessPoolExecutor() as executor: 
            results = executor.map(make_request, dictionary) 

        print('\n[*] Finished...')


if __name__ == '__main__': 

    banner()

    # Checking params
    if len(sys.argv) == 3:

        file = sys.argv[1]
        target = sys.argv[2]

        if checking_target(target) and checking_wordlist(file):
            main(file, target)
        else:
            print('[!] Error: something is wrong with the dictionary or the target...!')

            
    else:
        print(f"\n[*] Use: {sys.argv[0]} <wordlist> <target>")
        print("\n~ Examples: ")
        print(f"\n\t-> {sys.argv[0]} dictionary.txt http://127.0.0.1/")
        print(f"\t-> {sys.argv[0]} dictionary.txt http://127.0.0.1:8080/")
        print(f"\t-> {sys.argv[0]} /usr/share/wordlist/rockyou.txt http://target-to-fuzz.com/")
        os.system('tput cnorm')
        sys.exit(0)
        
