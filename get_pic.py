# part 1
import requests # we us this library for interaction with http protocol
import time


print(f"statrted time {start}")
url = "https://zenquotes.io/api/random"
res = requests.get(url)
re = res.json()
quote = re[0]['q']
author = re[0]['a']

payload = {
    "content": f"quote of the day:\n{quote}\n{author}"
}

dicord = "https://discord.com/api/webhooks/1162322646021714040/zeTDFjHnly0NZRfpU_hG_GTomnARmXJMVpzUYdjzHWnkXfFbQBEmaCr4k4vjcVyB4HLi"
requests.post(dicord, data=payload)
