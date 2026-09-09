#!/usr/bin/python3
import math
n=1329227995785002090679764570281989089
e=65537
c=224985365650225973530169307622688816
# TODO: Fermat - p,q close
a=math.isqrt(n)
if a*a<n: a+=1
for _ in range(200000):
    b2=a*a-n
    b=math.isqrt(b2)
    if b*b==b2:
        p=a-b; q=a+b
        print("found",p,q)
        break
    a+=1
else:
    print("not found, increase range"); raise SystemExit
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(c,d,n)
print(m.to_bytes((m.bit_length()+7)//8,"big"))
