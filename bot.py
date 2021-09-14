import requests
import json
def post_message(channel, text): 
    SLACK_BOT_TOKEN = "xoxb-2264595263921-2485079350275-K8JaJI8y5cqHBi8u96ZzrmnB"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
        }
    payload = {
        'channel': channel,
        'text': text
        }
    r = requests.post('https://slack.com/api/chat.postMessage', 
        headers=headers, 
        data=json.dumps(payload)
        )
if __name__ == '__main__':
    post_message("#thundervalley", "pip install sojung")


