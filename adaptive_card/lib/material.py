from __future__ import annotations
from abc import ABC
from enum import Enum
from typing import Any, List
from json import dumps
from collections.abc import Mapping

class MaterialTypes(Enum):
    ADAPTIVE_CARD = "AdaptiveCard"
    CONTAINER = "Container"
    CAROUSEL = "Carousel"
    CAROUSEL_PAGE = "CarouselPage"
    TABLE = "Table"
    TABLE_ROW = "TableRow"
    TABLE_CELL = "TableCell"
    TEXT_BLOCK = "TextBlock"
    FACT_SET = "FactSet"
    FACT = "Fact"
    COLUMN_SET = "ColumnSet"
    COLUMN = "Column"
    IMAGE_SET = "ImageSet"
    IMAGE = "Image"
    ACTION_SET = "ActionSet"
    ACTION_OPEN_URL = "Action.OpenUrl"
    ACTION_SUBMIT = "Action.Submit"
    ACTION_SHOW_CARD = "Action.ShowCard"
    ACTION_TOGGLE_VISIBILITY = "Action.ToggleVisibility"
    ACTION_EXECUTE = "Action.Execute"
    INPUT_TEXT = "Input.Text"
    INPUT_DATE = "Input.Date"
    INPUT_TIME = "Input.Time"
    INPUT_NUMBER = "Input.Number"
    INPUT_CHOICE_SET = "Input.ChoiceSet"
    INPUT_CHOICE = "Input.Choice"
    INPUT_TOGGLE = "Input.Toggle"
    MEDIA = "Media"

class ActionTypes(Enum):
    SUBMIT = MaterialTypes.ACTION_SUBMIT.value
    OPEN_URL = MaterialTypes.ACTION_OPEN_URL.value
    SHOW_CARD = MaterialTypes.ACTION_SHOW_CARD.value
    TOGGLE_VISIBILITY = MaterialTypes.ACTION_TOGGLE_VISIBILITY.value
    EXECUTE = MaterialTypes.ACTION_EXECUTE.value

class InputTypes(Enum):
    CHOICE_SET = MaterialTypes.INPUT_CHOICE_SET.value
    DATE = MaterialTypes.INPUT_DATE.value
    NUMBER = MaterialTypes.INPUT_NUMBER.value
    TEXT = MaterialTypes.INPUT_TEXT.value
    TIME = MaterialTypes.INPUT_TIME.value
    TOGGLE = MaterialTypes.INPUT_TOGGLE.value

class MaterialColors(Enum):
    UNSET = None
    DEFAULT = "Default"
    DARK = "Dark"
    LIGHT = "Light"
    ACCENT = "Accent"
    GOOD = "Good"
    ATTTENTION = "Attention"
    WARNING = "Warning"

class MaterialHeight(Enum):
    UNSET = None
    AUTO = "auto"
    STRETCH = "stretch"

class MaterialOrientation(Enum):
    UNSET = None
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

class HorizontalAlignments(Enum):
    UNSET = None
    LEFT = "Left"
    CENTER = "Center"
    RIGHT = "Right"

class VerticalAlignments(Enum):
    UNSET = None
    TOP = "Top"
    CENTER = "Center"
    BOTTOM = "Bottom"

class MaterialSpacings(Enum):
    UNSET = None
    NONE = "None"
    SMALL = "Small"
    DEFAULT = "Default"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "ExtraLarge"
    PADDING = "Padding"

class ActionStyles(Enum):
    UNSET = None
    DEFAULT = "default"
    POSITIVE = "positive"
    DESTRUCTIVE = "destructive"

class ActionModes(Enum):
    UNSET = None
    PRIMARY = "primary"
    SECONDARY = "secondary"

class ActionRoles(Enum):
    UNSET = None
    BUTTON = "Button"
    LINK = "Link"
    TAB = "Tab"
    MENU = "Menu"
    MENU_ITEM = "MenuItem"

class MaterialDynamic(ABC):
    def __init__(self, __value: Any):

        not_instantiatable(self, MaterialDynamic)

        self.__value = __value

    @property
    def value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return self.__value

