from ...utils import rest
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from starkcore.utils.api import from_api_json
from ..__creditnote import _resource as _creditNote_resource


class Log(Resource):
    """# creditnote.Log object
    Every time a CreditNote entity is updated, a corresponding creditnote.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the CreditNote.
    ## Attributes:
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - note [CreditNote]: CreditNote entity to which the log refers to.
    - errors [list of strings]: list of errors linked to this CreditNote event
    - type [string]: type of the CreditNote event which triggered the log creation. ex: "canceled", "created", "expired", "failed", "refunded", "registered", "sending", "sent", "signed", "success"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, created, type, errors, note):
        Resource.__init__(self, id=id)

        self.created = check_datetime(created)
        self.type = type
        self.errors = errors
        self.note = from_api_json(_creditNote_resource, note)


_resource = {"class": Log, "name": "CreditNoteLog"}


def get(id, user=None):
    """# Retrieve a specific creditnote.Log
    Receive a single creditnote.Log object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - creditnote.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, note_ids=None, user=None):
    """# Retrieve creditnote.Logs
    Receive a generator of creditnote.Log objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default 100]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["canceled", "created", "expired", "failed", "refunded", "registered", "sending", "sent", "signed", "success"]
    - note_ids [list of strings, default None]: list of CreditNote ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - generator of creditnote.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        note_ids=note_ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, note_ids=None, user=None):
    """# Retrieve paged creditnote.Logs
    Receive a list of up to 100 creditnote.Log objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["canceled", "created", "expired", "failed", "refunded", "registered", "sending", "sent", "signed", "success"]
    - note_ids [list of strings, default None]: list of CreditNote ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkinfra.user was set before function call
    ## Return:
    - list of creditnote.Log objects with updated attributes
    - cursor to retrieve the next page of creditnote.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        note_ids=note_ids,
        user=user,
    )
