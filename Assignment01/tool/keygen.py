#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import time

FILE_NAME_KEY = 'key.txt'

class KeyGen(object):
    
    def __init__(self):
        self.key = self.__randomKeyGen()
        self.__storeKey()
        
    #seed generator
    def __randomSeedGen(self):
        return str(time.time()*10000000)
    

    #key generator
    def __randomKeyGen(self):
        hasher = hashlib.md5()
        hasher.update(self.__randomSeedGen().encode('utf-8'))
        i = int(time.time()) % 100 + 64
        while i > 0:
            hasher.update(hasher.hexdigest().encode('utf-8'))
            i = i - 1
        return hasher.hexdigest()

    #store key to key.txt
    def __storeKey(self):
        with open(FILE_NAME_KEY,'w', encoding='utf-8') as file_key:
            file_key.write(self.key)
