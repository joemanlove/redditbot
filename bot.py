# import the modules
import praw

from user import user_details

# initialize with appropriate values
client_id = user_details["client_id"]
client_secret = user_details["client_secret"]
username = user_details["username"]
password = user_details["password"]
user_agent = user_details["user_agent"]

# creating an authorized reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Only allow bot to engage with private subreddit.
subreddit = reddit.subreddit('mechanicalMercs')

print("Bot is now running...")

# skip_existing makes the bot ignore old submissions to the subreddit in case of restarts
for submission in subreddit.stream.submissions(skip_existing=True):
    print(f"Processing a submission with id {submission.id}.")
    # reply with spaces removed
    if submission.selftext:
        text = submission.selftext
        no_spaces = text.replace(" ", "")
        submission.reply(f"You're wasting space, I've taken the liberty of removing it for you: \n\n{no_spaces}")
        submission.upvote()