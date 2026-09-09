### Hostel Photo - The Photographer Lied

Missing-person case, only clue is original `/challenge/sunset.jpg`. Instagram copy has no GPS, but this is the original.

```bash
exiftool -a -G1 sunset.jpg | grep -i -E "comment|desc|thumb"
# one field is base64 - decode it, it is a password, not the flag
echo <b64> | base64 -d
# hidden file appended after JPEG EOI, protected by that password (zip)
binwalk -e sunset.jpg
# or: unzip -l sunset.jpg ; 7z l sunset.jpg
unzip -p sunset.jpg hidden.txt || python3 -c "import zipfile;print(zipfile.ZipFile('sunset.jpg').read('hidden.txt').decode())"
cat hidden.txt | /challenge/verify
```

Chain: EXIF -> password -> appended ZIP -> intermediate -> flag. Real cases never give flag in first tool. Tools: `exiftool`, `binwalk`, `strings`, `unzip`.
