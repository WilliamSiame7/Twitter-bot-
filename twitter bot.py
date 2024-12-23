import tweepy
from tkinter import *
import threading

# Credentials
consumer_key = 'FarQ187'
consumer_secret = 'Powerman@200'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def perform_actions():
    search = E1.get()
    try:
        number_of_tweets = int(E2.get())
    except ValueError:
        print("Invalid number of tweets")
        return

    phrase = E3.get()
    reply = E4.get().lower()
    retweet = E5.get().lower()
    favorite = E6.get().lower()
    follow = E7.get().lower()

    for tweet in tweepy.Cursor(api.search_tweets, q=search, lang='en').items(number_of_tweets):
        try:
            print(f'\nTweet by: @{tweet.user.screen_name}')
            if reply == "yes":
                api.update_status(
                    f"@{tweet.user.screen_name} {phrase}",
                    in_reply_to_status_id=tweet.id
                )
                print(f"Replied: {phrase}")
            if retweet == "yes":
                tweet.retweet()
                print("Retweeted")
            if favorite == "yes":
                tweet.favorite()
                print("Favorited")
            if follow == "yes":
                tweet.user.follow()
                print("Followed user")
        except tweepy.TweepError as e:
            print(f"Error: {e}")

def start_thread():
    threading.Thread(target=perform_actions, daemon=True).start()

# GUI
root = Tk()
root.title("Twitter Bot")

labels = ["Search", "Number of Tweets", "Response", "Reply?", "Retweet?", "Favorite?", "Follow?"]
entries = []

for text in labels:
    Label(root, text=text).pack()
    entry = Entry(root, bd=5)
    entry.pack()
    entries.append(entry)

E1, E2, E3, E4, E5, E6, E7 = entries

submit = Button(root, text="Submit", command=start_thread)
submit.pack(side=BOTTOM)

root.mainloop()
