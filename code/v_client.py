import random
import time
import hashlib
import requests
from binascii import hexlify, unhexlify


#url = "https://ventra.transitsherpa.com/v2/rider/sync"
urlbase = "https://52.0.139.197"
headerbase = {'x-gs-user-agent': '{"appVersion":"1.1.1","osVersion":"4.4.4","osType":"32bit","deviceName":"android","deviceModel":"Nexus 4","devicePlatform":"Android"}', 'content-type': 'application/json', 'x-gs-scope': 'ventra-prod'}
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
    print(securitycodes(devid))
    print(agencysync(devid))
