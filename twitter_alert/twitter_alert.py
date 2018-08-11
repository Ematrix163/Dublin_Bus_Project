# -*- coding: utf-8 -*
import sys
sys.path.append('/home/student')
import MySQLdb
import mysql.connector
from mysql.connector import Error

import twitter



# The current schedule class is for methods that relate to the current schedule data
class TwitterAlert:

    # This method automatically initializes the class variables when an class instance is created
    def __init__(self):
        self._consumer_key = 'test'
        self._consumer_secret = 'test'
        self._access_token_key = 'test'
        self._access_token_secret = 'test'
        self._api = twitter.Api(self._consumer_key, self._consumer_secret, self._access_token_key, self._access_token_secret)
        self._tweets = None
        self._tw_dict = [{"id": "1", "text": "diversions on routes 12,25,63"}, {"id": "2", "text": "test test"}]
        self._lineIDs = None
        self._connection = None
        self._cursor = None
        self._feed = []

    def establish_connection(self):
        """This function connects to the mysql database on the VM"""
        while True:
            try:
                self._connection = mysql.connector.connect(host='localhost',
                                                     database='dublinBus',
                                                     user='front_end',
                                                     password='12345')
                if self._connection.is_connected():
                    print("This connection worked!")
                    self._cursor = self._connection.cursor(buffered=True)  # create cursor object - this can execute sql statments
                    break

                else:
                    print("Connection not established")

            except Error as error:
                print("ERRROR!!: ", error)
                print("will try to connect again in 25 seconds")
                sleep(25)

    def verify_credentials(self):
        print(self._api.VerifyCredentials())

    def request_timeline(self):
        self._tweets = self._api.GetUserTimeline(screen_name='dublinbusnews', count='7')

    def list_to_dictionary(self):
        self._tw_dict = [i.AsDict() for i in self._tweets]

    def display_tweets(self):
        for i in self._tw_dict:
            print(i['id'], i['text'])

    def db_line_ids(self):
        self._cursor.execute("SELECT * FROM dublinBus.routes;")
        self._lineIDs = [item[0] for item in self._cursor.fetchall()]

    def search_tweets(self):
        count_tweets = 0
        for string in self._tw_dict:
            print(string[('id')], string[('text')])
            for i in self._lineIDs:
                print(i)
                count = i in string[('text')]
                print("count: ", count)
                if count:
                    self._feed.append(i)
            count_tweets += 1

        print(self._feed)




x=TwitterAlert()
x.establish_connection()
x.db_line_ids()
x.search_tweets()
# x.verify_credentials()


