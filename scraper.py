import snscrape.modules.twitter as twitterScraper
import json
name = input("Enter the User_name to scrape details: ") or "sachin_rt"
scraper = twitterScraper.TwitterProfileScraper(name)
description = []
t = scraper._get_entity()

description.append({"biography": t.description,
"follower_count": t.followersCount,
"following_count": t.friendsCount,
"likes_count": t.favouritesCount,
"user_id": t.id})

f= open("desc.json","w")
j =json.dumps(description)
f.write(j)
f.close()