class Weight(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(__value)

class Seconds(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(__value)

class Pixels(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(f"{__value}px")

class Material(ABC):
    def _read(self, __value: Any) -> Any:
        if isinstance(__value, (Enum, MaterialDynamic)):
            return __value.value

        if isinstance(__value, (AdaptiveCardMaterial, MaterialMapping)):
            return __value.__dict__

        if isinstance(__value, (list, tuple)):
            return [self._read(item) for item in __value]
        
        return __value
   
class MaterialMapping(Material, Mapping):
    def __init__(self, **kwargs):

        not_instantiatable(self, MaterialMapping)

        self.__data = {}
        for key in kwargs:
            value = self._read(kwargs[key])
            if value is not None:
                self.__data[key] = value
    
    @property   
    def __dict__(self):
        return self.__data.copy()
    
    def __getitem__(self, __key: Any) -> Any:
        return self.__data.__getitem__(__key)

    def __len__(self) -> int:
        return len(self.__data)
    
    def __iter__(self):
        for key in self.__data:
            yield key
    
    def __str__(self) -> str:
        return str(self.__data)

class MaterialLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET
        ):

        super().__init__(
            separator=separator, 
            spacing=spacing
        )

class AdaptiveCardMaterial(Material): 
    def __init__(
            self, 
            __type: MaterialTypes,
            id: str | None=None,
            visible: bool=True,
            **kwargs
        ):
        
        not_instantiatable(self, AdaptiveCardMaterial)

        self.__data: dict[str, Any] = {"type": __type.value}

        if "type" in kwargs:
            del kwargs["type"]
        
        if id:
            self.__data["id"] = id

        if not visible:
            self.__data["isVisible"] = False

        for key in kwargs:
            value = self._read(kwargs[key])
            if value is not None:
                self.__data[key] = value
    
    @property
    def type(self):
        return self.__data["type"]
    
    @property
    def id(self):
        return self.__data.get("id")
    
    def get(self, __key: str) -> object:
        return self.__data.get(__key)
    
    def update(self, **kwargs):
        if "type" in kwargs:
            raise KeyError(f"You cannot change the attribute type of any '{self.__class__.__name__}' object.")
        
        for key in kwargs:
            value = self._read(kwargs[key])

            if value is None:
                if key in self.__data:
                    del self.__data[key]
            else:
                self.__data[key] = value
    
    @staticmethod
    def ensure_list_items_typing(__list: List[object] | None, *__types: type[Any]):
        if __list:
            __types = __types if __types else (AdaptiveCardMaterial)
            for index, item in enumerate(__list):
                if isinstance(item, __types):
                    continue
                    
                raise TypeError(f"Item at index {index} is not of a valid type. Valid types are: {[t.__name__ for t in __types]}.")

    @property
    def __dict__(self)->dict:
        return self.__data
    
    def __str__(self)->str:
        return dumps(self.__data)
    
    def __iter__(self):
        for key in self.__data:
            yield key

class BackgroundFillModes(Enum):
    UNSET = None
    COVER = "Cover"
    REPEAT = "Repeat"
    REPEAT_HORIZONTALLY = "RepeatHorizontally"
    REPEAT_VERTICALLY = "RepeatVertically"

class BackgroundImage(MaterialMapping):
    def __init__(
            self,
            __url: str,
            fill: BackgroundFillModes=BackgroundFillModes.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            vertical_alignment: VerticalAlignments=VerticalAlignments.UNSET  
        ):
        data = {"url": __url}

        if fill.value:
            data["fillMode"] = fill.value
        
        if horizontal_alignment.value:
            data["horizontalAlignment"] = horizontal_alignment.value

        if vertical_alignment.value:
            data["verticalAlignment"] = vertical_alignment.value
        
        super().__init__(backgroundImage=data)

class AdaptiveCardAction(AdaptiveCardMaterial):
    def __init__(
            self, 
            __type: ActionTypes,
            title: str, 
            tooltip: str | None=None,
            enabled: bool=True,
            icon_url: str | None=None,
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            id: str | None=None,
            **kwargs):
        
        not_instantiatable(self, AdaptiveCardAction)
        
        super().__init__(
            __type,
            id=id,
            title=title, 
            tooltip=tooltip,
            isEnabled=False if not enabled else None,
            iconUrl=icon_url,
            mode=mode,
            style=style,
            role=role,
            **kwargs
        )

def not_instantiatable(__instance: Any, __type: type[Any]):
    if __instance.__class__ is __type:
        raise TypeError(f"Abstract class '{__type.__name__}' cannot be instantiated.")