## Web Intrusion

Three live services on `127.0.0.1:80`. Each challenge starts its own server from `.init`. Read the source in `/challenge/app.py`, then exploit it.

Tools: `curl`, `python3`, `jwt.io`, browser devtools.

Concepts: JWT weak secrets, LFI filter bypass, SSTI. This is what `Playing with Programs -> Talking Web` goes deep on.
