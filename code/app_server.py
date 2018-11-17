import falcon
import json
import v_client as vc
import hashlib
import time


ticket = {
            "activated": False,
            "appId": "sha1 of device id",
            "destination": 248,
            "line": 246,
            "origin": 268,
            "originator": 1,
            "product": 10,
            "remove": 0,
#           "validTo: UNIX time * 1000
            "validTo": 1640613608000,
            "validFrom": 1540613608000,
#           "validFrom: UNIX time * 1000
            "serial": "<two_letters>-<two_alphanumeric>:<6 numbers>",
            "sundownDate": "2025-01-01T00:00:00.000Z",
#           Any 6 unique digits
            "ticketId": 444444,
            "userId": 0,
        }

class agencyResource:
    #passthrough and strip any body
    def on_get(self, req, resp):
        try:
            a = vc.agencysync(vc.devid)
            resp.body = json.dumps(a)
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500
        print('agency-sync')

class riderResource:
    #passthrough security codes and generate everything else
    def on_put(self, req, resp):
        try:
            scode = vc.securitycodes(vc.devid)
            #Build the response
            rv = {}
            rv['notices'] = []
            rv['securityCode'] = scode
            rv['ticket'] = [ticket]
            rv['ticket'][0]['appId'] = hashlib.sha1(vc.devid).hexdigest() 
            rv['ticket'][0]['validTo'] = ((time.time() + 3550)*1000)
            rv['ticket'][0]['validFrom'] = ((time.time()-60)*1000)
            resp.body = json.dumps(rv)
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500
        print("rider-sync")

api = falcon.API()
api.add_route('/v2/agency-sync/sync', agencyResource())
api.add_route('/v2/rider/sync', riderResource())
