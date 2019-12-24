import praw

reddit = praw.Reddit(client_id = 'hbuiDmSumzodIg',
                     client_secret = 'QWH1NZVIVgv8zg1D-6iuxcyuoHs' ,
                     username = 'Munch_bot' ,
                     password = 'bot123',
                     user_agent = 'munch_botv1')

subreddit = reddit.subreddit('leagueoflegends')

hot_python = subreddit.hot(limit = 10)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}\n\nContent: {}\n\nURL {}\n\n'.format(submission.title,
                                                      submission.selftext,
                                                      submission.url))

