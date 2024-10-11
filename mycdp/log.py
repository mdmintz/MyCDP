# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Log

from __future__ import annotations
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT
from . import network
from . import runtime


@dataclass
class LogEntry:
    """Log entry."""

    #: Log entry source.
    source: str

    #: Log entry severity.
    level: str

    #: Logged text.
    text: str

    #: Timestamp when this entry was added.
    timestamp: runtime.Timestamp

    category: typing.Optional[str] = None

    #: URL of the resource if known.
    url: typing.Optional[str] = None

    #: Line number in the resource.
    line_number: typing.Optional[int] = None

    #: JavaScript stack trace.
    stack_trace: typing.Optional[runtime.StackTrace] = None

    #: Identifier of the network request associated with this entry.
    network_request_id: typing.Optional[network.RequestId] = None

    #: Identifier of the worker associated with this entry.
    worker_id: typing.Optional[str] = None

    #: Call arguments.
    args: typing.Optional[typing.List[runtime.RemoteObject]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["source"] = self.source
        json["level"] = self.level
        json["text"] = self.text
        json["timestamp"] = self.timestamp.to_json()
        if self.category is not None:
            json["category"] = self.category
        if self.url is not None:
            json["url"] = self.url
        if self.line_number is not None:
            json["lineNumber"] = self.line_number
        if self.stack_trace is not None:
            json["stackTrace"] = self.stack_trace.to_json()
        if self.network_request_id is not None:
            json["networkRequestId"] = self.network_request_id.to_json()
        if self.worker_id is not None:
            json["workerId"] = self.worker_id
        if self.args is not None:
            json["args"] = [i.to_json() for i in self.args]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> LogEntry:
        return cls(
            source=str(json["source"]),
            level=str(json["level"]),
            text=str(json["text"]),
            timestamp=runtime.Timestamp.from_json(json["timestamp"]),
            category=(
                str(json["category"])
                if json.get("category", None) is not None
                else None
            ),
            url=(
                str(json["url"]) if json.get("url", None) is not None else None
            ),
            line_number=(
                int(json["lineNumber"])
                if json.get("lineNumber", None) is not None
                else None
            ),
            stack_trace=(
                runtime.StackTrace.from_json(json["stackTrace"])
                if json.get("stackTrace", None) is not None
                else None
            ),
            network_request_id=(
                network.RequestId.from_json(json["networkRequestId"])
                if json.get("networkRequestId", None) is not None
                else None
            ),
            worker_id=(
                str(json["workerId"])
                if json.get("workerId", None) is not None
                else None
            ),
            args=(
                [runtime.RemoteObject.from_json(i) for i in json["args"]]
                if json.get("args", None) is not None
                else None
            ),
        )


@dataclass
class ViolationSetting:
    """Violation configuration setting."""

    #: Violation type.
    name: str

    #: Time threshold to trigger upon.
    threshold: float

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name
        json["threshold"] = self.threshold
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ViolationSetting:
        return cls(
            name=str(json["name"]),
            threshold=float(json["threshold"]),
        )


def clear() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """Clears the log."""
    cmd_dict: T_JSON_DICT = {
        "method": "Log.clear",
    }
    json = yield cmd_dict  # NOQA


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables log domain, prevents further log entries
    from being reported to the client.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Log.disable",
    }
    json = yield cmd_dict  # NOQA


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables log domain, sends the entries collected so far
    to the client by means of the ``entryAdded`` notification.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Log.enable",
    }
    json = yield cmd_dict  # NOQA


def start_violations_report(
    config: typing.List[ViolationSetting],
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Start violation reporting.
    :param config: Configuration for violations.
    """
    params: T_JSON_DICT = dict()
    params["config"] = [i.to_json() for i in config]
    cmd_dict: T_JSON_DICT = {
        "method": "Log.startViolationsReport",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def stop_violations_report() -> (
    typing.Generator[T_JSON_DICT, T_JSON_DICT, None]
):
    """Stop violation reporting."""
    cmd_dict: T_JSON_DICT = {
        "method": "Log.stopViolationsReport",
    }
    json = yield cmd_dict  # NOQA


@event_class("Log.entryAdded")
@dataclass
class EntryAdded:
    """Issued when new message was logged."""

    #: The entry.
    entry: LogEntry

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> EntryAdded:
        return cls(entry=LogEntry.from_json(json["entry"]))
