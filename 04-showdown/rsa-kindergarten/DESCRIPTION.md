### RSA Kindergarten - Close Primes Die

`params.txt` gives `n,e,c`. `p,q` are close (diff < 100k). Standard brute force dies, Fermat lives.

```bash
cat params.txt
python3 starter.py  # broken, fix the Fermat loop
```

`starter.py` has the loop stub. Fill `a=ceil(sqrt(n))` then `b2=a*a-n` perfect-square check. Recover `p,q,d`, decrypt to intermediate, pipe to `verify`.

Intermediate is small int encoding `RVCE-RSA-...`. Talk: why real RSA needs random large primes.
