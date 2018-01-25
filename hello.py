from jira import JIRA
from jira import jirashell


jira = JIRA(server='https://jira.nevint.com/',basic_auth=('austin.bao','Chievo456789'))
projectlist = jira.projects()
issue = jira.issue('FMS-8')

print(issue)
print(projectlist)



