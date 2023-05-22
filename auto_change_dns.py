#!/usr/bin/env python3

import CloudFlare
import argparse
import sys
import pandas as pd


api_key = '####' #your cloudflare token
hostname = '###' #your subdomain 
# ip_address = '1.2.3.7'
ip_list = [] 
Number_of_subdomains = 10 #The number of domains that need to be set.
subdomains = 'mtn' # Your subdomain is determined here, for example, you can use mtn for Irancell


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-f", "--file", required=True, help="Add the file address")
    parser.add_argument("-s", "--sort", required=False, 
                        help="How are the IPs sorted? \n ads = sorted by avg_download_speed \n aus = sorted by avg_upload_speed \n adl = sorted by avg_download_latency \n aul = sorted by avg_upload_latency")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')
    args = parser.parse_args()

    print(args.file)
    readcsv = pd.read_csv(args.file) #read csv file
    print('user sort command',args.sort)
    sort = args.sort

    if sort == 'ads':
        #sorted by avg_download_speed

        readcsv.sort_values(["avg_download_speed"],axis=0, ascending=False, inplace=True, na_position='first')
        

    elif sort == 'aus':
        #sorted by avg_upload_speed
        readcsv.sort_values(["avg_upload_speed"],axis=0, ascending=False,inplace=True,na_position='first')

    elif sort == 'adl':
        #sorted by avg_download_latency
        readcsv.sort_values(["avg_download_latency"],axis=0, ascending=True,inplace=True,na_position='first')

    elif sort == 'aul':
        #sorted by avg_upload_latency
        readcsv.sort_values(["avg_upload_latency"],axis=0, ascending=True,inplace=True,na_position='first')

    else:
        #Default options is sorted by avg download speed
        readcsv.sort_values(["avg_download_speed"],axis=0, ascending=False,inplace=True,na_position='first')


    #read IPs column from CSV file
    ips = readcsv.loc[:,"ip"]
    print(f'{len(readcsv. index)} IPs were found!')
    print('add IPs to list')
    for i in ips:
        ip_list.append(i)

    # Initialize Cloudflare API client
    cf = CloudFlare.CloudFlare(
        token=api_key
    )

    # Get zone ID (for the domain). This is why we need the API key and the domain API token won't be sufficient
    zone = ".".join(hostname.split(".")[-2:]) # domain = test.mydomain.com => zone = mydomain.com
    zones = cf.zones.get(params={"name": zone})
    if len(zones) == 0:
        print(f"Could not find CloudFlare zone {zone}, please check domain {hostname}")
        sys.exit(2)
    zone_id = zones[0]["id"]


    if Number_of_subdomains > len(ip_list):
        print(len(ip_list))
        Number_of_subdomains = len(ip_list)
        print('Warning! The number of domains you entered is more than the number of IPs in the list')


    for i in range(Number_of_subdomains):

        hostname = subdomains+str(i+1) +'.'+ zone
        print(str(hostname))
        
        
        print('Fetch existing A record')
        
        try:
            

            print('Update record & save to cloudflare')
            a_record = cf.zones.dns_records.get(zone_id, params={"name": hostname, "type": "A"})[0]
            a_record["ttl"] = 1 # 1 == auto
            a_record["content"] = ip_list[i]
            cf.zones.dns_records.put(zone_id, a_record["id"], data=a_record)
            print('DNS Update!')

        except IndexError as e:
                
                dns_record ={'name': hostname, 'type':'A', 'content': ip_list[i]}

                cf.zones.dns_records.post(zone_id, data=dns_record)
                print(e)
                print('The subdomain did not exist, a new subdomain was created')
                print('DNS created!')






