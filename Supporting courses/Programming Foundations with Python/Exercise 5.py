from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1XXXXXXXX",
    from_="+1XXXXXXX",
    body="Hello from Paulina using Python!")

print(message.sid)