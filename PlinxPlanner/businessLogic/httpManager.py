import requests

API_ENDPOINT = "http://localhost:5200/api/v1/"

class Customer:
    def __init__(self, customerId):
        json_text = requests.get('http://localhost:5200/api/v1/Customer/' + customerId).json()
        self.firstname = json_text["firstName"]
        self.surname = json_text["surname"]
        self.organsiationName = json_text["companyName"] or ""
        
    def getFirstName(self):
        return self.firstname

    def getSurname(self):
        return self.surname
    
    def getOrgansiationName(self):
        return self.organsiationName

    
