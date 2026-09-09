# GDG RVCE: Blackbox

Incident Response orientation dojo for GDG RVCE Cybersecurity Vertical.

## Structure

- `01-gatekeeper` (3) - Own the VM: SSH, tmux, pipes, vim privesc
- `02-web-intrusion` (3) - JWT, LFI, SSTI on port 80, stdlib only
- `03-digital-detective` (3) - binwalk, exif, tshark/wireshark
- `04-showdown` (5) - Team mini-CTF (2-3 per team): git, pdf, rsa, rev, pwn

## Deploy

1. Push this folder as a GitHub repo (root must contain `dojo.yml`).
2. Go to `https://pwn.college/dojos/create` and enter `YOURUSER/gdg-rvce-blackbox`.
3. If private, add the shown Deploy Key to GitHub repo Settings > Deploy keys.
4. Test with an incognito account: Start each challenge, run the solve.
5. For the showdown, create team accounts `rvce-team01..12`, all join with password `rvce2026`.

## After extract, run once (Linux/WSL)

```bash
chmod +x */*/.init */*/verify */*/server */*/check 2>/dev/null; true
chmod 4755 04-showdown/strings-lied/crackme 04-showdown/ret2canteen/vuln 2>/dev/null; true
```

All Python SUID scripts use `#!/usr/bin/exec-suid -- /usr/bin/python3 -I` (compatible with default ubuntu:24.04 image).
All web services bind `127.0.0.1:80` and daemonize from `.init`.
Forensics use static-artifact + dynamic-verifier: artifact has static `RVCE-...` intermediate, `verify` checks it and prints real `/flag`.
