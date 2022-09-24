import datetime as dt

import pandas as pd
from cloud_dictionary import Cloud
from mypandas import MyPandas

from main import COUNTS, DAYS
from stardb import StarSchema

if __name__ == "__main__":
    from main import COUNTS, DAYS

    ISSUES_DONE_TODAY: int = int(COUNTS[-1])
    Cloud("kpiV1")["ISSUES_DONE_TODAY"] = ISSUES_DONE_TODAY
    with StarSchema() as db:
        db.insert_dimension("dimension_jira", [ISSUES_DONE_TODAY])

    query = """
    SELECT SUM(j.issues_done)
    FROM fact_table f
        INNER JOIN dimension_jira j
            ON f.id_jira = j.id
    WHERE month(f.date) = month(now());
    """
    with StarSchema() as db:
        ISSUES_DONE_THIS_MONTH: int = db.query(query)[0][0]
    print(ISSUES_DONE_TODAY, ISSUES_DONE_THIS_MONTH)
    # NOTE new RDS system, wait for new month to use
    # Cloud("kpiV1")["ISSUES_DONE_THIS_MONTH"] = ISSUES_DONE_THIS_MONTH
    # NOTE old mypandas system
    df = pd.DataFrame({"date": DAYS, "value": COUNTS})
    Cloud("kpiV1")["ISSUES_DONE_THIS_MONTH"] = int(
        MyPandas("mysql://root:root@localhost")(
            """
    SELECT SUM(value)
    FROM df
    WHERE month(date) = month(now());
    """,
            locals(),
        ).values[0]
    )

    df.to_json("plot.json")
    with open("plot.json", "r") as f:
        Cloud("plotsV2")["jira"] = f.read()
