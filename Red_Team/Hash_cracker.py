import hashlib
import sys
import pyfiglet
# If the program does not work try installing pyfiglet
ascii_banner = pyfiglet.figlet_format("HASH_CRACKER")
ascii_ERROR = pyfiglet.figlet_format("ERROR")
print(ascii_banner)
print('\033[94m'+"by Jerr279");

print('\033[95m' + "Types of hashes: MD5 | SHA1 | SHA224 | SHA256 | SHA384 | SHA512")
hash_type = str(input("What is the hash type? "))

wordlist_loc = str(input("wordlist location: "))
hash = str(input("input hash: "))

wordlist = open(f"{wordlist_loc}").read()
lists = wordlist.splitlines()

for word in lists:
    if hash_type == "MD5":
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")
    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")        
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")
    elif hash_type == "SHA256":
        hash_object = hashlib.sha256(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")
    elif hash_type == "SHA384":
        hash_object = hashlib.sha384(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")
    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[92m HASH FOUND: {word} \n")  
    else:
        print(ascii_ERROR)
        print("An error has occured check the sytax.")
        breakpoint