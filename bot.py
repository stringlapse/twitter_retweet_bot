import tweepy, secrets

bot_user_id = XXXXX

api = secrets.login()

mentions = api.mentions_timeline(count=5)

for mention in mentions:
    print("[NEW ] Found mention with Tweet id " + str(mention.id))

for mention in mentions:
    if mention.in_reply_to_user_id == bot_user_id:
        print("[PASS] Tweet id " + str(mention.id) + " is a reply to us")
        continue
    try:
        api.retweet(mention.id)
    except:
        print("[FAIL] We already Retweeted Tweet id " + str(mention.id))
        continue
    print("[ RT ] Successfully Retweeted Tweet id " + str(mention.id))
