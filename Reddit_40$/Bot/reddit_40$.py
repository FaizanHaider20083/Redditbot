import praw
import time

reddit = praw.Reddit(client_id = '4Y-ybqnRtI3Xog',
                     client_secret = 'NzTLmfzHxZjsq-XYHaf_I-ySysjGnw',
                     user_agent = 'console: flairbot 1.0')
                     


string = " "
comment_author = []



#functiom to follow subreddit
def follow_subreddit():
    global string
    print("Enter the name of the subreddit you want to follow :")

    string = input()
    return string


subreddit = reddit.subreddit("television")

for submission in subreddit.new(limit = 10):
    print ("..........................")
    print(submission.title)
    for comment in submission.comments:
        
        if hasattr(comment,"body"):
           comment_author.append(comment.author)
    d = dict.fromkeys(comment_author,0)
    for i in comment_author:
        d[i]+=1
    for k in comment_author:
        if d[k] >= 5:
            
