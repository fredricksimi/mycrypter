from django.shortcuts import render
from cryptography.fernet import Fernet

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()


# What do you want to do? Encrypt or Decrypt?
def home_view(request):
    return render(request, 'mainapp/index.html')

# Choose which file to encrypt/decrypt
def encdec(request):
    return render(request, 'mainapp/encdec.html')

# Enter a pass phrase that will be used as your encryption/decryption key
def pass_phrase(request):
    return render(request, 'mainapp/pass_phrase.html')

