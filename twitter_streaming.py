    # -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
access_token ="NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0&"
access_token_secret ="veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI&"
consumer_key = "cChZNFj6T5R0TigYB9yd1w"
consumer_secret ="L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg"
file2write=open("twitter_data.txt",'w')
i=0;
#no of tweets need to load 
no_tweets=3
lines=[]
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
   
    def on_data(self, data):
        
      
        global i
        global no_tweets
        
        if i>no_tweets:  
            return False
        else:      
            file2write.write(data)
            print("tweet %s Loaded..."%i)
            i+=1
            return True
        

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages=["en"],track=['IPL'])
    file2write.close()