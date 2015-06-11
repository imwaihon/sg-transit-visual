import time
import json
import urllib
from urlparse import urlparse
import httplib2 as http #External library 
if __name__=="__main__":
    # Parse in Account Key & User ID
    with open('apikey.txt') as fileObj:
        acckeyInfo = fileObj.readline()
        userInfo = fileObj.readline()
    accKey = acckeyInfo.split(':')[1].rstrip()
    userKey = userInfo.split(':')[1].rstrip()

    #Authentication parameters
    headers = { 'AccountKey' : accKey,
    'UniqueUserID' : userKey, 'accept' : 'application/json'} #Request results in JSON

    # Resource URL
    # Bus stop number : 30 ; Bus Stop ID = 15159
    urlPath = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival?BusStopID=15159&ServiceNo=30'
    #Query parameters ( Lat/ Long/ Dist/ etc.)
    params = {
        # Optional.
    }; 

    for i in range(1, 10):
        #Build query string & specify type of API call
        target = urlparse(urlPath + urllib.urlencode( params ) ) 
        print target.geturl()
        method = 'GET'
        body = ''
        #Get handle to http
        h = http.Http()
        #Obtain results
        response, content = h.request(
            target.geturl(),
            method,
            body,
            headers)
        #Parse JSON to print
        print (content)
        jsonObj = json.loads(content)
        print json.dumps(jsonObj, sort_keys=True, indent=4)
            #Save result to file
        with open("Bus30At15191_" + str(i) + ".json","w") as outfile: #Saving jsonObj["d"]
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
        # 1 minute interval
        time.sleep(60.0)




