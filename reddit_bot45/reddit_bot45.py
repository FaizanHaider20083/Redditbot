import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time

reddit = praw.Reddit(client_id = 'dZgHviGKVAV2Kw',
client_secret = '7HQadaouf7W428xNwHCjY26cbVQASw',
user_agent = 'console: message_bot 1.0',
username = 'Standard_Simp8640',
password = 'jackson_hugh11')

message = "Hey, I saw your post and I just wanted to invite you to our group on FB where we are about to give a shit ton of expert relationship and breakup advice. We also host Q/A every week! We are copy-pasting this message to you but we did read your post and think you can get a lot out of this. If you reply back, I’ll personally message you back! let me know if you want the link to it :)"

keywords = ['Help','Advice',"I don't know",'Idk','what to do','what should','anger','angry','guilt','Guilty','Fear','afraid','gaslight','gaslighting','emotional','manipulated','manipulation','narc','narcissist','codependent','codependency']

def check_author(author):
    
    file_read = open("comment_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if author in line:
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0
def check_inbox(author):
    
    file_read = open("inbox_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if author in line:
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0


i = 50

subreddits = ['relationship_advice','relationships','BreakUp','BreakUps','ExNoContact']
inbox_keywords = ['yes','yeah','sure','alright','Yes','Yeah','Sure','Alright']


while (i >0):
    for topic in subreddits:
        print("Searching through subreddits")
        subreddit = reddit.subreddit(topic)
        for submission in subreddit.new(limit = 10):
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                author = str(comment.author)
                                
                if check_author(author) == 1 :
                    print("Already sent")
                    continue
                else :
                    try:
                        for keyword in keywords:
                            if keyword in comment.body:
                                check2 = check_author(author)
                                if check2 == 0:
                                    try:
                                        print(comment.author)
                                        reddit.redditor(author).message('Relationship Counselling', message)
                                        print("Message sent")
                                                    
                                        message_list = open("comment_list.txt",'a+')
                                        message_list.write('\n' + author)
                                        
                                        message_list.close()
                                    
                                    except praw.exceptions.APIException as e:
                                        if s.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                                            print("Cant message this guy. Error 402")
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")


    #check inbox











    for item in reddit.inbox.unread(limit = None):
        print("checking inbox")
        if isinstance (item,Message):
            author = str(item.author)
            for keyword in inbox_keywords:
                if keyword in item.body:
                    check = check_inbox(author)
                    if check == 0:

                        check2 = check_inbox(author)
                        if check2 == 0:
                        
                            try:
                                print(author)
                                print("Message Sent")
                                reddit.redditor(author).message('Relationship Counselling', 'https://www.facebook.com/groups/rbmastery/ Check this, it will be worth your time.')
                            except praw.exceptions.APIException as e:
                                if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                                    print(author)
                                    print("Lol this user has a whitelist, there is no way to message them, giving up")
                            message_list = open("inbox_list.txt",'a+')
                            
                            message_list.write('\n' + author)
                            message_list.close()
                            
                            mark = [item]
                            reddit.inbox.mark_read(mark)
                            continue
    time.sleep(600)    
        



