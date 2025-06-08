from __future__ import annotations
from typing import List, Optional
from enum import Enum

from .material import *
from .adaptive_card import AdaptiveCard


class MSTeams(MaterialMapping):
    def __init__(self, __type: str, **kwargs):
        super().__init__(type=__type, **kwargs)

    @staticmethod
    def message_back(text: str, value: Optional[str]=None, display_text: Optional[str]=None):
        return MSTeams("messageBack", text=text, value=value, displayText=display_text)

    @staticmethod
    def im_back(value: str):
        return MSTeams("imBack", value=value)
    
    @staticmethod
    def invoke(action: str, value: Optional[dict | str]=None):
        return MSTeams(action, value=value)
    
    @staticmethod
    def sign_in(url: str):
        return MSTeams("signin", value=url)

class ActionData(MaterialMapping):
    def __init__(
            self, 
            msteams: Optional[MSTeams]=None,
            **kwargs
        ):

        super().__init__(msTeams=msteams, **kwargs)

class AssociatedInputs(Enum):
    AUTO = "auto"
    NONE = "none"

class ActionSubmit(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            tooltip: Optional[str]=None,
            enabled: bool=True,
            icon_url: Optional[str]=None, 
            data: Optional[ActionData | dict | str]=None,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            associated_inputs: AssociatedInputs=AssociatedInputs.AUTO,
            auto_disable: bool=False,
            id: Optional[str]=None):
        
        super().__init__(
            ActionType.SUBMIT,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            role=role,
            icon_url=icon_url,
            theme=theme,
            id=id,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputssChange=auto_disable or None
        )
    
    @staticmethod
    def empty() -> ActionSubmit:
        return ActionSubmit(title="")
    
class ActionOpenUrl(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            url: str,
            tooltip: Optional[str]=None,
            enabled: bool=True,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            icon_url: Optional[str]=None, 
            id: Optional[str]=None):

        super().__init__(
            ActionType.OPEN_URL,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            theme=theme,
            role=role,
            id=id,
            url=url
        )
    
    @staticmethod
    def empty() -> ActionOpenUrl:
        return ActionOpenUrl(title="", url="")

class ActionShowCard(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            card: AdaptiveCard,
            tooltip: Optional[str]=None,
            enabled: bool=True,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            icon_url: Optional[str]=None, 
            id: Optional[str]=None):

        super().__init__(
            ActionType.SHOW_CARD,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            theme=theme,
            role=role,
            id=id,
            card=card
        )
    
    @staticmethod
    def empty() -> ActionShowCard:
        return ActionShowCard(title="", card=AdaptiveCard.empty())

class TargetFreezing(Enum):
    NONE = None
    VISIBILITY = True
    INVISIBIITY = False

class TargetElement(AdaptiveCardMaterial):
    def __init__(self, __id: str, freeze: TargetFreezing=TargetFreezing.NONE):

        super().__init__(
            MaterialType.TARGET_ELEMENT,
            elementId=__id, 
            isVisible=freeze
        )
    
    @staticmethod
    def empty() -> TargetElement:
        return TargetElement("")

class ActionToggleVisibility(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            target_element_ids: List[str | TargetElement],
            tooltip: Optional[str]=None,
            enabled: bool=True,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            icon_url: Optional[str]=None, 
            id: Optional[str]=None):

        self.ensure_iterable_typing(target_element_ids, str, TargetElement)
        
        super().__init__(
            ActionType.TOGGLE_VISIBILITY,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            theme=theme,
            role=role,
            id=id,
            targetElements=target_element_ids
        )
    
    @staticmethod
    def empty() -> ActionToggleVisibility:
        return ActionToggleVisibility(title="", target_element_ids=[])

class ActionExecute(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            tooltip: Optional[str]=None,
            enabled: bool=True,
            verb: Optional[str]=None,
            data: Optional[dict | str]=None,
            icon_url: Optional[str]=None, 
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            associated_inputs: AssociatedInputs=AssociatedInputs.AUTO,
            auto_disable: bool=False,
            id: Optional[str]=None):
        
        super().__init__(
            ActionType.EXECUTE,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            theme=theme,
            icon_url=icon_url,
            role=role,
            id=id,
            verb=verb,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputssChange=auto_disable or None
        )
    
    @staticmethod
    def empty() -> ActionExecute:
        return ActionExecute(title="")

class ActionSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False,
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alighment: HorizontalAlignment=HorizontalAlignment.UNSET,
            height: Optional[MaterialHeight]=None):
        
        super().__init__(
            separator=separator, 
            spacing=spacing, 
            horizontalAlignment=horizontal_alighment if horizontal_alighment else None,
            height=height if height else None
        )

class ActionSet(AdaptiveCardMaterial):
    def __init__(
            self,
            actions: List[AdaptiveCardAction]=[],
            layout: Optional[ActionSetLayout]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(actions, AdaptiveCardAction)
        
        super().__init__(
            MaterialType.ACTION_SET, 
            id=id, 
            visible=visible, 
            actions=actions, 
            **layout or {}
        )
    
    @staticmethod
    def empty() -> ActionSet:
        return ActionSet()
    
__all__ = [
    'AssociatedInputs', 
    'ActionSubmit', 
    'ActionOpenUrl', 
    'ActionShowCard', 
    'TargetFreezing', 
    'TargetElement', 
    'ActionToggleVisibility', 
    'ActionExecute', 
    'ActionSetLayout', 
    'ActionSet',
    'MSTeams',
    'ActionData'
]