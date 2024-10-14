# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Browser

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT
from . import page
from . import target


class BrowserContextID(str):
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> BrowserContextID:
        return cls(json)

    def __repr__(self):
        return "BrowserContextID({})".format(super().__repr__())


class WindowID(int):
    def to_json(self) -> int:
        return self

    @classmethod
    def from_json(cls, json: int) -> WindowID:
        return cls(json)

    def __repr__(self):
        return "WindowID({})".format(super().__repr__())


class WindowState(enum.Enum):
    """The state of the browser window."""
    NORMAL = "normal"
    MINIMIZED = "minimized"
    MAXIMIZED = "maximized"
    FULLSCREEN = "fullscreen"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> WindowState:
        return cls(json)


@dataclass
class Bounds:
    """Browser window bounds information"""
    #: The offset from the left edge of the screen to the window in pixels.
    left: typing.Optional[int] = None
    #: The offset from the top edge of the screen to the window in pixels.
    top: typing.Optional[int] = None
    #: The window width in pixels.
    width: typing.Optional[int] = None
    #: The window height in pixels.
    height: typing.Optional[int] = None
    #: The window state. Default to normal.
    window_state: typing.Optional[WindowState] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.left is not None:
            json["left"] = self.left
        if self.top is not None:
            json["top"] = self.top
        if self.width is not None:
            json["width"] = self.width
        if self.height is not None:
            json["height"] = self.height
        if self.window_state is not None:
            json["windowState"] = self.window_state.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Bounds:
        return cls(
            left=(
                int(json["left"])
                if json.get("left", None) is not None
                else None
            ),
            top=(
                int(json["top"]) if json.get("top", None) is not None else None
            ),
            width=(
                int(json["width"])
                if json.get("width", None) is not None
                else None
            ),
            height=(
                int(json["height"])
                if json.get("height", None) is not None
                else None
            ),
            window_state=(
                WindowState.from_json(json["windowState"])
                if json.get("windowState", None) is not None
                else None
            ),
        )


class PermissionType(enum.Enum):
    ACCESSIBILITY_EVENTS = "accessibilityEvents"
    AUDIO_CAPTURE = "audioCapture"
    BACKGROUND_SYNC = "backgroundSync"
    BACKGROUND_FETCH = "backgroundFetch"
    CAPTURED_SURFACE_CONTROL = "capturedSurfaceControl"
    CLIPBOARD_READ_WRITE = "clipboardReadWrite"
    CLIPBOARD_SANITIZED_WRITE = "clipboardSanitizedWrite"
    DISPLAY_CAPTURE = "displayCapture"
    DURABLE_STORAGE = "durableStorage"
    FLASH = "flash"
    GEOLOCATION = "geolocation"
    IDLE_DETECTION = "idleDetection"
    LOCAL_FONTS = "localFonts"
    MIDI = "midi"
    MIDI_SYSEX = "midiSysex"
    NFC = "nfc"
    NOTIFICATIONS = "notifications"
    PAYMENT_HANDLER = "paymentHandler"
    PERIODIC_BACKGROUND_SYNC = "periodicBackgroundSync"
    PROTECTED_MEDIA_IDENTIFIER = "protectedMediaIdentifier"
    SENSORS = "sensors"
    STORAGE_ACCESS = "storageAccess"
    SPEAKER_SELECTION = "speakerSelection"
    TOP_LEVEL_STORAGE_ACCESS = "topLevelStorageAccess"
    VIDEO_CAPTURE = "videoCapture"
    VIDEO_CAPTURE_PAN_TILT_ZOOM = "videoCapturePanTiltZoom"
    WAKE_LOCK_SCREEN = "wakeLockScreen"
    WAKE_LOCK_SYSTEM = "wakeLockSystem"
    WINDOW_MANAGEMENT = "windowManagement"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> PermissionType:
        return cls(json)


class PermissionSetting(enum.Enum):
    GRANTED = "granted"
    DENIED = "denied"
    PROMPT = "prompt"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> PermissionSetting:
        return cls(json)


