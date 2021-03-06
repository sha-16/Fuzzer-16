#!/usr/bin/python3

import os, requests, sys
from pwn import *
from checkers import checking_target, checking_wordlist
from concurrent.futures import ThreadPoolExecutor
from banner_and_help import banner, helper
import signal 



#########################################################################################

"""
Aún estoy testeando el control de la sálida, debido a que se pierde el cursor...
Para recuperarlo ejecuta: 

    $ tput cnorm
    
Happy Hacking!

def ctrl_c(sig, frame):
    print('\n[!] Exiting...!')
    os._exit(1)

signal.signal(signal.SIGINT, ctrl_c)
"""


#########################################################################################

# Global variables for requests
# valid_status_code = [200, 301, 302, 500] 

valid_status_code = [200, 301, 302, 403, 500] 
requests_errors = 0

# Requests to the target
def make_request(word):

    url = f'{sys.argv[2]}/{word}'

    try: 
        req = requests.get(url, timeout=5)

        if req.status_code in valid_status_code: 
            print(f"\t-> {url} [Status: {req.status_code}]")

    except: 
        global requests_errors
        requests_errors += 1
        if requests_errors == 10:
            print('\n[!] Error: there are too many errors with requests, please check if your target is up!')
            os._exit(2)

#########################################################################################

# Main function to start
def main(file, target):

    # Open wordlist
    with open(file, 'r') as wordlist: 
                            
        dictionary = []
        for word in wordlist: 
            dictionary.append(word.rstrip())

        print(f"\n[*] Starting fuzz to {sys.argv[2]}")
        print('\n[~] Results:\n')
            
        # Starting process            
        with ThreadPoolExecutor(max_workers=50) as executor: 
            results = executor.map(make_request, dictionary) 

    print('\n[*] Finished...')
    sys.exit(0)

#########################################################################################

# Program presentation
if __name__ == '__main__': 

    banner()

    # Checking params
    if len(sys.argv) == 3:

        file = sys.argv[1]
        target = sys.argv[2]

        progress_testing = log.progress('Testing params')
        
        if checking_target(target) and checking_wordlist(file):

            progress_testing.success('Good!')
            main(file, target)
            
        else:
        
            progress_testing.success('Wrong!')
            print('\n[!] Error: something is wrong with the dictionary or the target...!')
            sys.exit(1)
            
    else:
        helper()
        sys.exit(0)
        
#########################################################################################
