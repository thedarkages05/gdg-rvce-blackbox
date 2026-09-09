### Dean PDF - White on White

`/challenge/dean.pdf` looks clean. Select-all reveals nothing. But `strings` lies less than renderers.

```bash
file dean.pdf
strings dean.pdf | grep -i rvce
qpdf --qdf --object-streams=disable dean.pdf out.pdf; strings out.pdf | grep RVCE
exiftool dean.pdf
# white text on page 2 + deleted object both hold halves
cat halves | /challenge/verify
```

Intermediate `RVCE-PDF-DEAN-63d2`. Talk: PDF objects, `qpdf`, metadata leaks.
