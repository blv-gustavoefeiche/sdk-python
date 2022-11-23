from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from starkcore.utils.api import from_api_json
from ..__individualidentity import _resource as _individualIdentity_resource


class Log(Resource):
    """# individualidentity.Log object
    Every time a IndividualIdentity entity is updated, a corresponding individualidentity.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the IndividualIdentity.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - identity [IndividualIdentity]: IndividualIdentity entity to which the log refers to.
    - errors [list of strings]: list of errors linked to this IndividualIdentity event
    - type [string]: type of the IndividualIdentity event which triggered the log creation. ex: "created", "canceled", "processing", "failed", "success"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, identity):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.individual = from_api_json(_individualIdentity_resource, identity)


_resource = {"class": Log, "name": "IndividualIdentityLog"}


def get(id, user=None):
    """# Retrieve a specific individualidentity.Log
    Receive a single individualidentity.Log object previously created by the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - individualidentity.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, identity_ids=None, user=None):
    """# Retrieve individualidentity.Logs
    Receive a generator of individualidentity.Log objects previously created in the Stark Infra API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "canceled", "processing", "failed", "success"]
    - identity_ids [list of strings, default None]: list of IndividualIdentity ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - generator of individualidentity.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        identity_ids=identity_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, identity_ids=None, user=None):
    """# Retrieve paged individualidentity.Logs
    Receive a list of up to 100 individualidentity.Log objects previously created in the Stark Infra API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "canceled", "processing", "failed", "success"]
    - identity_ids [list of strings, default None]: list of IndividualIdentity ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call.
    ## Return:
    - list of individualidentity.Log objects with updated attributes
    - cursor to retrieve the next page of individualidentity.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        identity_ids=identity_ids,
        user=user,
    )
