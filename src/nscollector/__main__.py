'''NS Gatherer

'''

import argparse
import gatherers
import getpass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        choices=[
            'login'
            ]
    )
    configs = parser.parse_args()
    if 'command' in configs:
        print gatherers.login(nation=raw_input('nation: '), password=getpass.getpass()).text
