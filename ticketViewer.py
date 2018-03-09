# Imports
from tabulate import tabulate
from ticket import*

# Set the HTTP request parameters
url = "https://arjunkalluri.zendesk.com/api/v2/tickets.json"
user = "nag11690@gmail.com"
pwd = "Anshika@489"

# List if all the tickets
ticketList = []


# Method for connecting to API and getting the ticket information
def connect(url, user, pwd):

    pagesRemaining = False

    while pagesRemaining is False:
        responseList = getJsonData(url, user, pwd)

        # Error check
        if responseList is False:
            print "Unable to access Zendesk API\n"
            return
        else:
            global ticketList
            for response in responseList:
                ticketsData = getTicketData(response)
                ticketList = getTicketList(ticketsData, ticketList)

            print "\nSuccessfully connected to Zendesk API and downloaded tickets data\n"
            pagesRemaining = True


# Method for displaying menu items
def displayMenuItems():
    print "Please select from the following options:"
    print "* Press 1 to connect to Zendesk API"
    print "* Press 2 to display all tickets"
    print "* Press 3 to display a specific ticket"
    print "* Press 4 to quit"


# Method fpr displaying all the tickets
def displayAllTickets(ticketList):

    print "\n----------------------------------------------------------------------------------------- \n"

    tabulatedList = []

    for ticket in ticketList:
        tabulatedList.append([ticket.id, ticket.subject, ticket.submitter_id,  ticket.created_at])

    print tabulate(tabulatedList, headers=["Ticket ID", "Subject", "Submitter ID",  "Submitted at"], numalign="center", stralign="center", tablefmt="grid")

    print "\n----------------------------------------------------------------------------------------- \n"


# Method for displaying a specific ticket information
def displayIndividualTicket(ticketList):

    inputTicketNumber = raw_input("\nPlease enter the desired ticket ID: ")

    tabulatedList = []

    # Checking for a ticket in the list
    for eachTicket in ticketList:
        if str(eachTicket.id) == inputTicketNumber:

            # Displaying information
            print "\n----------------------------------------------------------------------------------------- \n"

            tabulatedList.append(["Ticket ID", str(eachTicket.id)])
            tabulatedList.append(["Subject", str(eachTicket.subject)])
            tabulatedList.append(["Submitter ID", str(eachTicket.submitter_id)])
            tabulatedList.append(["Assignee ID", str(eachTicket.assignee_id)])
            tabulatedList.append(["Priority", str(eachTicket.priority)])
            tabulatedList.append(["Status", str(eachTicket.status)])
            tabulatedList.append(["Created at", str(eachTicket.created_at)])
            tabulatedList.append(["Description", str(eachTicket.description)])

            print tabulate(tabulatedList, tablefmt="grid")

            print "\n----------------------------------------------------------------------------------------- \n"

            return

    print "\nRequested ticket could not be found \n"


# Main method
def main():
    print "\n----------------------------------------------------------------------------------------- \n"
    print "------------------------------ Welcome to Ticket Viewer ---------------------------------"
    print "\n----------------------------------------------------------------------------------------- \n"

    # Flag for exiting
    exitFlag = False

    while exitFlag is False:

        # Method to display menu items
        displayMenuItems()

        inputValue = raw_input("\nPlease enter your selection : ")

        if inputValue is "1":
            connect(url, user, pwd)
        elif inputValue is "2":
            displayAllTickets(ticketList)
        elif inputValue is "3":
            displayIndividualTicket(ticketList)
        elif inputValue is "4":
            exitFlag = True
        else:
            print "\nKindly enter a valid input\n"

    print "\n----------------------------------------------------------------------------------------- \n"
    print "---------------------------- Thank you! Have a great day! -------------------------------"
    print "\n----------------------------------------------------------------------------------------- \n"


# Entry method
if __name__ == "__main__":
    main()
