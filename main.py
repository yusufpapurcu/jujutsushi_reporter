import praw

from dotenv import dotenv_values
config = dotenv_values(".env")  # take environment variables from .env.

reddit = praw.Reddit(
    client_id=config["BOT_ID"],
    client_secret=config["BOT_SECRET"],
    password=config["PASSWORD"],
    user_agent="macos:bot_py:v0.1 (by /u/yusufpapurcu)",
    username=config["USERNAME"],
    ratelimit_seconds=300
)

sub = reddit.subreddit("Jujutsushi")
for submission in sub.top("day", limit=5):
    print(submission.title)
