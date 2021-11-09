import requests

# Checker functions
def checking_target(target):
    try: 
        req_test = requests.get(target, timeout=4)            
        return True
    except: 
        return False


def checking_wordlist(file):
    try: 
        with open(file, 'r') as dictionary: 
            return True
    except: 
        return False
