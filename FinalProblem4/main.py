str = "MIGY MUS WIGJONYL MYWOLCNS CM U PYLS CGJILNUHN MOVDYWN NJXUS. C MUS CN CM UH YMMYHNCUF EHIQFYXAY."
i = 0
while i < 26:
    i += 1
    print(i, end='')
    print(":\t", end='')
    for char in str:
        if (ord(char)!=32)and(ord(char)!=46):
            tmp = ord(char)
            tmp += i
            if tmp > 90:
                tmp -= 26
            print(chr(tmp+32), end='')
        elif ord(char)==32:
            print(' ', end='')
        elif ord(char)==46:
            print('.', end='')
    print()
