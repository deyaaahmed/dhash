# Hash Decrypter was coded By "7AZABET"
"""
Who is '7azabet' ?
"7AZABET" is an Ethical Programmer not a hacker, Just a poor programmer .
"""
# THE QUIETER YOU BECOME, THE MORE YOU ARE ABLE TO HEAR !

from mymodule import *
from tqdm import tqdm
from time import sleep as s


def again():
    try:
        a = input('\033[1;34mDo you wanna decrypt another hash (y/n): \033[1;33m')
        print('\033[1;31m')
        if a.lower() == 'yes' or a.lower() == 'y':
            hash_decrypter()
        elif a == "":
            print('Specify an option "yes" or "no" ?')
            again()
        else:
            print('\033[1;36mExiting, Goodbye :)')
    except Exception as ex:
        print('\033[0;91mERROR!')


def probar():
    for _ in tqdm(range(10), ascii=False, desc='Progress..', unit='it', total=10, colour='#00FFFF'):
        s(0.3)


def login():
    print(f'{R}')
    clear()
    os.system('cat banner/login_banner.txt')
    space()
    username = input(W + 'USERNAME:' + y)
    password = input(W + 'PASSWORD:' + y)
    user = "7AZABET"
    passwd = 'El Korsan'
    probar()
    if username == user and password == passwd:
        time.sleep(0.5)
        # probar()
        print(G + '\n[+] Done Successfully ^__^ ')
        time.sleep(1)

    else:
        # for _ in tqdm(range(10), ascii=False, desc='Progress..', unit='it', total=10, colour='#00FFFF'):
        #     s(0.3)
        print(R + '[!] NOT FOUND')
        exit()


login()


def hash_decrypter():
    import time
    import hashlib
    # login()  # for only test
    print('\033[1;37m')
    banner()
    print(
        f'\033[1;37m\n             ==>\033[1;31m ^__^ أهلاً بكَ فى عالمى ^__^ {W}<==\n\n\033[1;37mGive me an '
        f'encrypted word or hash and I will decrypt it\nHappy Cracking ^__^ \n')

    # word1 = input("Enter a word to hash it with 'md5' hash:")
    # res1 = hashlib.md5(word1.encode()).hexdigest()
    # print(res1)

    # word2 = input("Enter a word to hash it with 'sha1' hash:")
    # res2 = hashlib.sha1(word2.encode()).hexdigest()
    # print(res2)

    time.sleep(0.1)

    hashd_word = input('Enter the hashed word: ' + G)
    file = input(W + 'Enter the name of wordlist or press Enter to use the default wordlist: ' + G)
    if file == '':
        file = 'db.txt'
    # else:
    #     file = file
    time.sleep(0.2)
    try:
        with open(file, mode='r') as f:
            for line in f:
                line = line.strip()
                if len(hashd_word) == 32:
                    hashd_word_in_file = hashlib.md5(line.encode()).hexdigest()
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33mmd5")
                        time.sleep(0.1)
                        again()
                        break
                elif len(hashd_word) == len(hashlib.blake2b('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.blake2b(line.encode()).hexdigest()
                    type_hash = 'blake2b'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        time.sleep(0.1)
                        again()
                        break
                elif len(hashd_word) == len(hashlib.blake2s('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.blake2s(line.encode()).hexdigest()
                    type_hash = 'blake2s'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        time.sleep(0.1)
                        again()
                        break
                elif len(hashd_word) == len(hashlib.sha1('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha1(line.encode()).hexdigest()
                    type_hash = 'sha1'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha224('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha224(line.encode()).hexdigest()
                    type_hash = 'sha224'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha256('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha256(line.encode()).hexdigest()
                    type_hash = 'sha256'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha384('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha384(line.encode()).hexdigest()
                    type_hash = 'sha384'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha512('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha512(line.encode()).hexdigest()
                    type_hash = 'sha512'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break

                # hashd_word_in_file = hashlib.md5(line.encode()).hexdigest()
                # if hashd_word_in_file == hashd_word:
                #    print(f"\033[1;37m[\033[1;32m+\033[1;37m] password found: \033[1;33m{line}")
                #    time.sleep(0.1)
                #    break
                elif len(hashd_word) == len(hashlib.sha3_224('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha3_224(line.encode()).hexdigest()
                    type_hash = 'sha3_224'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha3_256('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha3_256(line.encode()).hexdigest()
                    type_hash = 'sha3_256'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha3_384('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha3_384(line.encode()).hexdigest()
                    type_hash = 'sha3_384'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.sha3_512('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha3_512(line.encode()).hexdigest()
                    type_hash = 'sha3_512'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                if len(hashd_word) == len(hashlib.sha512('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.sha512(line.encode()).hexdigest()
                    type_hash = 'sha512'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break
                elif len(hashd_word) == len(hashlib.blake2b('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.blake2b(line.encode()).hexdigest()
                    type_hash = 'blake2b'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)
                        break

                elif len(hashd_word) == len(hashlib.blake2s('test'.encode()).hexdigest()):
                    hashd_word_in_file = hashlib.blake2s(line.encode()).hexdigest()
                    type_hash = 'blake2s'
                    if hashd_word_in_file == hashd_word:
                        print(f"\033[1;37m[\033[1;32m+\033[1;37m] Password found: \033[1;33m{line}\n\033[1;37m[\033["
                              f"1;32m+\033[1;37m] Type of hash: \033[1;33m{type_hash} ")
                        again()
                        time.sleep(0.1)

            else:
                time.sleep(0.2)
                print(f'[\033[1;31m!\033[0;37m] Sorry,But your ({hashd_word}) is not match any word in the specified '
                      f'file ({file})')
    except FileNotFoundError:
        print("\033[1;37m[\033[1;31m!\033[1;37m] The specified file is not exists")
    except KeyboardInterrupt:
        space()
        print(R + 'Exit :(')
        # else:
        #     time.sleep(0.2)
        #     print(f'[\033[1;31m!\033[0;37m] Sorry,But your ({hashd_word}) is not match any word in the specified '
        #           f'file ({file})')
    # except FileNotFoundError:
    #     print("\033[1;37m[\033[1;31m!\033[1;37m] The specified file is not exists")


# while True:
hash_decrypter()
