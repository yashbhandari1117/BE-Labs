import numpy as np
def permute(key, p):
  s = ''
  for i in p:
    s += key[i-1]
  return s

def split(key):
  n = int(len(key) / 2)
  return key[:n], key[n:]

def combine(a, b):
  for i in b:
    a += i
  return a

def left_shift(key, n):
  s = ''
  b = list(np.zeros(len(key)))

  for i in range(len(key)):
    b[i-n] = key[i]

  for i in b:
    s += i
  
  return s

def xor(a, b):
  z = zip(a, b)
  s = ''
  for i in z:
    if i[0] == i[1]:
      s += '0'
    else:
      s += '1'
  return s

def sbox(k, s):
  S0 = [
      ['01', '00', '11', '10'], 
      ['11', '10', '01', '00'], 
      ['00', '10', '01', '11'], 
      ['11', '01', '11', '10']]

  S1 = [['00', '01', '10', '11'], 
        ['10', '00', '01', '11'], 
        ['11', '00', '01', '00'], 
        ['10', '01', '00', '11']]

  b = ('00', '01', '10', '11')
  
  if s == 'S0':
    r = b.index(k[0] + k[3])
    c = b.index(k[1] + k[2])
    return S0[r][c]
      

  elif s == 'S1':
    r = b.index(k[0] + k[3])
    c = b.index(k[1] + k[2])
    return S1[r][c]
  else:
    print(f'Invalid parameter {s}!\nParameter "s" is either S0 or S1')
    return

def swap(a, b):
  return b, a
  

# Declaring Constants

key = "0111111101"
plain_text = '10001010'

S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
IPi = (4, 1, 3, 5, 7, 2, 8, 6)

E = (4, 1, 2, 3, 2, 3, 4, 1)


# Key Generation

k = permute(key, P10)
right_half, left_half = split(k)

r = left_shift(right_half, 1)
l = left_shift(left_half, 1)
k = combine(r, l)
k1 = permute(k, P8)

r = left_shift(right_half, 2)
l = left_shift(left_half, 2)
k = combine(r, l)
k2 = permute(k, P8)

print('\nKeys Generated\n')
print(f'K1: {k1}')
print(f'K2: {k2}')

ptxt = permute(plain_text, IP)
left_half, right_half = split(ptxt)

r = permute(right_half, E)
k = xor(r, k1)
s0_part, s1_part = split(k)
s0_part = sbox(s0_part, 'S0')
s1_part = sbox(s1_part, 'S1')
k = combine(s0_part, s1_part)
k = permute(k, P4)
k = xor(k, left_half)

left_half, right_half = swap(k, right_half)

r = permute(right_half, E)
k = xor(r, k2)
s0_part, s1_part = split(k)
s0_part = sbox(s0_part, 'S0')
s1_part = sbox(s1_part, 'S1')
k = combine(s0_part, s1_part)
k = permute(k, P4)
k = xor(k, left_half)

k = combine(k, right_half)
cipher_text = permute(k, IPi)

print(f'\nCipher Text: {cipher_text}')

# Decryption

ctxt = permute(cipher_text, IP)
left_half, right_half = split(ctxt)

r = permute(right_half, E)
k = xor(r, k2)
s0_part, s1_part = split(k)
s0_part = sbox(s0_part, 'S0')
s1_part = sbox(s1_part, 'S1')
k = combine(s0_part, s1_part)
k = permute(k, P4)
k = xor(k, left_half)

left_half, right_half = swap(k, right_half)

r = permute(right_half, E)
k = xor(r, k1)
s0_part, s1_part = split(k)
s0_part = sbox(s0_part, 'S0')
s1_part = sbox(s1_part, 'S1')
k = combine(s0_part, s1_part)
k = permute(k, P4)
k = xor(k, left_half)

k = combine(k, right_half)
decrypted_text = permute(k, IPi)

print(f'\nDecrypted Text: {decrypted_text}')

print(f'\nKey: {key}\n')
print(f'K1: {k1}')
print(f'K2: {k2}')
print(f'\nPlain Text: {plain_text}')
print(f'Cipher Text: {cipher_text}')
print(f'Deciphered Text: {decrypted_text}')
