import praw
import string


subreddit_choice = str(input("Enter name of subreddit: "))
user_input = []
n = int(input("How many words do you want to search? "))# int added before input as input gives in form of string otherwise

for i in range(n):
    x = str(input("Enter word: "))
    x = x.lower()
    user_input.append(x)

print(user_input)

reddit = praw.Reddit(client_id = 'hbuiDmSumzodIg',
                     client_secret = 'QWH1NZVIVgv8zg1D-6iuxcyuoHs' ,
                     username = 'Munch_bot' ,
                     password = 'bot123',
                     user_agent = 'munch_botv1')

subreddit = reddit.subreddit(subreddit_choice)

hot_python = subreddit.hot(limit = 100)

translator = str.maketrans('','', string.punctuation)

for submission in hot_python:
    counter = 0
    if not submission.stickied:

        text = submission.selftext
        new_text = text.translate(translator)
        new_text = new_text.lower()
        words_text = new_text.split(' ')
        length = len(words_text)

        for i in range(n):
            for j in range(length):
                if (user_input[i] == words_text[j]):
                    counter += 1

            if (counter == n):
                print('Title: {}\nContent: {}\nURL {}\n'.format(submission.title,
                                                                submission.selftext,
                                                                submission.url))

