import slack
import slack.channels

slack.api_token = 'xoxb-4587546526-030RU1gz9TVLOVQouCf8nVE9'
mezzanine_id = 'C04AX18F5'
f = open('history.txt', 'w')
history = slack.channels.history(mezzanine_id)


for msg in history["messages"]:
	f.write(msg["text"].encode('utf-8').strip())
	f.write('\n')