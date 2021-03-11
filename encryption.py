import bcrypt

def encrypt_password(password):
    password_bin = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bin, bcrypt.gensalt())
    return hashed

def confirm_password(password, hashed):
    ''' 
    Check if password matches.

    Args:
        password: bytes string, prompt password 
        hashed: bytes string, true password
    
    Return True if password matches, otherwise return False. '''

    if bcrypt.checkpw(password, hashed):
        return True

    return False