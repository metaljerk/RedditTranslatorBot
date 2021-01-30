import translators as translate
from config import reddit
from langdetect import detect

# Inspiration post
# user_text = 'ch hätte gerne, dass die Schleife jetzt mit dem Switch Befehl fortgeführt wird, da komme ich leider nicht mehr weiter. Das Ganze ist eine Schulaufgabe und ich komme nicht so richtig weiter Mit freundlichen Grüßen!'

    
for submission in reddit.subreddit('learnspanish').stream.submissions():
    user_text=submission.selftext
    try:
        language = detect(user_text)
    except Exception:
        pass
    else:
        if language != 'en':
            try:
                print(user_text)
                print(translate.google(user_text))
            except Exception:
                pass
