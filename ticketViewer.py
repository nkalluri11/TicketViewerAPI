# Import files
from tabulate import tabulate
from ticket import *

# Set the request parameters
url = "https://arjunkalluri.zendesk.com/api/v2/tickets.json"
user = "nag11690@gmail.com"
pwd = "Anshika@489"

# List if all the tickets 
ticketList = []

# Method for connecting to API and getting the ticket information
def connect(url, user, pwd):

    	responseList = getJsonData(url,user,pwd)

	# Error check
        if responseList == False:
            print "Unable to access Zendesk API. \n"
            return
        else:
	    global ticketList
       	    for response in responseList:
       	        ticketsData = getTicketData(response)
       	        ticketList = getTicketList(ticketsData, ticketList)


# Method for displaying menu items
def displayMenuItems():
    print "Please select from the following options:"
    print "* Press 1 to connect to Zendesk API"
    print "* Press 2 to display all tickets"
    print "* Press 3 to display a specific ticket"
    print "* Press 4 to quit"


def displayAllTickets(ticketList):

    start = 0
    end = len(ticketList)

    tabulated_list = []

    for ticket in ticketList[start:end]:
    	tabulated_list.append([ticket.id,ticket.subject,ticket.submitter_id, ticket.created_at])

    print tabulate(tabulated_list, headers=["ID","Subject","Submitter ID", "Submitted at"],tablefmt="simple") + "\n"


def displayIndividualTicket(ticketList):

    inputTicketNumber = raw_input("Enter the ticket ID: ")

    for eachTicket in ticketList:
        if str(eachTicket.id) == inputTicketNumber:

	    print "\nTicket ID: " + str(eachTicket.id)
	    print "Subject: " + str(eachTicket.subject)
	    print "Priority: " + str(eachTicket.priority)
	    print "Status: " + str(eachTicket.status)
            return

    print "No such ticket."


# Main method
def main():
    # Flag for exiting
    exitFlag = False    

    while exitFlag == False:

	# Method to display menu items
        displayMenuItems()
    	inputValue = raw_input("Enter your selection : ")

    	if inputValue == "1":
    	    connect(url, user, pwd)
    	elif inputValue == "2":
    	    displayAllTickets(ticketList)
    	elif inputValue == "3":
	    displayIndividualTicket(ticketList)
        elif inputValue == "4":
            exitFlag = True 
    	else:
            print "Kindly enter a valid input."

# Entry method        
if __name__== "__main__":
    main()




