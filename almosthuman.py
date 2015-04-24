import slack
import slack.chat
import slack.channels
from pymarkovchain import MarkovChain
import pprint

slack.api_token = 'xoxb-4587546526-030RU1gz9TVLOVQouCf8nVE9'

with open('history.txt') as f:
    history = f.read()

mc = MarkovChain("./markov")
mc.generateDatabase(history)
msg = mc.generateString()


slack.chat.post_message('#mezzanine', msg, username='almosthuman')


#print slack.channels.history('C04AX18F5')
