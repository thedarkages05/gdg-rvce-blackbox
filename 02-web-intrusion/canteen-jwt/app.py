# Source for canteen-jwt. Server is /challenge/server (same logic, runs as root).
SECRET = b"canteen123"  # hidden on server, but in wordlist.txt
# token = b64url({"alg":"HS256"}) . b64url({"user":"guest","role":"user"}) . b64url(HMAC_SHA256(secret, header.payload))
# /admin verifies signature with hmac.compare_digest, checks role==admin, returns /flag
