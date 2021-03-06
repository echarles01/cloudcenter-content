#!/usr/bin/env python
import infoblox, sys, requests, os, random
requests.packages.urllib3.disable_warnings()

#Check to see if command line included enough arguments.
#if (len(sys.argv) < 3):
#	print "Usage: createHost.py <fqdn> <network CIDR>"
#	quit()

#Write environment variables to file for development purposes
f = open('/usr/local/osmosix/callout/ipam/environment', 'w')
for key in os.environ.keys():
    f.write("%s=%s\n" % (key,os.environ[key]))
f.close()

#Assign command line arguments to named variables
hostname = "worker" + str(os.getenv('eNV_JOB_ID', "-storage" + str(random.randint(1, 1000)))) # Use jobID as part of name. If not set, use 0 as default
domain = "test.com"
fqdn = hostname + "." + domain #sys.argv[1]
network = "10.110.1.0/24" #sys.argv[2]
netmask = "255.255.255.0"
gateway = "10.110.1.1"
dns_server = "10.100.1.15"

#Setup connection object for Infoblox
iba_api = infoblox.Infoblox('10.110.1.45', 'admin', 'infoblox', '1.6', 'default', 'default', False)

try:
	#Create new host record with supplied network and fqdn arguments
    ip = iba_api.create_host_record(network, fqdn)
    print "nicCount=1"
    print "nicIP_0=" + ip
    print "nicDnsServerList_0="+dns_server
    print "nicGateway_0="+gateway
    print "nicNetmask_0="+netmask
    print "linuxDomain="+domain
    print "linuxHWClockUTC=true"
    print "linuxTimeZone=Canada/Eastern"
    print "osHostname="+hostname
except Exception as e:
    print e
