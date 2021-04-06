import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time

reddit = praw.Reddit(client_id = '4XuFDzAi1HPi6g',
client_secret = '69P1KdVI7fTMyhigtCy4EgJ3OUHjhA',
user_agent = 'console: message_bot 1.0',
username = 'johnsonphysics11',
password = 'johnson_chemistry11')

temp = Template('Hey, I was scrolling through  $subreddit and noticed your comment. There is this site called https://fan.reviews, its a site where you can leave reviews on any influencer/creator/onlyfans model, etc. You should leave a review for someone there. Its a great way to let them know if they are awesome or not so awesome. Its like Yelp for Creators.')


def check_author(author):
    
    file_read = open("comment_list.txt",'r+')
    
    for line in file_read.readlines():
        
        if line == (author + '\n'):
            
            file_read.close()
            
            return 1
    file_read.close()
    
    return 0




keywords = ['review','filter','rank']
searches = ['onlyFansModels','celebrity','influencer','models']



for search in searches:
    for submission in reddit.subreddit("all").search(search):
        
        print("online")
        message = temp.substitute({'subreddit':str(submission.subreddit)})

        
        submission.comments.replace_more(limit = 0)
        for comment in submission.comments :
           
            author = str(comment.author)
            check = check_author(author)
            if check == 1:
                
                continue
            else :
                try :
                    for keyword in keywords:
                        if keyword in comment.body:
                            check2 = check_author(author)
                            if check2 == 0:
                                print(author)
                                #reddit.redditor(author).message('Review', message)
                                print("Message sent")
                                reddit.redditor(author).message('Review', message)
                                
                                message_list = open("comment_list.txt",'a+')
                                message_list.write('\n' + author)
                                message_list.close()
                                continue
                except praw.exceptions.APIException as e:
                    if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                        print("Lol this user has a whitelist, there is no way to message them, giving up")
                        

#new loop
i = 50
while(i>0):
    for search in searches:

        print("Searching for new posts for keyword ",search)
        
        for submission in reddit.subreddit("all").search(search,sort = "new",limit=50):
            
            message = temp.substitute({'subreddit':str(submission.subreddit)})
            print("online")

            
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                
                author = str(comment.author)
                check = check_author(author)
                if check == 1:
                    
                    continue
                else :
                    try :
                        for keyword in keywords:
                            if keyword in comment.body:
                                print(comment.author)
                                #reddit.redditor(author).message('Review', message)
                                print("Message sent")
                                message_list = open("comment_list.txt",'a+')
                                message_list.write('\n' + author)
                                message_list.close()
                                continue
                    except praw.exceptions.APIException as e:
                        if e.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
                            print("Lol this user has a whitelist, there is no way to message them, giving up")
    time.sleep(600)                    

        


