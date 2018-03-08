# Imports
import requests

class Ticket:
    # ticket objects for reading ticket attributes from JSON data
    def __init__(self, dict):
        for key,value in dict.items():
	    # Data is list of lists with each list corresponding to a ticket
            if isinstance(value, (list, tuple)):
                setattr(self, key, [eachValue for eachValue in value])
            else:
                setattr(self, key,  value)


# Method for isolating tickets information from the JSON data
def getTicketData(ticketJson):
    ticketData = ticketJson.json()
    ticketText = ticketData['tickets'] 
    return ticketText


# Method for getting ticket data into a list 
def getTicketList(ticketData, ticketList):
    for ticket in ticketData:
    	newTicket = Ticket(ticket)
        ticketList.append(newTicket)
    return ticketList


# Method for JSON information for the response
def getJsonData(url, user,pwd):

    responseList = []
    try:
	# For hitting requests for multiple pages 
        while url: 
	    # HTTP request
            response = requests.get(url, auth=(user, pwd)) 
            if response.status_code == 401:
    		print "\nAuthorization error. Please check your credentials\n"
		return False
	    elif response.status_code == 404:
    		print "\nAPI not found. Please check the URL\n"
		return False
	    elif response.status_code == 503:
    		print "\nAPI unavailable. Please try after some time\n"
		return False
	    elif response.status_code == 429:
                print "\nToo many requests\n"
                responseText = response.json()
                waitTime = responseText['retry-after']
                time.sleep(int(waitTime))
                continue
	    elif response.status_code != 200:
    		return False
            else:
                responseList.append(response)
                responseText = response.json()
                url = responseText['next_page']
    except requests.exceptions.ConnectionError:
        return False

    return responseList


