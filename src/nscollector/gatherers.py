'''Nation States collector script

'''

from bs4 import BeautifulSoup as soup

NS = "https://www.nationstates.net"


def _clean_census_objects(html_objects):
    '''Gather current census from website.

    '''
    census_titles = [
        (int(c.get('value')), c.getText().replace('Next: ', '')) for c in html_objects
    ]
    census = sorted(census_titles, key=lambda x: x[1])
    return census


def _issues_exist(issues_html):
    '''Return number of issues if there are issues else False.

    '''
    return issues_html[0].getText() if issues_html else False


def process_issues(session, nation):
    '''If there are issues available, process them based on the Previously
    Encountered Changes and the attribute weights.

    '''
    bs = soup(session.get('%s/nation=%s' % (NS, nation)).text, 'lxml')
    if _issues_exist(bs.findAll('div', {'id': 'notificationnumber-issues'})):
        bs = soup(session.get('%s/page=dilemmas' % NS).text, 'lxml')
        print(
            list(
                zip(
                    [obj.getText() for obj in bs.findAll('div', {'class': 'dpaper4'})],
                    [obj['href'] for obj in bs.findAll('a', {'class': 'dillistnpaper silentlink'})]
                )
            )
        )


def update_issue_census(session, _):
    '''Update the stored list of issue census in the database.

    '''
    bs = soup(session.get('%s/page=list_nations?censusid=0' % NS).text, 'lxml')
    print(
        [
            x[1] for x in _clean_census_objects(
                bs.findAll('select', {'name': 'censusid'})[0].findAll('option')
            )
        ]
    )