@dataclass
class PermissionDescriptor:
    """
    Definition of PermissionDescriptor defined in the Permissions API:
    https://w3c.github.io/permissions/#dom-permissiondescriptor.
    """
    #: Name of permission.
    name: str
    #: For "midi" permission, may also specify sysex control.
    sysex: typing.Optional[bool] = None
    #: For "push" permission, may specify userVisibleOnly.
    #: Note that userVisibleOnly = true is the only currently supported type.
    user_visible_only: typing.Optional[bool] = None
    #: For "clipboard" permission, may specify allowWithoutSanitization.
    allow_without_sanitization: typing.Optional[bool] = None
    #: For "fullscreen" permission, must specify allowWithoutGesture:true.
    allow_without_gesture: typing.Optional[bool] = None
    #: For "camera" permission, may specify panTiltZoom.
    pan_tilt_zoom: typing.Optional[bool] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name
        if self.sysex is not None:
            json["sysex"] = self.sysex
        if self.user_visible_only is not None:
            json["userVisibleOnly"] = self.user_visible_only
        if self.allow_without_sanitization is not None:
            json["allowWithoutSanitization"] = self.allow_without_sanitization
        if self.allow_without_gesture is not None:
            json["allowWithoutGesture"] = self.allow_without_gesture
        if self.pan_tilt_zoom is not None:
            json["panTiltZoom"] = self.pan_tilt_zoom
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PermissionDescriptor:
        return cls(
            name=str(json["name"]),
            sysex=(
                bool(json["sysex"])
                if json.get("sysex", None) is not None
                else None
            ),
            user_visible_only=(
                bool(json["userVisibleOnly"])
                if json.get("userVisibleOnly", None) is not None
                else None
            ),
            allow_without_sanitization=(
                bool(json["allowWithoutSanitization"])
                if json.get("allowWithoutSanitization", None) is not None
                else None
            ),
            allow_without_gesture=(
                bool(json["allowWithoutGesture"])
                if json.get("allowWithoutGesture", None) is not None
                else None
            ),
            pan_tilt_zoom=(
                bool(json["panTiltZoom"])
                if json.get("panTiltZoom", None) is not None
                else None
            ),
        )


class BrowserCommandId(enum.Enum):
    """Browser command ids used by executeBrowserCommand."""
    OPEN_TAB_SEARCH = "openTabSearch"
    CLOSE_TAB_SEARCH = "closeTabSearch"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> BrowserCommandId:
        return cls(json)


@dataclass
class Bucket:
    """Chrome histogram bucket."""
    #: Minimum value (inclusive).
    low: int
    #: Maximum value (exclusive).
    high: int
    #: Number of samples.
    count: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["low"] = self.low
        json["high"] = self.high
        json["count"] = self.count
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Bucket:
        return cls(
            low=int(json["low"]),
            high=int(json["high"]),
            count=int(json["count"]),
        )


@dataclass
class Histogram:
    """Chrome histogram."""
    #: Name.
    name: str
    #: Sum of sample values.
    sum_: int
    #: Total number of samples.
    count: int
    #: Buckets.
    buckets: typing.List[Bucket]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name
        json["sum"] = self.sum_
        json["count"] = self.count
        json["buckets"] = [i.to_json() for i in self.buckets]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Histogram:
        return cls(
            name=str(json["name"]),
            sum_=int(json["sum"]),
            count=int(json["count"]),
            buckets=[Bucket.from_json(i) for i in json["buckets"]],
        )


