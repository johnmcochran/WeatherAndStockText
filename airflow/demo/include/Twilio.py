from twilio.rest import Client
import sys
import os
dag_directory = os.path.dirname(os.path.abspath(__file__))
utils_directory = os.path.join(dag_directory, 'utils')
sys.path.append(utils_directory)
sys.path.append(dag_directory)
sys.path.append(os.path.dirname(__file__))
import AWS


def text_message(message):
    try:
        twilio_account_sid = AWS.get_variable('twilio_account_sid')
        twilio_auth_token = AWS.get_variable('twilio_auth_token')
        client = Client(twilio_account_sid, twilio_auth_token)

        message = client.messages.create(
            to=AWS.get_variable('twilio_to_phone'),
            body=message,
            from_=AWS.get_variable('twilio_from_phone')
        )
        print(message.sid)
    except Exception as error:
        print(str(error))

