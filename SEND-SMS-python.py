from twilio.rest import Client


account_sid = 'something'
auth_token = 'something'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+number',  
    to='+number',  
    body='This is a test message from Python using Twilio!'
)

print(f"✅ SMS sent! SID: {message.sid}")
