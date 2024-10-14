# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Database (experimental)

from __future__ import annotations
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT


class DatabaseId(str):
    """Unique identifier of Database object."""

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> DatabaseId:
        return cls(json)

    def __repr__(self):
        return "DatabaseId({})".format(super().__repr__())


@dataclass
class Database:
    """Database object."""
    #: Database ID.
    id_: DatabaseId
    #: Database domain.
    domain: str
    #: Database name.
    name: str
    #: Database version.
    version: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["id"] = self.id_.to_json()
        json["domain"] = self.domain
        json["name"] = self.name
        json["version"] = self.version
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Database:
        return cls(
            id_=DatabaseId.from_json(json["id"]),
            domain=str(json["domain"]),
            name=str(json["name"]),
            version=str(json["version"]),
        )


@dataclass
class Error:
    """Database error."""
    #: Error message.
    message: str
    #: Error code.
    code: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["message"] = self.message
        json["code"] = self.code
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Error:
        return cls(
            message=str(json["message"]),
            code=int(json["code"]),
        )


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables database tracking.
    Prevents database events from being sent to the client.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Database.disable",
    }
    json = yield cmd_dict  # NOQA


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables database tracking.
    Database events will now be delivered to the client.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Database.enable",
    }
    json = yield cmd_dict  # NOQA


def execute_sql(database_id: DatabaseId, query: str) -> typing.Generator[
    T_JSON_DICT,
    T_JSON_DICT,
    typing.Tuple[
        typing.Optional[typing.List[str]],
        typing.Optional[typing.List[typing.Any]],
        typing.Optional[Error],
    ],
]:
    """
    :param database_id:
    :param query:
    :returns: A tuple with the following items:
        0. **columnNames** -
        1. **values** -
        2. **sqlError** -
    """
    params: T_JSON_DICT = dict()
    params["databaseId"] = database_id.to_json()
    params["query"] = query
    cmd_dict: T_JSON_DICT = {
        "method": "Database.executeSQL",
        "params": params,
    }
    json = yield cmd_dict  # NOQA
    return (
        (
            [str(i) for i in json["columnNames"]]
            if json.get("columnNames", None) is not None
            else None
        ),
        (
            [i for i in json["values"]]
            if json.get("values", None) is not None
            else None
        ),
        (
            Error.from_json(json["sqlError"])
            if json.get("sqlError", None) is not None
            else None
        ),
    )


def get_database_table_names(
    database_id: DatabaseId,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[str]]:
    """
    :param database_id:
    """
    params: T_JSON_DICT = dict()
    params["databaseId"] = database_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Database.getDatabaseTableNames",
        "params": params,
    }
    json = yield cmd_dict
    return [str(i) for i in json["tableNames"]]


@event_class("Database.addDatabase")
@dataclass
class AddDatabase:
    database: Database

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AddDatabase:
        return cls(database=Database.from_json(json["database"]))
