import itertools

#x^32 + x^15 + x^9 + x^7 + x^4 + x^3 + 1
irr = [ 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
key = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

def bin2int(B):
    n = 0
    for i in range(len(B)):
        if B[i] == 1:
            n += (2**(len(B)-i-1))
    return n

def xor(v1,v2):
    result = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        result.append(b)
    return result

def multiplication(A,B,irr):
    result = [ ]
    for i in range(len(A)):
        result.append(0)

    for i in range(len(A)):
        if B[i] == 1:
            shift = A
            for s in range(i):
                do_we_have_overflow = (shift[-1] == 1)
                shift = [0] + shift[:-1]
                if do_we_have_overflow:
                    shift = xor(shift, irr)
            result = xor(result,shift)
    return result

def gold(P):
    return multiplication( P, multiplication(P, P, irr), irr)

def encrypt(P,K):
    ## P
    if (len(P) < 32):
        P = P + [0]*(32-len(P))
    else :
        P = P[:32]
    ## K
    if (len(K) < 32):
        K = K + [0]*(32-len(K))
    else :
        K = K[:32]
    return xor(gold(P),K)

#print(encrypt([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]))

text = "This is an example input file created specifically for the third mandatory assignment in INF143A. If you are reading this, I wish you a great Easter vacation, and good luck on the assignment!"

def text_to_binary_list(P):
    bin_list = []
    for x in P:
        z = format(ord(x), 'b')
        for y in z:
            bin_list.append(int(y))
    #print(bin_list, len(bin_list))
    return bin_list


### TESTING
#chr(84) #num to string
#print(ord("T")) #string to num
#print(format(84,'b')) #num to binary

#text_to_binary_list(text)
#print(ecb_encrypt(text,key))


#   ECB mode: encrypt the plaintext with the same key, and return the ciphertext.
def ecb_encrypt(P ,K):
    newP = text_to_binary_list(P) # turn P from a string to a list of bits
    ciphertext = []
    #count = 0
    for i in range(0, len(newP), 32):
        ciphertext.append(encrypt(newP[i:i+32], K)) # encrypt the 32 bits of P
        #count += 1
    #print(count) ## for-loop is looping 41 times which is the expected amount of blocks
    return ciphertext


#   CBC mode: encrypt the plaintext with the same key, and XOR the ciphertext with
#   the previous ciphertext block. Return the ciphertext.

def cbc_encrypt(P, K, IV):
    newP = text_to_binary_list(P) # turn P from a string to a list of bits
    ciphertext = []
    prev_ciphertext = IV
    #count = 0
    for i in range(0, len(newP), 32):
        ciphertext.append(encrypt(xor(newP[i:i+32], prev_ciphertext), K)) # encrypt the 32 bits of P
        prev_ciphertext = ciphertext[-1]
        #count += 1
    #print(count) ## for-loop is looping 41 times which is the expected amount of blocks
    return ciphertext


#function for output feedback mode(OFB) of operation
## TODO NOT IMPLEMENTED YET
def ofb_encrypt(P, K, IV):
    #Output feedback (OFB) mode of operation

    newP = text_to_binary_list(P) # turn P from a string to a list of bits
    ciphertext = []
    IV =


    return ciphertext

##TODO
# encrypt the plaintext in gold_plaintext.in with ECB, CBC and OFB.
#can take read file code from files






