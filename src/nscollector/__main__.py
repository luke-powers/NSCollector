'''NS Gatherer

'''

import argparse
import nscollector.gatherers as gatherers
import getpass
import requests

NATION = None
SESSION = None


def get_session(nation=None, password=None):
    '''Login and return requests session object.

    '''
    global SESSION
    global NATION
    if not nation:
        NATION = input('nation: ')
    else:
        NATION = nation
    if not password:
        password = getpass.getpass()

    with requests.Session() as session:
        resp = session.post(
            'https://www.nationstates.net',
            data={'logging_in': 1, 'nation': NATION, 'password': password}
        )
        if 'Incorrect password' in resp.text:
            exit('bad login')
        else:
            SESSION = session


def main():
    global SESSION
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    configs = parser.parse_args()
    if 'command' in configs:
        if hasattr(gatherers, configs.command):
            get_session(input('Nation: '), getpass.getpass())
            getattr(gatherers, configs.command)(SESSION, NATION)
        else:
            print('unknown command: %s' % configs.command)
