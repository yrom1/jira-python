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

with open("ISSUES_DONE_TODAY", "w") as f:
    f.write(str(COUNTS[0]))

DAYS = DAYS[:14][::-1]
COUNTS = COUNTS[:14][::-1]

assert len(DAYS) == len(COUNTS)

# JIRA args
# server: str = None,
# options: Dict[str, Union[str, bool, Any]] = None,
# basic_auth: Optional[Tuple[str, str]] = None,
# token_auth: Optional[str] = None,
# oauth: Dict[str, Any] = None,
# jwt: Dict[str, Any] = None,
# kerberos=False,
# kerberos_options: Dict[str, Any] = None,
# validate=False,
# get_server_info: bool = True,
# async_: bool = False,
# async_workers: int = 5,
# logging: bool = True,
# max_retries: int = 3,
# proxies: Any = None,
# timeout: Union[float, int, Tuple[float, float], NoneType] = None,
# auth: Tuple[str, str] = None,
# default_batch_sizes: Optional[
#     Dict[Type[jira.resources.Resource], Optional[int]]
# ] = None,

# jira object
# "AGILE_BASE_URL",
# "DEFAULT_OPTIONS",
# "JIRA_BASE_URL",
# "__class__",
# "__del__",
# "__delattr__",
# "__dict__",
# "__dir__",
# "__doc__",
# "__eq__",
# "__format__",
# "__ge__",
# "__getattribute__",
# "__gt__",
# "__hash__",
# "__init__",
# "__init_subclass__",
# "__le__",
# "__lt__",
# "__module__",
# "__ne__",
# "__new__",
# "__reduce__",
# "__reduce_ex__",
# "__repr__",
# "__setattr__",
# "__sizeof__",
# "__str__",
# "__subclasshook__",
# "__weakref__",
# "_add_client_cert_to_session",
# "_add_ssl_cert_verif_strategy_to_session",
# "_check_for_html_error",
# "_check_update_",
# "_create_cookie_auth",
# "_create_http_basic_session",
# "_create_jwt_session",
# "_create_kerberos_session",
# "_create_oauth_session",
# "_create_token_session",
# "_fetch_pages",
# "_fields_cache",
# "_fields_cache_value",
# "_find_for_resource",
# "_gain_sudo_session",
# "_get_batch_size",
# "_get_items_from_page",
# "_get_json",
# "_get_latest_url",
# "_get_mime_type",
# "_get_sprint_field_id",
# "_get_url",
# "_get_user_id",
# "_get_user_identifier",
# "_is_cloud",
# "_magic",
# "_options",
# "_rank",
# "_session",
# "_set_avatar",
# "_timestamp",
# "_try_magic",
# "_update_fields_cache",
# "_version",
# "add_attachment",
# "add_comment",
# "add_group",
# "add_issue_property",
# "add_issues_to_epic",
# "add_issues_to_sprint",
# "add_remote_link",
# "add_simple_link",
# "add_user",
# "add_user_to_group",
# "add_vote",
# "add_watcher",
# "add_worklog",
# "application_properties",
# "applicationlinks",
# "assign_issue",
# "async_do",
# "attachment",
# "attachment_meta",
# "auth",
# "avatars",
# "backup",
# "backup_complete",
# "backup_download",
# "backup_progress",
# "boards",
# "checked_version",
# "client_info",
# "close",
# "comment",
# "comments",
# "component",
# "component_count_related_issues",
# "confirm_project_avatar",
# "confirm_user_avatar",
# "create_board",
# "create_component",
# "create_customer",
# "create_customer_request",
# "create_filter",
# "create_issue",
# "create_issue_link",
# "create_issues",
# "create_project",
# "create_sprint",
# "create_temp_project_avatar",
# "create_temp_user_avatar",
# "create_version",
# "createmeta",
# "current_user",
# "custom_field_option",
# "dashboard",
# "dashboards",
# "deactivate_user",
# "delete_attachment",
# "delete_board",
# "delete_component",
# "delete_issue_link",
# "delete_permissionscheme",
# "delete_project",
# "delete_project_avatar",
# "delete_remote_link",
# "delete_screen",
# "delete_user",
# "delete_user_avatar",
# "deploymentType",
# "editmeta",
# "favourite_filters",
# "fields",
# "filter",
# "find",
# "find_transitionid_by_name",
# "get_igrid",
# "get_issue_type_scheme_associations",
# "get_project_version_by_name",
# "group",
# "group_members",
# "groups",
# "incompletedIssuesEstimateSum",
# "issue",
# "issue_link",
# "issue_link_type",
# "issue_link_types",
# "issue_properties",
# "issue_property",
# "issue_type",
# "issue_type_by_name",
# "issue_type_schemes",
# "issue_types",
# "issuesecurityschemes",
# "kill_session",
# "kill_websudo",
# "log",
# "move_to_backlog",
# "move_version",
# "my_permissions",
# "myself",
# "notificationschemes",
# "permissionschemes",
# "priorities",
# "priority",
# "project",
# "project_avatars",
# "project_components",
# "project_issue_security_level_scheme",
# "project_notification_scheme",
# "project_permissionscheme",
# "project_priority_scheme",
# "project_role",
# "project_roles",
# "project_versions",
# "project_workflow_scheme",
# "projectcategories",
# "projects",
# "rank",
# "reindex",
# "remote_link",
# "remote_links",
# "remove_group",
# "remove_user_from_group",
# "remove_vote",
# "remove_watcher",
# "removedIssuesEstimateSum",
# "removed_issues",
# "rename_user",
# "rename_version",
# "request_type_by_name",
# "request_types",
# "resolution",
# "resolutions",
# "role",
# "screens",
# "search_allowed_users_for_issue",
# "search_assignable_users_for_issues",
# "search_assignable_users_for_projects",
# "search_issues",
# "search_users",
# "security_level",
# "server_info",
# "server_url",
# "service_desk",
# "service_desks",
# "session",
# "set_application_property",
# "set_project_avatar",
# "set_user_avatar",
# "sprint",
# "sprint_info",
# "sprints",
# "sprints_by_name",
# "status",
# "statuscategories",
# "statuscategory",
# "statuses",
# "supports_service_desk",
# "sys_version_info",
# "templates",
# "transition_issue",
# "transitions",
# "update_filter",
# "update_sprint",
# "user",
# "user_avatars",
# "version",
# "version_count_related_issues",
# "version_count_unresolved_issues",
# "votes",
# "watchers",
# "workflows",
# "workflowscheme",
# "worklog",
# "worklogs",
