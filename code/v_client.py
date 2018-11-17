import random
import time
import hashlib
import requests
import pprint
from binascii import hexlify, unhexlify

#Change to current server IP if DNS is being spoofed
urlbase = "https://ventra.transitsherpa.com"
headerbase = {'x-gs-user-agent': '{"appVersion":"1.3.4936","osVersion":"8.0.0","osType":"32bit","deviceName":"android","deviceModel":"Nexus 6P" ,"devicePlatform":"Android"}', 'content-type': 'application/json', 'x-gs-scope': 'ventra-prod'}
devid = b'1234'

def securitycodes(deviceuuid):
    url=urlbase+"/v2/rider/sync"
    headers = headerbase
    noop_payload = '{"actions":{}}'
    hk = hashlib.sha1(deviceuuid).hexdigest()
    #Signature is not checked so why even send it?
    headers['x-gs-key'] = hk
    headers['x-gs-appid'] = hk
    headers['x-gs-timestamp'] = str(time.time()*1000)
    r = requests.put(url, headers=headers, data=noop_payload, verify=False)
    r.raise_for_status() 
    return r.json()['securityCode']

def agencysync(deviceuuid):
    url=urlbase+"/v2/agency-sync/sync"
    headers = headerbase
    hk = hashlib.sha1(deviceuuid).hexdigest()
    #Signature is not checked so why even send it?
    headers['x-gs-key'] = hk
    headers['x-gs-appid'] = hk
    headers['x-gs-timestamp'] = str(time.time()*1000)
    r = requests.get(url, headers=headers, verify=False)
    r.raise_for_status() 
    return r.json()


if __name__=='__main__':
    pprint.pprint(securitycodes(devid))
    pprint.pprint(agencysync(devid))
