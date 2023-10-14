# part 1
import requests # we us this library for interaction with http protocol
import time

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
    dicord = "https://discord.com/api/webhooks/1162322646021714040/zeTDFjHnly0NZRfpU_hG_GTomnARmXJMVpzUYdjzHWnkXfFbQBEmaCr4k4vjcVyB4HLi"
    res = requests.post(dicord, data=payload)

    return "done"
    
if __name__ == "__main__":

    quote, author = random_quote()
    send_notification(quote, author)

    print("done")

# important points:
# defining meaningful names for variables and functions
# using type hints