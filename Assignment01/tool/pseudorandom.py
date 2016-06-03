#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PseudorandomNumGen(object):
    
    def __init__(self, key):
        self.key = key
        self.blist = self.__key2blist(self.key)
        # print(self.blist)
        # print(self.key)

    # key to bit list
    def __key2blist(seglf, key):
        length = len(key)
        blist = []
        
        i = 0
        while i < length:
            tmp_chr = ord(key[i])
            #print(tmp_chr)
            i = i + 1
            j = 8
            while j > 0:
                #print(tmp_chr)
                if tmp_chr & 0x80 == 0:
                    blist.append(0)
                else:
                    blist.append(1)
                tmp_chr = tmp_chr << 1
                j = j - 1

        return blist

    def getByte(self):
        length = len(self.blist)
        tmp_list = []

        tmp_list.append(self.blist.pop(0))
        tmp_list.append(self.blist[length-2])
        tmp_list.append(self.blist[(length-1)//2])

        self.blist.append(tmp_list[0]^tmp_list[1]^tmp_list[2])

        return tmp_list[0]^tmp_list[2]

# test
if __name__=='__main__':
    prng = PseudorandomNumGen('adfsfadfads')

    i = 1000
    while i > 0:
        print(prng.getByte())
        #print(prng.blist)
        i = i - 1
    
