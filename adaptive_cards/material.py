from __future__ import annotations
from typing import Optional, Any, Iterable, overload
from abc import ABC, abstractmethod
from collections.abc import Mapping
from json import dumps
from enum import Enum

class MaterialType(Enum):
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
    TARGET_ELEMENT = "TargetElement"
    INPUT_TEXT = "Input.Text"
    INPUT_DATE = "Input.Date"
    INPUT_TIME = "Input.Time"
    INPUT_NUMBER = "Input.Number"
    INPUT_CHOICE_SET = "Input.ChoiceSet"
    INPUT_CHOICE = "Input.Choice"
    INPUT_TOGGLE = "Input.Toggle"
    MEDIA = "Media"

class ActionType(Enum):
    SUBMIT = MaterialType.ACTION_SUBMIT.value
    OPEN_URL = MaterialType.ACTION_OPEN_URL.value
    SHOW_CARD = MaterialType.ACTION_SHOW_CARD.value
    TOGGLE_VISIBILITY = MaterialType.ACTION_TOGGLE_VISIBILITY.value
    EXECUTE = MaterialType.ACTION_EXECUTE.value

class InputType(Enum):
    CHOICE_SET = MaterialType.INPUT_CHOICE_SET.value
    DATE = MaterialType.INPUT_DATE.value
    NUMBER = MaterialType.INPUT_NUMBER.value
    TEXT = MaterialType.INPUT_TEXT.value
    TIME = MaterialType.INPUT_TIME.value
    TOGGLE = MaterialType.INPUT_TOGGLE.value

class MaterialColor(Enum):
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

class HorizontalAlignment(Enum):
    UNSET = None
    LEFT = "Left"
    CENTER = "Center"
    RIGHT = "Right"

class VerticalAlignment(Enum):
    UNSET = None
    TOP = "Top"
    CENTER = "Center"
    BOTTOM = "Bottom"

class MaterialSpacing(Enum):
    UNSET = None
    NONE = "None"
    SMALL = "Small"
    DEFAULT = "Default"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "ExtraLarge"
    PADDING = "Padding"

class ActionTheme(Enum):
    UNSET = None
    DEFAULT = "default"
    POSITIVE = "positive"
    DESTRUCTIVE = "destructive"

class ActionMode(Enum):
    UNSET = None
    PRIMARY = "primary"
    SECONDARY = "secondary"

class ActionRole(Enum):
    UNSET = None
    BUTTON = "Button"
    LINK = "Link"
    TAB = "Tab"
    MENU = "Menu"
    MENU_ITEM = "MenuItem"

class Material:
    def __init__(self):
        self.ensure_abstraction(Material)

    def ensure_abstraction(self, __class: type[Any]):
        if self.__class__ is __class:
            raise TypeError(f"Abstract class '{__class.__name__}' cannot be instantiated.")
    
    @staticmethod
    def read(__value: Any) -> Any:
        if isinstance(__value, (Enum, MaterialDynamic)):
            return __value.value

        if isinstance(__value, (AdaptiveCardMaterial, MaterialMapping)):
            return __value.__dict__

        if isinstance(__value, (list, tuple)):
            return [Material.read(item) for item in __value]
        
        return __value

class MaterialDynamic(Material):
    def __init__(self, __value: Any):
        self.ensure_abstraction(MaterialDynamic)
        self.__value = __value

    @property
    def value(self) -> Any:
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)

