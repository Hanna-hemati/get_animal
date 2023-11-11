import time
import os

import requests # we us this library for interaction with http protocol


def random_quote():
    """
    This function returns a random quote from zenquotes.io 
    """
    url = "https://zenquotes.io/api/random"
    res = requests.get(url)
    re = res.json()
    quote = re[0]['q']
    author = re[0]['a']
    return quote, author

def send_notification(quote: str, author: str) -> str:
    """
    This function sends a notification to discord channel
    """
    
    payload = {
      "content": f"quote of the day:\n{quote}\n{author}\n------------"
    }
    dicord = os.getenv("WEBHOOK_URL")
    res = requests.post(dicord, data=payload)

    return "done"
    
if __name__ == "__main__":
    print("Program started...")
    
    while True:
        time.sleep(3) 
        print("sending notification")
        quote, author = random_quote()
        send_notification(quote, author)

        print("done")

# important points:
# defining meaningful names for variables and functions
# using type hints
