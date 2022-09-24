import datetime
import os
from zoneinfo import ZoneInfo

import pytz
from dateutil import parser
from jira import JIRA

est = pytz.timezone("US/Eastern")
utc = pytz.utc
fmt = "%Y-%m-%d"

today = datetime.datetime.now(ZoneInfo("US/Eastern"))
dates = [today - datetime.timedelta(days=x) for x in range(31)]
dates_counter = {x.strftime(fmt): 0 for x in dates}

jira = JIRA(
    server="https://yrom1.atlassian.net/",
    basic_auth=(os.environ["JIRA_USERNAME"], os.environ["JIRA_PASSWORD"]),
)

issues = jira.search_issues("project = LYFE AND status = Done")

for issue in issues:
    d = parser.parse(issue.fields.updated)  # type: ignore
    assert type(d) == datetime.datetime
    d_date = d.astimezone(est).strftime(fmt)
    if d_date in dates_counter:
        dates_counter[d_date] += 1

DAYS = list(dates_counter.keys())
COUNTS = list(dates_counter.values())
DAYS = DAYS[:14][::-1]
COUNTS = COUNTS[:14][::-1]
assert len(DAYS) == len(COUNTS)