class Weight(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(__value)

class Seconds(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(__value)

class Pixels(MaterialDynamic):
    def __init__(self, __value: int):
        super().__init__(f"{__value}px")
   
class MaterialMapping(Material, Mapping):
    def __init__(self, **kwargs):

        self.ensure_abstraction(MaterialMapping)

        self.__data = dict()
        for key in kwargs:
            value = self.read(kwargs[key])
            if value is not None:
                self.__data[key] = value
    
    @property   
    def __dict__(self):
        return self.__data
    
    def __getitem__(self, __key: Any) -> Any:
        return self.__data.__getitem__(__key)

    def __len__(self) -> int:
        return len(self.__data)
    
    def __iter__(self):
        for key in self.__data:
            yield key
    
    def __str__(self) -> str:
        return dumps(self.__data)

class MaterialLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET
        ):

        super().__init__(
            separator=separator, 
            spacing=spacing
        )

class AdaptiveCardMaterial(Material, ABC): 
    def __init__(
            self, 
            __type: MaterialType,
            id: Optional[str]=None,
            visible: bool=True,
            **kwargs
        ):
        self.ensure_abstraction(AdaptiveCardMaterial)

        self.__data: dict[str, Any] = dict(type=__type.value)

        if "type" in kwargs:
            del kwargs["type"]
        
        if id:
            self.__data["id"] = id

        if not visible:
            self.__data["isVisible"] = False

        for key in kwargs:
            value = self.read(kwargs[key])
            if value is not None:
                self.__data[key] = value
    
    @property
    def type(self) -> MaterialType:
        return MaterialType(self.__data["type"])
    
    @property
    def id(self) -> str:
        return self.__data.get("id")
    
    @overload
    def get(self, __key: str) -> object:
        return self.__data.get(__key)
    
    @overload
    def get(self, __key: str, __default: Any) -> object:
        return self.__data.get(__key, __default)
    
    def get(self, __key: str, *args) -> object:
        if args:
            return self.__data.get(__key, args[0])
        
        return self.__data.get(__key)
    
    def update(self, **kwargs):
        if "type" in kwargs:
            raise KeyError(f"You cannot change the attribute type of any '{self.__class__.__name__}' object.")
        
        for key in kwargs:
            value = self.read(kwargs[key])

            if value is None:
                if key in self.__data:
                    del self.__data[key]
            else:
                self.__data[key] = value
    
    def using(self, __data) -> AdaptiveCardMaterial:
        self.__data["$data"] = __data
        return self

    def when(self, __condition: str) -> AdaptiveCardMaterial:
        self.__data["$when"] = __condition
        return self
    
    @staticmethod
    @abstractmethod
    def empty() -> AdaptiveCardMaterial:
        pass
    
    @classmethod
    def from_dict(cls, __data: dict) -> AdaptiveCardMaterial:
        __data = __data.copy()
        __data_type = __data.pop("type", None)
        
        component = cls.empty()
        
        if __data_type and component.type != __data_type:
            raise TypeError(f"Mismatching types. Cannot create an instance of '{component.__class__.__name__}' from a dictionary with its property 'type' being '{__data_type}'. Expected type was '{component.type}'.")
        
        component.update(**__data)
        return component

    @staticmethod
    def ensure_iterable_typing(__iterable: Optional[Iterable[object]], *__types: type[Any]):
        if __iterable:
            __types = __types if __types else tuple([AdaptiveCardMaterial])
            for index, item in enumerate(__iterable):
                if isinstance(item, __types):
                    continue
                    
                raise TypeError(f"Item at index {index} is not of a valid type. Valid types are: {', '.join([t.__name__ for t in __types])}.")
 
    def __getitem__(self, __key: Any) -> Any:
        return self.__data.__getitem__(__key)

    def __len__(self) -> int:
        return len(self.__data)
    
    @property
    def __dict__(self) -> dict:
        return self.__data
    
    def __str__(self) -> str:
        return dumps(self.__data)
    
    def __iter__(self):
        for key in self.__data:
            yield key

class BackgroundFillMode(Enum):
    UNSET = None
    COVER = "Cover"
    REPEAT = "Repeat"
    REPEAT_HORIZONTALLY = "RepeatHorizontally"
    REPEAT_VERTICALLY = "RepeatVertically"

class BackgroundImage(MaterialMapping):
    def __init__(
            self,
            __url: str,
            fill: BackgroundFillMode=BackgroundFillMode.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            vertical_alignment: VerticalAlignment=VerticalAlignment.UNSET  
        ):
        data = dict(url=__url)

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
            __type: ActionType,
            title: str, 
            tooltip: Optional[str]=None,
            enabled: bool=True,
            icon_url: Optional[str]=None,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            id: Optional[str]=None,
            **kwargs):
        
        self.ensure_abstraction(AdaptiveCardAction)
        
        super().__init__(
            __type,
            id=id,
            title=title, 
            tooltip=tooltip,
            isEnabled=False if not enabled else None,
            iconUrl=icon_url,
            mode=mode,
            style=theme,
            role=role,
            **kwargs
        )

    @staticmethod
    @abstractmethod
    def empty() -> AdaptiveCardAction:
        pass

__all__ = [
    'MaterialType',
    'ActionType',
    'InputType',
    'MaterialColor',
    'MaterialHeight',
    'MaterialOrientation',
    'HorizontalAlignment',
    'VerticalAlignment',
    'MaterialSpacing',
    'ActionTheme',
    'ActionMode',
    'ActionRole',
    'Material',
    'MaterialDynamic',
    'Weight',
    'Seconds',
    'Pixels',
    'MaterialMapping',
    'MaterialLayout',
    'AdaptiveCardMaterial',
    'BackgroundFillMode',
    'BackgroundImage',
    'AdaptiveCardAction'
]