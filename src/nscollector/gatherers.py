'''Nation States collector script

'''

from bs4 import BeautifulSoup as soup

NS = "https://www.nationstates.net"


def _extract_text(bs_obj):
    txt = bs_obj.getText()
    if 'Next:' in txt:
        txt = txt.split('Next: ')[1]
    return txt


def _gather_current_census(session):
    '''Gather current census from website.

    '''
    bs = soup(session.get('%s/page=list_nations?censusid=0' % NS).text, 'lxml')
    census_titles = [
        (int(c.get('value')), _extract_text(c))
        for c in bs.findAll('select', {'name': 'censusid'})[0].findAll('option')
    ]
    census = sorted(census_titles, key=lambda x: x[1])
    return census


def _issues_exist(session, nation):
    '''Return number of issues if there are issues for the nation else False.

    '''
    bs = soup(session.get('%s/nation=%s' % (NS, nation)).text, 'lxml')
    issues = bs.findAll('div', {'id': 'notificationnumber-issues'})
    return issues[0].getText() if issues else False


def process_issues(session, nation):
    '''If there are issues available, process them based on the Previously
    Encountered Changes and the attribute weights.

    '''
    if _issues_exist(session, nation):
        print('issues exist')


def update_issue_census(session, _):
    '''Update the stored list of issue census in the database.

    '''
    print([x[1] for x in _gather_current_census(session)])
