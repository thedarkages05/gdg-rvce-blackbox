### Canteen WiFi - Sniffed UPI

You are given `/challenge/canteen.pcap` - 2000 packets, 99% Spotify + UPI noise. Attacker exfiltrated an intermediate three ways. Reconstruct ANY one:

```bash
tshark -r canteen.pcap -Y dns -T fields -e dns.qry.name | grep rvce | sort -u
tshark -r canteen.pcap -Y http.request -T fields -e http.file_data | strings
strings canteen.pcap | grep -i RVCE
tshark -r canteen.pcap -q -z follow,tcp,raw,0 > stream.txt; strings stream.txt | grep RVCE
echo "RVCE-PCAP-..." | /challenge/verify
```

No GUI needed. IR over SSH uses `tshark`. Wireshark GUI uses the same display filters. Talk: DNS exfil, cleartext HTTP, TCP streams.
