key=input("Provide the Key:- ")
key=key.replace(" ","").lower()
kset=list()
for i in key:
    if i not in kset:
        kset.append(i)
l1=list()
l2=list()
for i in kset:
    l2.append(i)
    if(len(l2)==5):
        l1.append(l2)
        l2=list()
c=97
while(c<=122):
    if(chr(c) not in kset and c!=106):
        l2.append(chr(c))
        if(len(l2)==5):
            l1.append(l2)
            l2=list()
    c+=1
for i in l1:
    print(i)
message=input("\nEnter the message:- ")
message=message.replace(" ","").lower()
print(message)
def encryption(msg):
    pairs=list()
    l=len(msg)
    i=0
    while(i<len(msg)):
        if(msg[i]!=msg[i+1]):
            pairs.append(msg[i:i+2])
        else:
            msg=msg[0:i+1]+'x'+msg[i+1:]
            pairs.append(msg[i:i+2])
        i+=2
        if(i==len(msg)-1):
            msg=msg+'x'
    print(pairs)
    ans=list()
    for x in pairs:
        dict1=dict()
        dict1={'x1':0,'y1':0,'x2':0,'y2':0}
        for i in range(5):
            for j in range(5):
                if(x[0]==l1[i][j]):
                    dict1['x1']=i
                    dict1['y1']=j
                if(x[1]==l1[i][j]):
                    dict1['x2']=i
                    dict1['y2']=j
        #print(l1[dict1['x1']][dict1['y2']]+l1[dict1['x2']][dict1['y1']])
        if(dict1['x1']==dict1['x2']):
            ans.append(l1[dict1['x1']][(dict1['y1']%4)+1]+l1[dict1['x1']][(dict1['y2']%4)+1])
        elif(dict1['y1']==dict1['y2']):
            ans.append(l1[(dict1['x1']%4)+1][dict1['y1']]+l1[(dict1['x2']%4)+1][dict1['y2']])
        else:
            ans.append(l1[dict1['x1']][dict1['y2']]+l1[dict1['x2']][dict1['y1']])
    return "".join(ans)
def decryption(msg):
    pairs=list()
    l=len(msg)
    i=0
    while(i<len(msg)):
        if(msg[i]!=msg[i+1]):
            pairs.append(msg[i:i+2])
        else:
            msg=msg[0:i+1]+'x'+msg[i+1:]
            pairs.append(msg[i:i+2])
        i+=2
        if(i==len(msg)-1):
            msg=msg+'x'
    print(pairs)
    ans=list()
    for x in pairs:
        dict1=dict()
        dict1={'x1':0,'y1':0,'x2':0,'y2':0}
        for i in range(5):
            for j in range(5):
                if(x[0]==l1[i][j]):
                    dict1['x1']=i
                    dict1['y1']=j
                if(x[1]==l1[i][j]):
                    dict1['x2']=i
                    dict1['y2']=j
        #print(l1[dict1['x1']][dict1['y2']]+l1[dict1['x2']][dict1['y1']])
        if(dict1['x1']==dict1['x2']):
            if(dict1['x1']==4 or dict1['x2']==4):
                ans.append(l1[dict1['x1']][(dict1['y1']%5)-1]+l1[dict1['x1']][(dict1['y2']%5)-1])
            else:
                ans.append(l1[dict1['x1']][(dict1['y1']%4)-1]+l1[dict1['x1']][(dict1['y2']%4)-1])
        elif(dict1['y1']==dict1['y2']):
            if(dict1['y1']==4 or dict1['y2']==4):
                ans.append(l1[(dict1['x1']%5)-1][dict1['y1']]+l1[(dict1['x2']%5)-1][dict1['y2']])
            else:
                ans.append(l1[(dict1['x1']%4)-1][dict1['y1']]+l1[(dict1['x2']%4)-1][dict1['y2']])
        else:
            ans.append(l1[dict1['x1']][dict1['y2']]+l1[dict1['x2']][dict1['y1']])
    return "".join(ans)
cipher_txt=encryption(message)
print('\nCiphertext:-',cipher_txt)
decrypted=decryption(cipher_txt)
print('\nDecrypted text:-',decrypted)

            
    

