from twilio.rest import Client

#todo: hide sid, auth token and phone numbers by using airflow variables

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


def text_message(message):
    try:
        message = client.messages.create(
        to='',
        body=message,
        from_=''
        )
        print(message.sid)
    except Exception as error:
        print(str(error))

