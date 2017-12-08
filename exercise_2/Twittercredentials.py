import tweepy

consumer_key = "kcnrBVbzs90wBBjQeDh8e1JB0";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "4vWVntZpQvKQEY3vtS7R995YNVb8VSQh6xubkJTl80QzFYXzOI";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "856984298317955072-J2dOrfr2NOh2EKmZihmZavU7H5RjogZ";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "HNk8b1DqBcArRlDN4Fg0TVc3h8MQxZMWKi1wNzwijmX7t";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



