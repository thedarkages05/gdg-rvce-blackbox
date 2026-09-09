### Strings Lied - Don't Trust Strings

`/challenge/crackme` prints a fake flag in `strings`. The real check is an XOR loop. No source.

```bash
strings crackme | grep RVCE
ltrace ./crackme
objdump -d crackme | less
python3 -c "import subprocess;print(subprocess.check_output(['strings','crackme']).decode()[:500])"
# find xor key, run: ./crackme <key>
./crackme rvce-rocks-77
```

Real key `rvce-rocks-77` prints your personal `/flag` (binary is setuid-root, reads `/flag` only on correct key). Talk: static analysis vs dynamic.
