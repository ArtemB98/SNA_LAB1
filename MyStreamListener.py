import tweepy

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        f = open('messages.txt', 'a')
        f.write("@%s, сообщение номер %s\n %s\n"
                % (status.author.screen_name, status.id_str,
                   status.text))
        f.close()
        print("@%s, сообщение номер %s\n %s\n"
              % (status.author.screen_name, status.id_str,
                 status.text))

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def monitoring_tweets(query, api):
        GEOBOX_SAMARA_BIG = [48.9700523344, 52.7652295668, 50.7251182524, 53.6648329274]
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth,
                                 listener=myStreamListener)
        myStream.filter(locations=GEOBOX_SAMARA_BIG)

    def task3_part3(self):
        query = [" "]
        while True:
            try:
                auth = tweepy.OAuthHandler(API_KEY,
                                           API_SECRET)
                auth.set_access_token(ACCESS_TOKEN,
                                      ACCESS_TOKEN_SECRET)
                api = tweepy.API(auth)
                MyStreamListener.monitoring_tweets(query, api)
            except Exception as error_msg: \
                    print(error_msg)