def set_permission(
    permission: PermissionDescriptor,
    setting: PermissionSetting,
    origin: typing.Optional[str] = None,
    browser_context_id: typing.Optional[BrowserContextID] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set permission settings for given origin.
    **EXPERIMENTAL**
    :param permission: Descriptor of permission to override.
    :param setting: Setting of the permission.
    :param origin: *(Optional)* Origin the permission applies to,
     all origins if not specified.
    :param browser_context_id: *(Optional)* Context to override.
    When omitted, default browser context is used.
    """
    params: T_JSON_DICT = dict()
    params["permission"] = permission.to_json()
    params["setting"] = setting.to_json()
    if origin is not None:
        params["origin"] = origin
    if browser_context_id is not None:
        params["browserContextId"] = browser_context_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.setPermission",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def grant_permissions(
    permissions: typing.List[PermissionType],
    origin: typing.Optional[str] = None,
    browser_context_id: typing.Optional[BrowserContextID] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Grant specific permissions to the given origin and reject all others.
    **EXPERIMENTAL**
    :param permissions:
    :param origin: *(Optional)* Origin the permission applies to,
     all origins if not specified.
    :param browser_context_id: *(Optional)* BrowserContext to
     override permissions. When omitted, default browser context is used.
    """
    params: T_JSON_DICT = dict()
    params["permissions"] = [i.to_json() for i in permissions]
    if origin is not None:
        params["origin"] = origin
    if browser_context_id is not None:
        params["browserContextId"] = browser_context_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.grantPermissions",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def reset_permissions(
    browser_context_id: typing.Optional[BrowserContextID] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Reset all permission management for all origins.
    :param browser_context_id: *(Optional)* BrowserContext
    to reset permissions. When omitted, default browser context is used.
    """
    params: T_JSON_DICT = dict()
    if browser_context_id is not None:
        params["browserContextId"] = browser_context_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.resetPermissions",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def set_download_behavior(
    behavior: str,
    browser_context_id: typing.Optional[BrowserContextID] = None,
    download_path: typing.Optional[str] = None,
    events_enabled: typing.Optional[bool] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set the behavior when downloading a file.
    **EXPERIMENTAL**
    :param behavior: Whether to allow all or deny all download requests,
     or use default Chrome behavior if available (otherwise deny).
     ``allowAndName`` allows download and names files
     according to their download guids.
    :param browser_context_id: *(Optional)*
     BrowserContext to set download behavior.
     When omitted, default browser context is used.
    :param download_path: *(Optional)*
     The default path to save downloaded files to.
     This is required if behavior is set to 'allow' or 'allowAndName'.
    :param events_enabled: *(Optional)*
     Whether to emit download events (defaults to false).
    """
    params: T_JSON_DICT = dict()
    params["behavior"] = behavior
    if browser_context_id is not None:
        params["browserContextId"] = browser_context_id.to_json()
    if download_path is not None:
        params["downloadPath"] = download_path
    if events_enabled is not None:
        params["eventsEnabled"] = events_enabled
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.setDownloadBehavior",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def cancel_download(
    guid: str, browser_context_id: typing.Optional[BrowserContextID] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Cancel a download if in progress.
    **EXPERIMENTAL**
    :param guid: Global unique identifier of the download.
    :param browser_context_id: *(Optional)*
     BrowserContext to perform the action in.
     When omitted, default browser context is used.
    """
    params: T_JSON_DICT = dict()
    params["guid"] = guid
    if browser_context_id is not None:
        params["browserContextId"] = browser_context_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.cancelDownload",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def close() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """Close browser gracefully."""
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.close",
    }
    json = yield cmd_dict  # NOQA


def crash() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Crashes browser on the main thread.
    **EXPERIMENTAL**
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.crash",
    }
    json = yield cmd_dict  # NOQA


def crash_gpu_process() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Crashes GPU process.
    **EXPERIMENTAL**
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.crashGpuProcess",
    }
    json = yield cmd_dict  # NOQA


def get_version() -> (
    typing.Generator[
        T_JSON_DICT, T_JSON_DICT, typing.Tuple[str, str, str, str, str]
    ]
):
    """
    Returns version information.
    :returns: A tuple with the following items:
        0. **protocolVersion** - Protocol version.
        1. **product** - Product name.
        2. **revision** - Product revision.
        3. **userAgent** - User-Agent.
        4. **jsVersion** - V8 version.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getVersion",
    }
    json = yield cmd_dict
    return (
        str(json["protocolVersion"]),
        str(json["product"]),
        str(json["revision"]),
        str(json["userAgent"]),
        str(json["jsVersion"]),
    )


