import slack
import slack.channels

slack.api_token = 'xoxb-4587546526-030RU1gz9TVLOVQouCf8nVE9'
mezzanine_id = 'C04AX18F5'
f = open('history.txt', 'w')
history = slack.channels.history(mezzanine_id)
messages = history["messages"]
print len(messages)
has_more = history["has_more"]
print history
if has_more is True:
	latest = messages[-1]["ts"]
	print "getting more since"
	print ts
	more_history = slack.channels.history(mezzanine_id, latest)
	print more_history
	messages += more_history["messages"]

for msg in messages:
	if "subtype" not in msg:
		f.write(msg["text"].encode('utf-8').strip())
		f.write('\n')