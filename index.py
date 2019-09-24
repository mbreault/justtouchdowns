import nflgame
import os
from twython import Twython

def tweet(play):

    twitter = Twython(
        os.environ['TWITTER_CONSUMER_KEY'],
        os.environ['TWITTER_CONSUMER_SECRET'],
        os.environ['TWITTER_ACCESS_TOKEN'],
        os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

    twitter.update_status(status=play)
    print("Tweeted: %s" % play)

def live_callback(active, completed, diffs):

    global sleep_time
    global tweeted_plays
    sleep_time = 1

    for diff in diffs:
        for play in diff.plays:
            if "TOUCHDOWN" in str(play):
                tweet(str(play))

def main():

    try:
        nflgame.live.run(live_callback, active_interval=15,inactive_interval=900, stop=None)
    except Exception as e:
        # When an exception occurs: log it, send a message, and sleep for an
        # exponential backoff time
        print("Error occurred:")
        print(e)
        print("Sleeping for " + int(sleep_time) + " minutes")
        send_error_message(e)

        time.sleep(sleep_time * 60)
        sleep_time *= 2

if __name__ == "__main__":
    main()
