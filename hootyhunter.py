#!/usr/bin/python3

import html
import re
from requests import get, post

# from discord_webhook import DiscordWebhook
# webhook_url = ""
# payload = "I am living in your walls, this is a threat\nHoot hoot!"
# webhook = DiscordWebhook(url=webhook_url, content=payload)
# response = webhook.execute()

# Call the get request using the 4chan API
threads = get("https://find.4chan.org/api?q=owl%20house&b=co").json()["threads"]

# Get the thread numbers for every matching thread
threads = [thread["thread"][1:] for thread in threads]

# Extract all posts from every thread matched
posts = []
for thread in threads:
    target = f"https://a.4cdn.org/co/thread/{thread}.json"
    posts += get(target).json()["posts"]

# Check each post for a regex match for the desired mega link
matches = []
for post in posts:
    # If there is no comment present in a post, skip it
    if "com" not in post: continue

    # Strip html tags and convert special chars to regular text
    comment = html.unescape(re.compile(r"<[^>]+>").sub("", post["com"]))

    # If the comment matches the regex, add it to the matches list
    if bool(re.search("mega.nz", comment)): matches.append(comment)

# TODO - Print matches found to the console
print(matches)
