print('Enter two prime numbers p and q:-')
p=int(input('Enter p:-'))
q=int(input('Enter q:-'))
n=p*q
theta=(p-1)*(q-1)
def gcd(x,y):
    if(x<y):small=x
    else:small=y
    for i in range(1,small+1):
        if((x%i==0) and (y%i==0)):gcd=i
    return gcd
e=0
for i in range(2,theta):
    if(gcd(i,theta)==1):
        e=i
        break
x=1
d=0
while(1):
    if((theta*x+1)%e==0):
        d=int((theta*x+1)/e)
        break
    x+=1
pb_key=(e,n)
pv_key=(d,n)
print(e,d)
msg=int(input('Enter message number :-'))
cipher=(pow(msg,pb_key[0])%pb_key[1])
print('Ciphertext:-',cipher)
decrypt=(pow(cipher,pv_key[0])%pv_key[1])
print('Plaintext:-',decrypt)

