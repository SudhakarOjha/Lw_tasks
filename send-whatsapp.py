from twilio.rest import Client

account_sid = '-----------------------'# twilio account_sid
auth_token = '----------------------------'#authentication mumber of twilio

client = Client(account_sid, auth_token)


from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio Sandbox number
to_whatsapp_number = 'whatsapp:+919057892972'   # Your verified number

message = client.messages.create(
    body="Hello Sudhakar!  WhatsApp message via Twilio Sandbox is working!",
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"WhatsApp message sent successfully! SID: {message.sid}")
