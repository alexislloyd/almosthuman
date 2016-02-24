import time
import random
from pymarkovchain import MarkovChain
from slackclient import SlackClient
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    token = cfg['slack']['token']
    print token

sc = SlackClient(token)
channel = '#mezzanine'
mc = MarkovChain("./markov")
msg_count = 0
rand = random.randint(4, 10)
print rand

if sc.rtm_connect():
    while True:
        messages = sc.rtm_read()
        for msg in messages:
            if 'text' in msg:
                if "subtype" not in msg:
                    print msg['text']
                    f = open('history.txt', 'a')
                    f.write(msg['text'].encode('utf-8').strip())
                    f.write('\n')
                    f.close()
                    msg_count = msg_count + 1

                    #if it's ready to respond or is directly mentioned in the previous message, send a reply
                    if msg_count == rand or '<@U04H9G2FG>' in msg['text']: 
			print "posting a message"
                        with open('history.txt') as archive:
                            history = archive.read()
                        mc.generateDatabase(history)
                        archive.close()
                        comment = mc.generateString().replace('<@U03QPG6U1>','')
                        sc.api_call("chat.postMessage", channel=channel, text=comment, as_user=True) 
                        msg_count = 0
			print "new random"
			rand = random.randint(5, 15)
			print rand
                    else:
                        print "no match between %d and %d" % (rand, msg_count)
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
