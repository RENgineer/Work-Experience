#Crypt(data, initialValue) #returns byte string
#data = b'random string'
#steps = 9 #this is an integer
#initialValue=0xFFFFFFFF

import hashlib

message='random string'
data = message.encode('utf-8')
#print(data)
data2=message.encode('ascii')
#mLength=len(message)
dataLength=len(message)
#x=bin(data)
#int.from_bytes(data,byteorder='big')
#print(int(data))
key=[bin(87654321)]
key2=15
h=hex(key2)
#print(h)
y=(bin(8))
y2=(bin(7))
#print(y)
#print(y2)
#r=y^y2
#print(key)
#a = key2.to_bytes(dataLength,'little')
#print(a)
b = int.from_bytes(data,'little',signed=False)
print(b,"b")
c = bin(b)
#print(c,"c")
c2= c[2:]
print(c2,"c2") #c2 doesn't have the "0b" for binary
clen=len(c2)
clenmod=clen%4
clenexact=clen//4
print(clen, "length of c2")
print(clenexact, "clenexact")

def BinarySplit():
    n=0
    m=n+4
    i=0
    builtbin=[]
    for i in range(clenexact):
        splitmsg=c2[n:m]
        builtbin.append(splitmsg)
        n=n+4
        m=m+4
        i=i+4
        print(i,"i")
        print(builtbin)
    
    if clenmod != 0:
        xtrazero=[]
        for i in range(4-clenmod):
            if clenmod = 3
            xtrazero.append(0)
            print(xtrazero)
        #splitmsg=c2[]
                
        
        
BinarySplit()


c3 = c2[:4]
c4 = c2[4:8]
c5 = c2[8:12]
#for i = 1 to 
print (c3,c4,c5, "c3-c5")
d = hex(b)
print(d,"d")
f = bin(23)
f2 = bin(2)
f3 = bin(3)
#f4 = f2 ^ f3
print (f, f2, f3, "f sequence")
#print(f5)
#b = data.to_bytes(dataLength,'little')
#b = 10.to_bytes(4, 'little')



#hexmessage=hexdigest(data)
newmessage=hashlib.md5(data)
nm2=hashlib.md5(data2)
#print(newmessage)
#newermessage=newmessage.update(data)
h=hash(data)
newermessage=newmessage.digest()
h1=hash(newermessage)
print(newermessage) #stays the same 
#z = map(bin,bytearray(data2))
#print(z)
