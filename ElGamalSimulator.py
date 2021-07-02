def ElGamal_Key_Generation():
    p = 11
    d = 3
    e1 = 2
    e2 = e1**d % p
    Public_key = [e1, e2, p]
    Private_key = d
    return Public_key, Private_key


def ElGamal_Encryption(e1, e2, p, P):
    r = 4
    c1 = e1**r % p
    c2 = P*e2**r % p
    return c1, c2


def ElGamal_Decryption(d, p, c1, c2):
    P = c2*c1**(p-1-d) % p
    return P


Plaintext = 7
print("Plaintext : ", Plaintext)

Public_key, Private_key = ElGamal_Key_Generation()
c1, c2 = ElGamal_Encryption(Public_key[0], Public_key[1], Public_key[2], Plaintext)
print("Ciphertext : (", c1, ", ", c2, ")")

p = ElGamal_Decryption(Private_key, Public_key[2], c1, c2)
print("Plaintext : ", p)
