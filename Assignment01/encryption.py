#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The seed for Rseudorandom Number Generator is generated by tool.keygen and stored in key.txt


import tool.keygen
import tool.pseudorandom
import math
import struct

FILE_NAME_PLAINTEXT = 'mesage.txt'
FILE_NAME_CIPHERTEXT = 'toyou'

# get 16 bytes from Rseudorandom Number Generator
def __get16bytes():
    i = 16
    ans = 0
    while i > 0:
        i -= 1
        ans += prng.getByte() * int(math.pow(2, i))
    return ans

# ========= main ==========
if __name__ == '__main__':

    # implement Rseudorandom Number Generator
    prng = tool.pseudorandom.PseudorandomNumGen(tool.keygen.KeyGen().key)

    # open plaintext
    with open(FILE_NAME_PLAINTEXT, 'r', encoding='utf-8') as file_plaintext:

        # open ciphertext(bin). if not exist, create(open() function)
        with open(FILE_NAME_CIPHERTEXT, 'wb') as file_ciphertext:

            # ===== open two file successfully, begin to work =====

            # read plaintext chr by chr
            for chr_plaintext in file_plaintext.read():

                index_chr = ord(chr_plaintext)

                # XOR
                bit_ciphertext = index_chr ^ __get16bytes()

                # change int to bin
                parsedata_ciphertext = struct.pack("L", bit_ciphertext)

                # store bin to a bin file
                file_ciphertext.write(parsedata_ciphertext)

            # =================== end of work =====================
