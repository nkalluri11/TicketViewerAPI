# Imports
import requests

class Ticket:
    def __init__(self, dict):
        for key,value in dict.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [eachValue for eachValue in value])
            else:
                setattr(self, key,  value)

def getJsonData(url, user,pwd):
    responseList = []
    try:
        while url: 
            response = requests.get(url, auth=(user, pwd)) 
            if response.status_code == 401:
    		print ("Authorization error. Please check your credentials")
	    elif response.status_code == 404:
    		print ("API not found. Please check the URL")
	    elif response.status_code == 503:
    		print ("API unavailable. Please try after some time")
	    elif response.status_code == 429:
                print "Too many requests"
                responseText = response.json()
                time_to_wait = responseText['retry-after']
                time.sleep(int(time_to_wait))
                continue
            else:
                responseList.append(response)
                responseText = response.json()
                url = responseText['next_page']
    except requests.exceptions.ConnectionError:
        return False
    return responseList


def getTicketData(ticketJson):
    pass

def getTicketList(ticketData, ticketList):
    pass



