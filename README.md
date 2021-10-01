# Python script for piHole used to update the IPv6 Adresses of the local network
## Why?
### The short answer: 
**Because German (and other) ISPs suck!**  
### The long answer: 
Even tough Ipv6 gives us more adresses than we could ever need, IPv6 prefixes assigned by providers are most oftem dynamic.
Ist is fine if you don't want to adress yout local network devices via IPv6. As soon as you do that and your provider changes the Prefix all your private DNS records are wrong...
So this scripts takes the current prefix , add the static suffix (SLAAC) and writes it to the /etc/pihole/custom.list
