import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time



reddit = praw.Reddit(client_id = 'L0yELzFKwXc1iQ',
client_secret = 'w_tF1HhRJkei24RQwgVHTXYcfBt2RQ',
user_agent = 'console: message_bot 1.0',
username = 'holysavana',
password = '1233456')

message = "Hey babe will you enter my new sub and check my divine body XoXo? r/Divinebody"

def check_author(author):
    
    file_read = open("comment_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if line == (author + '\n'):
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0
i = 50

subreddits = ['Nudes','PetiteGoneWild']
while (i>0):
    for topic in subreddits:
        
        subreddit = reddit.subreddit(topic)
        for submission in subreddit.new(limit = 20):
            print("online")
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                author = str(comment.author)
                                
                if check_author(author) == 1 :
                    
                    continue
                else :
                    try:
                        print(comment.author)
                        #reddit.redditor(author).message('Check out my body', message)
                        
                        print("Message sent")
                                    
                        message_list = open("comment_list.txt",'a+')
                        message_list.write('\n' + author)
                        message_list.close()
                        continue
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")

    time.sleep(600)