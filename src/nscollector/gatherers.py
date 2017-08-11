'''Nation States collector script

'''

from BeautifulSoup import BeautifulSoup as soup


def _issues_exist(session, nation):
    '''Return number of issues if there are issues for the nation else False.

    '''
    bs = soup(session.get('https://www.nationstates.net/nation=%s' % nation).text)
    issues = bs.findAll('div', {'id': 'notificationnumber-issues'})
    return issues[0].getText() if issues else False

def process_issues(session, nation):
    '''If there are issues available, process them based on the Previously
    Encountered Changes and the attribute weights.

    '''
    if _issues_exist(session, nation):
        print 'issues exist'
