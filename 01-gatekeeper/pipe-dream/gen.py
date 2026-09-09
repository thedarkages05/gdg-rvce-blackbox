#!/usr/bin/python3
import random, os, pathlib
flag = open("/flag").read().strip()
random.seed(flag)
attacker = f"10.{random.randint(11,99)}.{random.randint(2,254)}.{random.randint(2,254)}"
logdir = pathlib.Path("/challenge/logs")
logdir.mkdir(exist_ok=True)
# store expected for verify (root-only)
open("/tmp/.expected_ip", "w").write(attacker)
os.chmod("/tmp/.expected_ip", 0o600)
lines = []
for _ in range(20000):
    ip = f"10.{random.randint(11,99)}.{random.randint(2,254)}.{random.randint(2,254)}"
    code = random.choice(["200"]*8 + ["404", "403", "500"])
    lines.append(f"{ip} - - [09/Sep/2026] \"GET /{random.randint(1,9999)} HTTP/1.1\" {code} 512\n")
# inject attacker sequence
lines.append(f"{attacker} - - [09/Sep/2026] \"GET /admin HTTP/1.1\" 404 512\n")
lines.append(f"{attacker} - - [09/Sep/2026] \"GET /admin HTTP/1.1\" 404 512\n")
lines.append(f"{attacker} - - [09/Sep/2026] \"GET /admin HTTP/1.1\" 404 512\n")
lines.append(f"{attacker} - - [09/Sep/2026] \"GET /admin HTTP/1.1\" 200 512\n")
random.shuffle(lines)
open(logdir / "auth.log", "w").writelines(lines)
# hacker-readable
os.system("chmod -R a+r /challenge/logs")
