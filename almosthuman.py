import slack
import slack.chat
import slack.channels
import markovgenerator
import pprint

slack.api_token = 'xoxb-4587546526-030RU1gz9TVLOVQouCf8nVE9'

with open('history.txt') as f:
    history = f.read()

markov_gen = markovgenerator.MarkovGenerator(history, 200, 3)

markov_gen.generate_words()


#slack.chat.post_message('#eng', 'Hello slackers!', username='mybot')


#print slack.channels.history('C04AX18F5')
