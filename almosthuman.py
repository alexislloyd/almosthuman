import time
import random
from pymarkovchain import MarkovChain
from slackclient import SlackClient

token = "xoxb-4587546526-030RU1gz9TVLOVQouCf8nVE9"
sc = SlackClient(token)
channel = '#mezzanine'
mc = MarkovChain("./markov")
msg_count = 0

if sc.rtm_connect():
    while True:
        f = open('history.txt', 'a')
        messages = sc.rtm_read()
        rand = random.randint(5, 15)
        for msg in messages:
            if 'text' in msg:
                if "subtype" not in msg:
                    print msg['text']
                    f.write(msg['text'].encode('utf-8').strip())
                    f.write('\n')
                    f.close()
                    msg_count+=1

                    #if it's ready to respond or is directly mentioned in the previous message, send a reply
                    if msg_count == rand or '<@U04H9G2FG>' in msg['text']: 
                        with open('history.txt') as archive:
                            history = archive.read()
                        mc.generateDatabase(history)
                        archive.close()
                        comment = mc.generateString().replace('@','')
                        sc.api_call("chat.postMessage", channel=channel, text=comment, as_user=True) 
                        msg_count = 0
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"