# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Autofill (experimental)

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT
from . import dom
from . import page


@dataclass
class CreditCard:
    #: 16-digit credit card number.
    number: str

    #: Name of the credit card owner.
    name: str

    #: 2-digit expiry month.
    expiry_month: str

    #: 4-digit expiry year.
    expiry_year: str

    #: 3-digit card verification code.
    cvc: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["number"] = self.number
        json["name"] = self.name
        json["expiryMonth"] = self.expiry_month
        json["expiryYear"] = self.expiry_year
        json["cvc"] = self.cvc
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CreditCard:
        return cls(
            number=str(json["number"]),
            name=str(json["name"]),
            expiry_month=str(json["expiryMonth"]),
            expiry_year=str(json["expiryYear"]),
            cvc=str(json["cvc"]),
        )


@dataclass
class AddressField:
    #: address field name, for example GIVEN_NAME.
    name: str

    #: address field value, for example Jon Doe.
    value: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name
        json["value"] = self.value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AddressField:
        return cls(
            name=str(json["name"]),
            value=str(json["value"]),
        )


@dataclass
class AddressFields:
    """A list of address fields."""
    fields: typing.List[AddressField]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["fields"] = [i.to_json() for i in self.fields]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AddressFields:
        return cls(
            fields=[AddressField.from_json(i) for i in json["fields"]],
        )


@dataclass
class Address:
    #: fields and values defining an address.
    fields: typing.List[AddressField]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["fields"] = [i.to_json() for i in self.fields]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Address:
        return cls(
            fields=[AddressField.from_json(i) for i in json["fields"]],
        )


@dataclass
class AddressUI:
    """
    Defines how addresses can be displayed like in chrome://settings/addresses.
    Address UI is a two dimensional array, each inner array is an
    "address information line", and when rendered in a UI surface
    should be displayed as such.
    The following address UI for instance:
    [[{name: "GIVE_NAME", value: "Jon"}, {name: "FAMILY_NAME", value: "Doe"}],
    [{name: "CITY", value: "Munich"}, {name: "ZIP", value: "81456"}]]
    should allow the receiver to render:
    Jon Doe
    Munich 81456
    """

    #: A two dimension array containing the representation of values
    #  from an address profile.
    address_fields: typing.List[AddressFields]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["addressFields"] = [i.to_json() for i in self.address_fields]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AddressUI:
        return cls(
            address_fields=[
                AddressFields.from_json(i) for i in json["addressFields"]
            ],
        )


class FillingStrategy(enum.Enum):
    """
    Specified whether a filled field was done so by using
    the html autocomplete attribute or autofill heuristics.
    """

    AUTOCOMPLETE_ATTRIBUTE = "autocompleteAttribute"
    AUTOFILL_INFERRED = "autofillInferred"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> FillingStrategy:
        return cls(json)


@dataclass
class FilledField:
    #: The type of the field, e.g text, password etc.
    html_type: str

    #: the html id
    id_: str

    #: the html name
    name: str

    #: the field value
    value: str

    #: The actual field type, e.g FAMILY_NAME
    autofill_type: str

    #: The filling strategy
    filling_strategy: FillingStrategy

    #: The frame the field belongs to
    frame_id: page.FrameId

    #: The form field's DOM node
    field_id: dom.BackendNodeId

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["htmlType"] = self.html_type
        json["id"] = self.id_
        json["name"] = self.name
        json["value"] = self.value
        json["autofillType"] = self.autofill_type
        json["fillingStrategy"] = self.filling_strategy.to_json()
        json["frameId"] = self.frame_id.to_json()
        json["fieldId"] = self.field_id.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> FilledField:
        return cls(
            html_type=str(json["htmlType"]),
            id_=str(json["id"]),
            name=str(json["name"]),
            value=str(json["value"]),
            autofill_type=str(json["autofillType"]),
            filling_strategy=FillingStrategy.from_json(
                json["fillingStrategy"]
            ),
            frame_id=page.FrameId.from_json(json["frameId"]),
            field_id=dom.BackendNodeId.from_json(json["fieldId"]),
        )


def trigger(
    field_id: dom.BackendNodeId,
    card: CreditCard,
    frame_id: typing.Optional[page.FrameId] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Trigger autofill on a form identified by the fieldId.
    If the field and related form cannot be autofilled, returns an error.
    :param field_id: Identifies a field that serves as an anchor for autofill.
    :param frame_id: *(Optional)* Identifies the frame that field belongs to.
    :param card: Credit card information to fill out the form.
    Credit card data is not saved.
    """
    params: T_JSON_DICT = dict()
    params["fieldId"] = field_id.to_json()
    if frame_id is not None:
        params["frameId"] = frame_id.to_json()
    params["card"] = card.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Autofill.trigger",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def set_addresses(
    addresses: typing.List[Address],
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set addresses so that developers can verify their forms implementation.
    :param addresses:
    """
    params: T_JSON_DICT = dict()
    params["addresses"] = [i.to_json() for i in addresses]
    cmd_dict: T_JSON_DICT = {
        "method": "Autofill.setAddresses",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """Disables autofill domain notifications."""
    cmd_dict: T_JSON_DICT = {
        "method": "Autofill.disable",
    }
    json = yield cmd_dict  # NOQA


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """Enables autofill domain notifications."""
    cmd_dict: T_JSON_DICT = {
        "method": "Autofill.enable",
    }
    json = yield cmd_dict  # NOQA


@event_class("Autofill.addressFormFilled")
@dataclass
class AddressFormFilled:
    """Emitted when an address form is filled."""

    #: Information about the fields that were filled
    filled_fields: typing.List[FilledField]
    #: An UI representation of the address used to fill the form.
    #: Consists of a 2D array where each child represents
    #  an address/profile line.
    address_ui: AddressUI

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AddressFormFilled:
        return cls(
            filled_fields=[
                FilledField.from_json(i) for i in json["filledFields"]
            ],
            address_ui=AddressUI.from_json(json["addressUi"]),
        )
