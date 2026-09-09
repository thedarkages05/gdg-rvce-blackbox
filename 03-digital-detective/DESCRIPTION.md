## Digital Detective

Forensics triple: firmware carving, photo EXIF chain, WiFi pcap. All artifacts are static and contain a static `RVCE-...` intermediate. Pipe that intermediate to `/challenge/verify` to get your personal `/flag`.

Tools (already in `/nix` overlay, no install needed): `binwalk`, `foremost`, `exiftool`, `steghide`, `tshark`, `strings`, `dd`, `unzip`.
