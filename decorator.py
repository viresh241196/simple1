user = {
    'name': 'viresh',
    "password": 'asd',
    'valid': True
}


def authentication(fun):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] and args[0]['password'] == args[1]:
            fun(*args, **kwargs)
        else:
            print('kindly login')

    return wrapper


@authentication
def message_friend(user, password):
    print('message has been sent')


message_friend(user, 'asd')
