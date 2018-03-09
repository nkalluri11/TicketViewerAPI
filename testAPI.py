import unittest
import requests

from ticket import*
from ticketViewer import*

# Set the HTTP request parameters for Authorized user
url1 = "https://arjunkalluri.zendesk.com/api/v2/tickets.json"
user1 = "nag11690@gmail.com"
pwd1 = "Anshika@489"

# Set the HTTP request parameters for Unauthorized user
url2 = "https://arjunkalluri.zendesk.com/XYZ.json"
user2 = "nag11690@gmail.com"
pwd2 = "Abc@abc"


# Sample tests for Authorization
class AuthorizeTestCase(unittest.TestCase):

    def testNotAuthorized(self):
        # User is not authorized
        auth2 = (user2, pwd2)
        response = requests.get(url1, auth=auth2)
        self.assertEqual(response.status_code, 401)

    def testAuthorized(self):
         # Authorized user 
         auth1 = (user1, pwd1)
         response = requests.get(url1, auth=auth1)
         self.assertEqual(response.status_code, 200)

    def testIncorrectAPI(self):
        # Incorrect API
        auth3 = (user1, pwd1)
        response = requests.get(url2, auth=auth3)
        self.assertEqual(response.status_code, 404)


# Sample tests for Ticket class
class TicketTestCase(unittest.TestCase):

    def testIDnotValid(self):
        id = 21
        url = "https://arjunkalluri.zendesk.com/api/v2/tickets/{}.json".format(id)
        response = requests.get(url, auth=(user1, pwd1))
        self.assertEqual(response.status_code, 200)

    def testIDEmpty(self):
        url = "https://arjunkalluri.zendesk.com/api/v2/tickets/{}.json".format(id)
        response = requests.get(url, auth=(user1, pwd1))
        self.assertEqual(response.status_code, 400)

    def testIDNegative(self):
        id = -17
        url = "https://arjunkalluri.zendesk.com/api/v2/tickets/{}.json".format(id)
        response = requests.get(url, auth=(user1, pwd1))
        self.assertEqual(response.status_code, 400)

    def testIDString(self):
        id = "abcd"
        url = "https://arjunkalluri.zendesk.com/api/v2/tickets/{}.json".format(id)
        response = requests.get(url, auth=(user1, pwd1))
        self.assertEqual(response.status_code, 400)

    def testGetTicketData(self):
        ticket_json = TempObject({"tickets": {"id": "11", "subject": "Test ticket", "submitter_id": "360846047774", "submitted_at": "2018-03-08T01:17:30Z"}})
        ticket = getTicketData(ticket_json)
        self.assertTrue(ticket == {"id": "11", "subject": "Test ticket", "submitter_id": "360846047774", "submitted_at": "2018-03-08T01:17:30Z"})

    def testGetTicketList(self):
        ticketData = [{"id": "11", "subject": "Test ticket", "submitter_id": "360846047774", "submitted_at": "2018-03-08T01:17:30Z"}]
        ticketList = getTicketList(ticketData, [])
        ticket = ticketList[0]
        self.assertTrue(ticket.submitter_id == "360846047774")
        self.assertTrue(ticket.id == "11")


# Temp object for mimicking the response from the HTTP request
class TempObject:

    def __init__(self, tempJson):
        self.tempJson = tempJson

    def json(self):
        return self.tempJson


# Main test method
if __name__ == '__main__':
    unittest.main()
