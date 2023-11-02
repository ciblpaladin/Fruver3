import bcrypt


class Password:

    @staticmethod
    def encrypt(password):
        password = password.encode('utf-8')
        pass_encryp = bcrypt.hashpw(password, bcrypt.gensalt())
        return pass_encryp
    @staticmethod
    def validate_password(password_in, password_store):

        password_in = password_in.encode('utf-8')
        password_store = password_store.encode('utf')
        if(bcrypt.checkpw(password_in, password_store)):

            return True
        else:

            return False
        