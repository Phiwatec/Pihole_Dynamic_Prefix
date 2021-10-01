
import requests
#Get own IP adress
r = requests.get('https://www.trackip.net/ip')
#Check if request was okay and adress is IPv6
if r.status_code != 200 :
    exit("ERROR: Can't get IP adress please check internet connection")
if "." in r.text :
    print("ERROR: Got IPv4 adress: Make shure you have IPv6 internet access")
#function for seperating the prefix part from the host part
def getPrefix(ip):
    ip=ip.split(":")
    ret_ip=""
    for i in range(0,4):
        ret_ip+=ip[i]+':'
    return ret_ip

#Get prefix from own IP adress
new_prefix=getPrefix(r.text)

#reaad config file
config_file = open("custom.list", "r")
config_file_content=config_file.read()
config_file.close()

#Find first occurrence of a IPv6 adress in config file and get the old prefix
config_file_list=config_file_content.split("\n")

for  line in config_file_list:
    if ':' in line:
        old_prefix=getPrefix(line)
        break

#Print the old and new prefix 
print("Old prefix: "+old_prefix)
print("New Prefix: "+new_prefix)

#Check if prefix changed
if old_prefix == new_prefix:
    print("Prefix didn't change. Exiting")
    exit()

#Update config file 
config_file_content=config_file_content.replace(old_prefix,new_prefix)

#Write new configuration to file
config_file = open("custom.list", "w")
config_file.write(config_file_content)
config_file.close()

#Smile
print("Wrote config file successfully :)")



