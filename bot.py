import tweepy, secrets

bot_user_id = XXXXX
rt_trigger_1 = "XXXXX"
rt_trigger_2 = "XXXXX"

api = secrets.login()

mentions = api.mentions_timeline(count=5)

for mention in mentions:
    print("[NEW ] Found mention with Tweet id " + str(mention.id))

for mention in mentions:
    if mention.in_reply_to_user_id == bot_user_id:
        print("[PASS] Tweet id " + str(mention.id) + " is a reply to us")
        continue
    if not (rt_trigger_1 in mention.full_text.lower() and rt_trigger_2 in mention.full_text.lower()):
        print("[PASS] Tweet id " + str(mention.id) + " is  missing triggers")
        continue
    try:
        api.retweet(mention.id)
    except:
        print("[FAIL] We already Retweeted Tweet id " + str(mention.id))
        continue
    print("[ RT ] Successfully Retweeted Tweet id " + str(mention.id))
