# Python script for piHole used to update the IPv6 Adresses of the local network
## Why?
### The short answer: 
**Because German (and other) ISPs suck!**  
### The long answer: 
Even though Ipv6 gives us more adresses than we could ever need, IPv6 prefixes assigned by providers are most often dynamic.
This is fine if you don't want to adress your local network devices via IPv6. As soon as you do that and your provider changes the Prefix all your private DNS records are wrong...
So this scripts takes the current prefix and updates the /etc/pihole/custom.list config file
## Usage:
I recommend calling this script every 5 minutes using a cron job:  
`sudo crontab -e`  
and add the following:  
`*/5 * * * * python /path/to/script/dynamic_prefix.py >/dev/null 2>&1`  
You can also run it nomal as root:  
`sudo python dynamic_prefix.py`  

