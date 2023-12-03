# Reconnaissance

**netdiscover**
Active/passive ARP reconnaissance tool
```SHELL
netdiscover -i eth1 -r 10.0.0.5/24
```

**Nmap**
...
# Vulnerability Scanner

**Nikto**
[https://github.com/sullo/nikto/wiki](https://github.com/sullo/nikto/wiki)  
```SHELL
nikto -h 10.0.0.7 -p 3000
```

# Scanner/Bruterforcer

**Kiterunner**
```SHELL
kr scan <target> -w <wordlist>  
kr brute <target> -w <wordlist>
```
