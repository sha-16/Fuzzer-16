def banner():
    print(
"""\n 
███████╗██╗   ██╗███████╗███████╗███████╗██████╗        ██╗ ██████╗ 
██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗      ███║██╔════╝ 
█████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝█████╗╚██║███████╗ (by sha-16)
██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗╚════╝ ██║██╔═══██╗
██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║       ██║╚██████╔╝
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝ ╚═════╝                                                                             
"""
    )


def helper():
    print("[*] Use: fuzzer-16.py <wordlist> <target>")
    print("\n~ Examples: ")
    print("\n\t-> fuzzer-16.py dictionary.txt http://127.0.0.1/")
    print("\t-> fuzzer-16.py dictionary.txt http://127.0.0.1:8080/")
    print("\t-> fuzzer-16.py /usr/share/wordlist/rockyou.txt http://target-to-fuzz.com/")
