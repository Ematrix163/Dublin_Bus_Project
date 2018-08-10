# -*- coding: utf-8 -*

sys.path.append('/home/student')

from weatherapi.dbconnect.py import establishConnection
import twitter



# The current schedule class is for methods that relate to the current schedule data
class TwitterAlert:

    # This method automatically initializes the class variables when an class instance is created
    def __init__(self):
        self._consumer_key = 'test'
        self._consumer_secret = 'test'
        self._access_token_key = 'test'
        self._access_token_secret = 'test'
        self.api = twitter.Api(self._consumer_key, self._consumer_secret, self._access_token_key, self._access_token_secret)
        self.tweets = None
        self.tw_dict = None
        self.tw_dict =

    def verify_credentials(self):
        print(self.api.VerifyCredentials())

    def request_timeline(self):
        self.tweets = self.api.GetUserTimeline(screen_name='dublinbusnews', count='7')

    def list_to_dictionary(self):
        self.tw_dict=[i.AsDict() for i in self.tweets]

    def display_tweets(self):
        for i in self.tw_dict:
            print(i['id'], i['text'])

    def search_tweets(self):
        for i in self.tw_dict:
            str.find(str, beg=0, end=len(string))
            print(i['id'], i['text'])



x=TwitterAlert()

x.verify_credentials()
