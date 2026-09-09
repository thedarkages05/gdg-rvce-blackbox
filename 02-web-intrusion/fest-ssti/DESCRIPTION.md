### Fest SSTI - Templates Are Code

8th Mile site greets you: `http://127.0.0.1:80/?name=you`. It concatenates your name into a template. Try math first:

```bash
curl "http://127.0.0.1:80/?name={{7*7}}"
```

If you see `49`, it evaluated you. Read `/challenge/app.py`, then escalate to `os.popen('cat /flag')` through the template sandbox (intentionally weak for teaching).

Solve chain in `solve.py`. Talk: SSTI -> RCE, why user input must never reach template engines.
