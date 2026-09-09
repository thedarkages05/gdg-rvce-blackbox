### Git Grave - Fest Site Never Forgets

Clone is already at `/challenge/site/`. Flag was deleted 3 commits ago but git never forgets.

```bash
cd /challenge/site
git log --all --oneline
git log -p -S RVCE | head -100
git show HEAD~3:secret.txt
cat secret.txt | /challenge/verify
```

Talk: `.git` exposure, GitHub dorks, `git reflog`, force-push does not delete.
