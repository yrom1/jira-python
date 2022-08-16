from jira import JIRA
import os

jira = JIRA()

jac = JIRA('https://jira.atlassian.com')

auth_jira = JIRA(auth=(os.environ["JIRA_USERNAME"], os.environ["JIRA_PASSWORD"]))

print(auth_jira)
print(dir(auth_jira))
