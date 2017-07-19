'''Nation States collector script

'''

import requests


def login(nation, password):
    '''Login and return requests session object.

    '''

    payload = {'logging_in': 1, 'nation': nation, 'password': password}

    with requests.Session() as session:
        return session.post('https://www.nationstates.net', data=payload)
