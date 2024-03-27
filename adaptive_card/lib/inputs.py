from __future__ import annotations
from .material import *
from datetime import date, time

class InputValidation(MaterialMapping):
    def __init__(
            self,
            required: bool=False,
            error_message: str | None=None
        ):

        if required and not error_message:
            raise ValueError("Property 'error_message' cannot be empty or null when property 'required' is True.")
        
        super().__init__(required=required, error_message=error_message)

class InputLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET):
        
        super().__init__(
            separator=separator, 
            spacing=spacing, 
            height=height
        )

class AdaptiveCardInput(AdaptiveCardMaterial):
    def __init__(
            self,
            __type: InputTypes,
            id: str,
            label: str | None=None,
            default: Any | None=None,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            visible: bool=True,
            **kwargs
        ):
        
        not_instantiatable(self, AdaptiveCardInput)
        
        super().__init__(
            __type,
            id=id,
            visible=visible,
            label=label,
            value=default,
            **layout or {},
            **validation or {},
            **kwargs
        )   

class ChoiceSetStyles(Enum):
    UNSET = None
    COMPACT = "compact"
    EXPANDED = "expanded"
    FILTERED = "filtered"

class InputChoice(MaterialMapping):
    def __init__(self, title: str, value: str):
        super().__init__(title=title, value=value)

class InputChoiceSet(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: str,
            choices: List[InputChoice],
            placeholder: str | None=None,
            default: str | None=None,
            style: ChoiceSetStyles=ChoiceSetStyles.UNSET,
            enable_multi_selection: bool=False,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            wrap: bool=False,
            visible: bool=True):
        
        super().ensure_list_items_typing(choices, InputChoice)

        if isinstance(default, InputChoice):
            default = default.get("title") if style is ChoiceSetStyles.FILTERED and not enable_multi_selection else default.get("value")
        
        super().__init__(
            InputTypes.CHOICE_SET,
            id=id,
            label=label,
            default=default,
            validation=validation,
            layout=layout,
            visible=visible,
            choices=choices,
            placeholder=placeholder,
            isMultiSelect=enable_multi_selection or None,
            style=style,
            wrap=wrap or None
        )

class InputTextValidation(MaterialMapping):
    def __init__(
            self,
            required: bool=False,
            error_message: str | None=None,
            pattern: str | None=None
        ):

        if required and not error_message:
            raise ValueError("Property 'error_message' cannot be empty or null when property 'required' is True.")
        
        super().__init__(isRequired=required, errorMessage=error_message, regex=pattern)

class InputTextStyles(Enum):
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
            label: str,
            placeholder: str | None=None,
            default: str | None=None,
            multiline: bool=False,
            maximum_length: int | None=None,
            layout: InputLayout | None=None,
            validation: InputTextValidation | None=None,
            inline_action: AdaptiveCardAction | None=None,
            style: InputTextStyles=InputTextStyles.UNSET,
            visible: bool=True
        ):
        
        super().__init__(
            InputTypes.TEXT,
            id=id,
            label=label,
            default=default,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            isMultiline=multiline,
            maxLength=maximum_length,
            style=style,
            inlineAction=inline_action
        )
    
class InputNumber(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: str,
            placeholder: str | None=None,
            default: int | None=None,
            minimum_value: int | None=None,
            maximum_value: int | None=None,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            visible: bool=True,  
        ):
        super().__init__(
            InputTypes.NUMBER,
            id=id,
            label=label,
            default=default,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value,
            max=maximum_value
        )

class InputDate(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: str,
            placeholder: str | None=None,
            default: date | None=None,
            minimum_value: date | None=None,
            maximum_value: date | None=None,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            visible: bool=True,
        ):
        super().__init__(
            InputTypes.DATE,
            id=id,
            label=label,
            default=default.isoformat() if default else None,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value.isoformat() if minimum_value else None,
            max=maximum_value.isoformat() if maximum_value else None
        )

class InputTime(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            label: str,
            placeholder: str | None=None,
            default: time | None=None,
            minimum_value: time | None=None,
            maximum_value: time | None=None,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            visible: bool=True,
        ):
        super().__init__(
            InputTypes.DATE,
            id=id,
            label=label,
            default=default.strftime("%H:%M") if default else None,
            validation=validation,
            layout=layout,
            visible=visible,
            placeholder=placeholder,
            min=minimum_value.strftime("%H:%M") if minimum_value else None,
            max=maximum_value.strftime("%H:%M") if maximum_value else None
        )

class InputToggle(AdaptiveCardInput):
    def __init__(
            self,
            id: str,
            title: str,
            label: str | None=None,
            value_when_on: str="true",
            value_when_off: str="false",
            default: str | None=None,
            validation: InputValidation | None=None,
            layout: InputLayout | None=None,
            visible: bool=True,
        ):
        super().__init__(
            InputTypes.DATE,
            id=id,
            label=label,
            default=default,
            validation=validation,
            layout=layout,
            visible=visible,
            title=title,
            valueOn=value_when_on,
            valueOff=value_when_off
        )