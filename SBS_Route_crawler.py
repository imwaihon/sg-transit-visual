import time
import json
import urllib
import csv
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

    # Get bus route from csv file
    bus30route = []
    bus30distanceFromInterchange = []
    with open('bus30route1.csv') as csvfile:
        routeReader = csv.DictReader(csvfile)
        for row in routeReader:
            bus30route.append(str(row['StopNumber']))
            # Optional : Distance
            bus30distanceFromInterchange.append(str(row['Distance']))
    

    # Resource URL
    # Bus stop number : 30
    # 10 minutes
    with open("Bus30RouteTiming.json","w") as outfile: #Saving jsonObj["d"]
        # 10 minutes
        for i in range (1,11):
            for stopNumber in bus30route:
                urlPath = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrival?BusStopID=' + str(stopNumber) + '&ServiceNo=30'
                #Query parameters ( Lat/ Long/ Dist/ etc.)
                params = {
                    # Optional.
                }; 

                #Build query string & specify type of API call
                target = urlparse(urlPath + urllib.urlencode( params ) ) 
                #print target.geturl()
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
                jsonObj = json.loads(content)
                jsonObj['Current Time'] = time.strftime("%c")
                print json.dumps(jsonObj, sort_keys=True, indent=4)
                    #Save result to file
                json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            # 1 minute interval
            time.sleep(60.0)
    outfile.close()

