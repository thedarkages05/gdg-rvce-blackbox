### Pipe Dream - 5GB of Noise

Hostel router dumped `/challenge/logs/auth.log` (~200k lines). The attacker IP did `404,404,404,200` in that order. `cat` will hang your scrollback. Use pipes.

```bash
grep " 404 " /challenge/logs/auth.log | cut -d' ' -f1 | sort | uniq -c | sort -nr | head
grep "<suspect-ip>" /challenge/logs/auth.log | head
echo "<suspect-ip>" | /challenge/verify
```

The log is generated at boot seeded from your personal `/flag`, so every VM has a different attacker. Copy-paste from a friend fails.

Solve: `cut -d' ' -f1` extracts IP, `uniq -c` counts, second grep confirms the 200.
