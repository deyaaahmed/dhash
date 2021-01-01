import hashlib
#print(dir(hashlib))
print(hashlib.blake2s(input('Enter a word to encrypt it (blake2s):').encode()).hexdigest())
print(hashlib.blake2b(input('Enter a word to encrypt it (blake2b):').encode()).hexdigest())
print(hashlib.sha512(input('Enter a word to encrypt it (sha512):').encode()).hexdigest())
print(hashlib.md5(input('Enter a word to encrypt it (md5):').encode()).hexdigest())
print(hashlib.sha224(input('Enter a word to encrypt it (sha224):').encode()).hexdigest())
