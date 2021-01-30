import translators as ts
from config import reddit

# Inspiration post
# user_text = 'ch hätte gerne, dass die Schleife jetzt mit dem Switch Befehl fortgeführt wird, da komme ich leider nicht mehr weiter. Das Ganze ist eine Schulaufgabe und ich komme nicht so richtig weiter Mit freundlichen Grüßen!'

    
for submission in reddit.subreddit('learnprogramming').stream.submissions():
    user_text=submission.selftext
    print(ts.google(user_text))
