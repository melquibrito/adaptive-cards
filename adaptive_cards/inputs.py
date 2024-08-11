from __future__ import annotations
from typing import List, Optional, Any
from abc import ABC, abstractmethod
from datetime import date, time
from enum import Enum

from .material import *

class InputValidation(MaterialMapping):
    def __init__(
            self,
            required: bool=False,
            error_message: Optional[str]=None
        ):

        if required and not error_message:
            raise ValueError("Property 'error_message' cannot be empty or null when property 'required' is True.")
        
        super().__init__(isRequired=required, errorMessage=error_message)

class InputLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET):
        
        super().__init__(
            separator=separator, 
            spacing=spacing, 
            height=height
        )

class AdaptiveCardInput(AdaptiveCardMaterial, ABC):
    def __init__(
            self,
            __type: InputType,
            id: str,
            label: Optional[str]=None,
            value: Optional[Any]=None,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            visible: bool=True,
            **kwargs
        ):
        
        self.ensure_abstraction(AdaptiveCardInput)
        
        super().__init__(
            __type,
            id=id,
            visible=visible,
            label=label,
            value=value,
            **layout or {},
            **validation or {},
            **kwargs
        )

    @staticmethod
    @abstractmethod
    def empty() -> AdaptiveCardInput:
        pass
    
class ChoiceSetMode(Enum):
    UNSET = None
    COMPACT = "compact"
    EXPANDED = "expanded"
    FILTERED = "filtered"

class InputChoice(MaterialMapping):
    def __init__(self, __title: str, __value: Optional[str]=None):
        super().__init__(title=__title, value=__value or __title)

class InputChoiceSet(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            choices: List[InputChoice]=[],
            label: Optional[str]=None,
            placeholder: Optional[str]=None,
            value: Optional[str]=None,
            mode: ChoiceSetMode=ChoiceSetMode.UNSET,
            enable_multi_selection: bool=False,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            wrap: bool=False,
            visible: bool=True):
        
        self.ensure_iterable_typing(choices, InputChoice)

        if isinstance(value, InputChoice):
            value = value.get("title") if mode is ChoiceSetMode.FILTERED and not enable_multi_selection else value.get("value")
        
        super().__init__(
            InputType.CHOICE_SET,
            id=id,
            label=label,
            value=value,
            validation=validation,
            layout=layout,
            visible=visible,
            choices=choices,
            placeholder=placeholder,
            isMultiSelect=enable_multi_selection or None,
            style=mode,
            wrap=wrap or None
        )
    
    @staticmethod
    def empty() -> InputChoiceSet:
        return InputChoiceSet(id="", label="", choices=[])

class InputTextValidation(MaterialMapping):
    def __init__(
            self,
            required: bool=False,
            error_message: Optional[str]=None,
            pattern: Optional[str]=None
        ):

        if required and not error_message:
            raise ValueError("Property 'error_message' cannot be empty or null when property 'required' is True.")
        
        super().__init__(isRequired=required, errorMessage=error_message, regex=pattern)

class InputTextMode(Enum):
    UNSET = None
    TEXT = "Text"
    TEL = "Tel"
    URL = "Url"
    EMAIL = "Email"
    PASSWORD = "Password"

class InputText(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: Optional[str]=None,
            placeholder: Optional[str]=None,
            value: Optional[str]=None,
            multiline: bool=False,
            maximum_length: Optional[int]=None,
            layout: Optional[InputLayout]=None,
            validation: Optional[InputTextValidation]=None,
            inline_action: Optional[AdaptiveCardAction]=None,
            mode: InputTextMode=InputTextMode.UNSET,
            visible: bool=True):
        
        super().__init__(
            InputType.TEXT,
            id=id,
            label=label,
            value=value,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            isMultiline=multiline,
            maxLength=maximum_length,
            style=mode,
            inlineAction=inline_action
        )
    
    @staticmethod
    def empty() -> InputText:
        return InputText(id="", label="")
    
class InputNumber(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: Optional[str]=None,
            placeholder: Optional[str]=None,
            value: Optional[int]=None,
            minimum_value: Optional[int]=None,
            maximum_value: Optional[int]=None,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            visible: bool=True,  
        ):
        super().__init__(
            InputType.NUMBER,
            id=id,
            label=label,
            value=value,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value,
            max=maximum_value
        )
    
    @staticmethod
    def empty() -> InputNumber:
        return InputNumber(id="", label="")

class InputDate(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: Optional[str]=None,
            placeholder: Optional[str]=None,
            value: Optional[date]=None,
            minimum_value: Optional[date]=None,
            maximum_value: Optional[date]=None,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            visible: bool=True,
        ):
        super().__init__(
            InputType.DATE,
            id=id,
            label=label,
            value=value.isoformat() if value else None,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value.isoformat() if minimum_value else None,
            max=maximum_value.isoformat() if maximum_value else None
        )
    
    @staticmethod
    def empty() -> InputDate:
        return InputDate(id="", label="")

class InputTime(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: Optional[str]=None,
            placeholder: Optional[str]=None,
            value: Optional[time]=None,
            minimum_value: Optional[time]=None,
            maximum_value: Optional[time]=None,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            visible: bool=True,
        ):
        super().__init__(
            InputType.DATE,
            id=id,
            label=label,
            value=value.strftime("%H:%M") if value else None,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value.strftime("%H:%M") if minimum_value else None,
            max=maximum_value.strftime("%H:%M") if maximum_value else None
        )

    @staticmethod
    def empty() -> InputTime:
        return InputTime(id="", label="")
    
class InputToggle(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            title: str,
            label: Optional[str]=None,
            value_when_on: str="true",
            value_when_off: str="false",
            value: Optional[str]=None,
            validation: Optional[InputValidation]=None,
            layout: Optional[InputLayout]=None,
            visible: bool=True,
        ):
        super().__init__(
            InputType.TOGGLE,
            id=id,
            label=label,
            value=value,
            validation=validation,
            layout=layout,
            visible=visible,
            title=title,
            valueOn=value_when_on,
            valueOff=value_when_off
        )
    
    @staticmethod
    def empty() -> InputToggle:
        return InputToggle(id="", title="")
    
__all__ = [
    'InputValidation',
    'InputLayout',
    'AdaptiveCardInput',
    'ChoiceSetMode',
    'InputChoice',
    'InputChoiceSet',
    'InputTextValidation',
    'InputTextMode',
    'InputText',
    'InputNumber',
    'InputDate',
    'InputTime',
    'InputToggle'
]