import requests
import requests as requests

class GenerateData():

    def __init__(self):
        self.parameters={
            "amount":10,
            "type":"boolean",
        }
        self.get_data()
        print(self.question_data)

    def get_data(self):
        self.response = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        self.response.raise_for_status()

        data = self.response.json()

        self.question_data = data['results']

lol = GenerateData()
