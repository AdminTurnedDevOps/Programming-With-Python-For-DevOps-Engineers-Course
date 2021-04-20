import sys

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def message(token, channel, mess):
    auth = WebClient(token=token)

    try:
        message = str(mess)
        auth.chat_postMessage(channel=channel, text=message)
    
    except SlackApiError as e:
        assert e.response["ok"] is False
        print(f"Received Error: {e.response['error']}")


token = sys.argv[1]
channel = sys.argv[2]
mess = sys.argv[3]


if __name__ == '__main__':
    message(token, channel, mess)