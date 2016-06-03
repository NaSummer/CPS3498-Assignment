#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tool.pseudorandom
import math
import struct

FILE_NAME_PLAINTEXT = 'mesage_decrypted.txt'
FILE_NAME_CIPHERTEXT = 'toyou'
FILE_NAME_KEY = 'key.txt'

# get 16 bytes from Rseudorandom Number Gennerator
def __get16bytes():
    i = 16
    ans = 0
    while i > 0:
        i -= 1
        ans += prng.getByte() * int(math.pow(2, i))
    return ans

# ========== main ==========
if __name__ == '__main__':

    # use key.txt as a key to implement Pseudorandom Number Generator
    key = ''
    with open(FILE_NAME_KEY, 'r', encoding='utf-8') as file_key:
        key = file_key.read()
    prng = tool.pseudorandom.PseudorandomNumGen(key)

    # open ciphertext
    with open(FILE_NAME_CIPHERTEXT, 'rb') as file_ciphertext:

        # open plaintext decrypted. if not exist, create(open() function)
        with open(FILE_NAME_PLAINTEXT, 'w', encoding='utf-8') as file_plaintext:

            # ===== open two file successfully, begin to work =====

            # flag for judging whether reaching the end of the file
            done = 0
            while not done:
                # the length of long int is 8 bits
                tmp_ciphertext = file_ciphertext.read(8)
                if (tmp_ciphertext != b''):

                    # trans bin to long int
                    index_bit = struct.unpack('L', tmp_ciphertext)

                    # XOR
                    ord_plaintext = index_bit[0] ^ __get16bytes()

                    # write file
                    file_plaintext.write(chr(ord_plaintext))

                else:
                    done = 1

            # =================== end of work ====================
