#split the message (file) to be encoded into blocks M1, M2, . . . , MK of l bits;
#• pad MK if necessary;
#• choose an initialization vector IV and set M0 = IV ;
#• to encrypt block Mi, compute h(K||Mi−1) and XOR it with Mi (where K
#is the secret key)
# 

import cryptography


m = open("goldplaintext.in", "r")

IV = M[0]

#cryptographically secure hash function h with output length l can be used to construct a block cipher as follows
h = cryptographySecureHashFunction()
h.outputLength = l
#construct block cipher 


### FÅ TIL DENNE OPPGAVEN, MÅL FOR 1 MAY.
