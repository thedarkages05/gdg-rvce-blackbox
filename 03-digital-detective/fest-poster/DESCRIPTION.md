### Fest Poster - Firmware Hiding in Plain Sight

8th Mile design team released `/challenge/poster.jpg` (4MB for a 200KB photo). They claim high resolution. The firmware team is laughing.

```bash
file poster.jpg
binwalk poster.jpg
binwalk -e poster.jpg
ls -R _poster.jpg.extracted/
strings poster.jpg | head -30
unzip _poster.jpg.extracted/*.zip || 7z x ...
cat inner.txt | /challenge/verify
```

`inner.txt` is a static intermediate, not your flag. `verify` exchanges it for your personal `/flag`. Every VM has the same poster but a different flag - sharing the intermediate still needs your own verify.

Tools: `binwalk -e`, `foremost`, `dd`, `strings`. Talk: supply-chain, firmware updates.
