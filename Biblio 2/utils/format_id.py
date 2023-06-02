import json


def id(u):
    cp = dict.copy(u)
    cp['_id'] = str(u['_id'])
    return cp


def convert(cursor):
    ls = list(cursor)
    ls = list(map(id, ls))
    return ls


def from_objectId_to_json(item: object):
    item = json.loads(item.to_json())
    cp = dict.copy(item)
    cp["_id"] = cp['_id']['$oid']
    return cp
