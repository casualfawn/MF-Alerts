from twilio.rest import Client

class TwilioMessageManager:
    acct_token = 'a_private_key'
    acct_id = 'default user id'

    def __init__(self):
        self.twiliophone = 23042941

    def check_login(self):
        check_login = False  # placeholder
        if check_login == True:
            return 'You are authenticated'
        else:
            return 'You are not authenticated'

    def get_all_sent_messages(self):
        message_list = list('message1', 'message2')
        return message_list

    def get_messages_from_number(self, sentby_number):
        self.sentby_number = sentby_number
        msgs = twilio.get(messages, sentby_number)
        print(f"messagesfromuser")

        @classmethod
        def setauth(cls, account_id, auth_token):


            TwilioMessageManager.acct_token = auth_token
            TwilioMessageManager.account_id = account_id
            print("Auth token has been updated.")
            client = Client(account_id, auth_token)
            return client

        @classmethod
        def set_twilio_phone(cls, twilio_phone_number):
            self.twiliophone = twilio_phone_number
            TwilioMessageManager.account_id = account_id
            print("Twilio Phone has been updated.")


class TwilioMessageSender(TwilioMessageManager):

    def send_SMS(self, message, recipients):
        self.message = message
        self.sender = TwilioMessageManager.twiliophone
        self.recipients = recipients

        try:
            message = TwilioMessageManager.client.messages.create(
                to=recipients,
                from = TwilioMessageManager.twiliophone,
                body = message)


