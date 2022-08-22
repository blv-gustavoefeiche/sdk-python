from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.api import from_api_json
from starkcore.utils.checks import check_datetime, check_date
from ..__pixclaim import _resource as _pixclaim_resource


class Log(Resource):
    """# pixclaim.Log object
    Every time a PixClaim entity is modified, a corresponding PixClaim.Log
    is generated for the entity. This log is never generated by the user.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - claim [PixClaim]: PixClaim entity to which the log refers to.
    - type [string]: type of the PixClaim event which triggered the log creation. ex: "created", "failed", "delivering", "delivered", "confirming", "confirmed", "success", "canceling", "canceled"
    - errors [list of strings]: list of errors linked to this PixClaim event
    - reason [string]: reason why the PixClaim was modified, resulting in the Log. Options: "fraud", "userRequested", "accountClosure", "defaultOperation", "reconciliation"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """
    
    def __init__(self, id, claim, type, errors, reason, created):
        Resource.__init__(self, id=id)

        self.claim = from_api_json(_pixclaim_resource, claim)
        self.type = type
        self.errors = errors
        self.reason = reason
        self.created = check_datetime(created)


_resource = {"class": Log, "name": "PixClaimLog"}


def get(id, user=None):
    """# Retrieve a specific PixClaim.Log
    Receive a single PixClaim.Log object previously created by the Stark Infra API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - PixClaim.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(ids=None, limit=None, after=None, before=None, types=None, claim_ids=None, user=None):
    """# Retrieve PixClaim.Logs
    Receive a generator of PixClaim.Log objects previously created in the Stark Infra API
    ## Parameters (optional):
    - ids [list of strings, default None]: Log ids to filter PixClaim Logs. ex: ["5656565656565656"]
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. ex: ["created", "failed", "delivering", "delivered", "confirming", "confirmed", "success", "canceling", "canceled"]
    - claim_ids [list of strings, default None]: list of PixClaim ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - generator of PixClaim.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        claim_ids=claim_ids,
        user=user,
    )


def page(cursor=None, ids=None, limit=None, after=None, before=None, types=None, claim_ids=None, user=None):
    """# Retrieve paged PixClaim.Logs
    Receive a list of up to 100 PixClaim.Log objects previously created in the Stark Infra API and the cursor to the next page.
    Use this function instead of query if you want to manually page your claims.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - ids [list of strings, default None]: Log ids to filter PixClaim Logs. ex: ["5656565656565656"]
    - limit [integer, default 100]: maximum number of objects to be retrieved. Max = 100. ex: 35
    - after [datetime.date or string, default None]: date filter for objects created after a specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None]: date filter for objects created before a specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter retrieved objects by types. ex: ["created", "failed", "delivering", "delivered", "confirming", "confirmed", "success", "canceling", "canceled"]
    - claim_ids [list of strings, default None]: list of PixClaim IDs to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of PixClaim.Log objects with updated attributes
    - cursor to retrieve the next page of PixClaim.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        claim_ids=claim_ids,
        user=user,
    )