def get_browser_command_line() -> (
    typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[str]]
):
    """
    Returns the command line switches for the browser process if,
    and only if --enable-automation is on the command-line.
    **EXPERIMENTAL**
    :returns: Commandline parameters
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getBrowserCommandLine",
    }
    json = yield cmd_dict
    return [str(i) for i in json["arguments"]]


def get_histograms(
    query: typing.Optional[str] = None, delta: typing.Optional[bool] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[Histogram]]:
    """
    Get Chrome histograms.
    **EXPERIMENTAL**
    :param query: *(Optional)* Requested substring in name.
     Only histograms which have query as a substring in their name
     are extracted. An empty or absent query returns all histograms.
    :param delta: *(Optional)* If true, retrieve delta since last delta call.
    :returns: Histograms.
    """
    params: T_JSON_DICT = dict()
    if query is not None:
        params["query"] = query
    if delta is not None:
        params["delta"] = delta
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getHistograms",
        "params": params,
    }
    json = yield cmd_dict
    return [Histogram.from_json(i) for i in json["histograms"]]


def get_histogram(
    name: str, delta: typing.Optional[bool] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, Histogram]:
    """
    Get a Chrome histogram by name.
    **EXPERIMENTAL**
    :param name: Requested histogram name.
    :param delta: *(Optional)* If true, retrieve delta since last delta call.
    :returns: Histogram.
    """
    params: T_JSON_DICT = dict()
    params["name"] = name
    if delta is not None:
        params["delta"] = delta
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getHistogram",
        "params": params,
    }
    json = yield cmd_dict
    return Histogram.from_json(json["histogram"])


def get_window_bounds(
    window_id: WindowID,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, Bounds]:
    """
    Get position and size of the browser window.
    **EXPERIMENTAL**
    :param window_id: Browser window id.
    :returns: Bounds information of the window.
    When window state is 'minimized',
    the restored window position and size are returned.
    """
    params: T_JSON_DICT = dict()
    params["windowId"] = window_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getWindowBounds",
        "params": params,
    }
    json = yield cmd_dict
    return Bounds.from_json(json["bounds"])


def get_window_for_target(
    target_id: typing.Optional[target.TargetID] = None,
) -> typing.Generator[
    T_JSON_DICT, T_JSON_DICT, typing.Tuple[WindowID, Bounds]
]:
    """
    Get the browser window that contains the devtools target.
    **EXPERIMENTAL**
    :param target_id: *(Optional)* Devtools agent host id.
     If called as a part of the session, associated targetId is used.
    :returns: A tuple with the following items:
        0. **windowId** - Browser window id.
        1. **bounds** - Bounds information of the window.
        When window state is 'minimized',
        the restored window position and size are returned.
    """
    params: T_JSON_DICT = dict()
    if target_id is not None:
        params["targetId"] = target_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.getWindowForTarget",
        "params": params,
    }
    json = yield cmd_dict
    return (
        WindowID.from_json(json["windowId"]),
        Bounds.from_json(json["bounds"]),
    )


def set_window_bounds(
    window_id: WindowID, bounds: Bounds
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set position and/or size of the browser window.
    **EXPERIMENTAL**
    :param window_id: Browser window id.
    :param bounds: New window bounds.
    The 'minimized', 'maximized' and 'fullscreen' states
    cannot be combined with 'left', 'top', 'width' or 'height'.
    Leaves unspecified fields unchanged.
    """
    params: T_JSON_DICT = dict()
    params["windowId"] = window_id.to_json()
    params["bounds"] = bounds.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.setWindowBounds",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def set_dock_tile(
    badge_label: typing.Optional[str] = None,
    image: typing.Optional[str] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set dock tile details, platform-specific.
    **EXPERIMENTAL**
    :param badge_label: *(Optional)*
    :param image: *(Optional)* Png encoded image.
    (Encoded as a base64 string when passed over JSON)
    """
    params: T_JSON_DICT = dict()
    if badge_label is not None:
        params["badgeLabel"] = badge_label
    if image is not None:
        params["image"] = image
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.setDockTile",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def execute_browser_command(
    command_id: BrowserCommandId,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Invoke custom browser commands used by telemetry.
    **EXPERIMENTAL**
    :param command_id:
    """
    params: T_JSON_DICT = dict()
    params["commandId"] = command_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.executeBrowserCommand",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


def add_privacy_sandbox_enrollment_override(
    url: str,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Allows a site to use privacy sandbox features that require enrollment
    without the site actually being enrolled. Only supported on page targets.
    :param url:
    """
    params: T_JSON_DICT = dict()
    params["url"] = url
    cmd_dict: T_JSON_DICT = {
        "method": "Browser.addPrivacySandboxEnrollmentOverride",
        "params": params,
    }
    json = yield cmd_dict  # NOQA


@event_class("Browser.downloadWillBegin")
@dataclass
class DownloadWillBegin:
    """
    **EXPERIMENTAL**
    Fired when page is about to start a download.
    """
    #: Id of the frame that caused the download to begin.
    frame_id: page.FrameId
    #: Global unique identifier of the download.
    guid: str
    #: URL of the resource being downloaded.
    url: str
    #: Suggested file name of the resource
    #  (the actual name of the file saved on disk may differ).
    suggested_filename: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DownloadWillBegin:
        return cls(
            frame_id=page.FrameId.from_json(json["frameId"]),
            guid=str(json["guid"]),
            url=str(json["url"]),
            suggested_filename=str(json["suggestedFilename"]),
        )


@event_class("Browser.downloadProgress")
@dataclass
class DownloadProgress:
    """
    **EXPERIMENTAL**
    Fired when download makes progress. Last call has ``done`` == true.
    """
    #: Global unique identifier of the download.
    guid: str
    #: Total expected bytes to download.
    total_bytes: float
    #: Total bytes received.
    received_bytes: float
    #: Download status.
    state: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DownloadProgress:
        return cls(
            guid=str(json["guid"]),
            total_bytes=float(json["totalBytes"]),
            received_bytes=float(json["receivedBytes"]),
            state=str(json["state"]),
        )
