import random

from flask_mail import Message
from apps import App,Mongo
import string


class Utilities:
    app = App()
    mail = app.mail

    def send_email(self, email, random):
        msg = Message()
        msg.subject = "BURNOUT - Reset Password Request"
        msg.sender = 'bogusdummy123@gmail.com'
        msg.recipients = [email]
        msg.body = 'Please use the following password to login to your account: ' + random
        mongo = Mongo().mongoClient
        mongo.ath.update({'email': email}, {'$set': {'temp': random}})
        if self.mail.send(msg):
            return "success"
        else:
            return "failed"

    def get_random_string(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)
        return result_str
