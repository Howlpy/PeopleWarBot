import twitter
import time
api = twitter.Api(consumer_key="consumer key",
                  consumer_secret="consumer secret",
                  access_token_key="access token",
                  access_token_secret="token secret")

def tweetear(texto="",id=None):
    while True:
        try:
            api.PostUpdate(status=texto,in_reply_to_status_id=id)
            return True
        except Exception as e:
            print(e)
        time.sleep(15)

def status(id):
    return api.GetStatus(id)

def get_tweets():
    t = api.GetUserTimeline(screen_name="peoplewarbot", count=1)
    return t

