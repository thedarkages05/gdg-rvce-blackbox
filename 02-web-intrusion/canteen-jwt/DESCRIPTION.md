### Canteen Coupons - Forge The JWT

Canteen portal on `http://127.0.0.1:80/`. It sets `token=<jwt>` with `HS256`, secret is a canteen word (`wordlist.txt` provided). `GET /` = guest, `GET /admin` = flag if `role:admin`.

```bash
curl -i http://127.0.0.1:80/
curl -i -b "token=<guest>" http://127.0.0.1:80/admin
# crack secret, forge admin, retry
/usr/bin/python3 /challenge/forge.py
```

Read `/challenge/app.py` first. Then jwt.io. Secret is in `/challenge/wordlist.txt` (200 words).

Solve: brute HMAC with wordlist, re-sign `{"user":"guest","role":"admin"}`. Talk: JWT is signed, not encrypted; weak secrets kill it.
