# -*- coding: utf-8 -*-
import hashlib
import base58
print("Bienvenue dans mnemobit")
input = "Quand je serai grand je serai toto le heros"
hashkey = hashlib.sha256(input.encode('utf-8'))
key = "\x80" + hashkey.digest()
print(hashkey.hexdigest())
#key="80"+hashkey.hexdigest()
#print(key)
firstsha = hashlib.sha256(key)
print(firstsha.hexdigest())
print("----")
print(firstsha.digest())
secondsha = hashlib.sha256(firstsha.digest())
print(secondsha.digest())
print(secondsha.hexdigest())
checksum = hashlib.sha256(hashlib.sha256(key).digest()).hexdigest()[0:8]
print(checksum)
check =  hashlib.sha256(hashlib.sha256(key).digest()).digest()[0:4]
final="80"+hashkey.hexdigest()+checksum
print(final)
key=key+check
print(base58.b58encode(key))
#80d0db30825d32e8bdcd55016f1f9de4d2115e5252476318f9201baa3a0814e6c1ac186ff3
#print(base58.b58encode_check(key))
