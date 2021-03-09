import bcrypt

def encrypt_password(password):
    password_bin = password.encode('ascii')
    hashed = bcrypt.hashpw(password_bin, bcrypt.gensalt())
    return hashed

def confirm_password(password, hashed):
    ''' Return True if password matches, otherwise return False. '''

    if bcrypt.checkpw(password.encode('ascii'), hashed):
        return True

    return False