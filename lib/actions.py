from __future__ import annotations
from .material import *
from typing import List
from .adaptive_card import AdaptiveCard

class AssociatedInput(Enum):
    AUTO = "auto"
    NONE = "none"

class Submit(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            tooltip: Optional[str]=None,
            enabled: bool=True,
            icon_url: Optional[str]=None, 
            data: Optional[dict | str]=None,
            mode: ActionMode=ActionMode.UNSET,
            theme: ActionTheme=ActionTheme.UNSET,
            role: ActionRole=ActionRole.UNSET,
            associated_inputs: AssociatedInput=AssociatedInput.AUTO,
            auto_disable: bool=False,
            id: Optional[str]=None):
        
        super().__init__(
            ActionTypes.SUBMIT,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            role=role,
            icon_url=icon_url,
            style=theme,
            id=id,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputsChange=auto_disable or None
        )
    
    @staticmethod
    def empty() -> Submit:
        return Submit(title="")
    
class OpenUrl(AdaptiveCardAction):
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
            ActionTypes.OPEN_URL,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=theme,
            role=role,
            id=id,
            url=url
        )
    
    @staticmethod
    def empty() -> OpenUrl:
        return OpenUrl(title="", url="")

class ShowCard(AdaptiveCardAction):
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
            ActionTypes.SHOW_CARD,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=theme,
            role=role,
            id=id,
            card=card
        )
    
    @staticmethod
    def empty() -> ShowCard:
        return ShowCard(title="", card=AdaptiveCard.empty())

class Freezing(Enum):
    NONE = None
    VISIBILITY = True
    INVISIBIITY = False

class TargetElement(MaterialMapping):
    def __init__(self, __id: str, freeze: Freezing=Freezing.NONE):

        super().__init__(
            elementId=__id, 
            isVisible=freeze
        )

class ToggleVisibility(AdaptiveCardAction):
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

        super().ensure_iterable_typing(target_element_ids, str, TargetElement)
        
        super().__init__(
            ActionTypes.TOGGLE_VISIBILITY,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=theme,
            role=role,
            id=id,
            targetElements=target_element_ids
        )
    
    @staticmethod
    def empty() -> ToggleVisibility:
        return ToggleVisibility(title="", target_element_ids=[])

class Execute(AdaptiveCardAction):
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
            associated_inputs: AssociatedInput=AssociatedInput.AUTO,
            auto_disable: bool=False,
            id: Optional[str]=None):
        
        super().__init__(
            ActionTypes.EXECUTE,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            style=theme,
            icon_url=icon_url,
            role=role,
            id=id,
            verb=verb,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputsChange=auto_disable or None
        )
    
    @staticmethod
    def empty() -> Execute:
        return Execute(title="")

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
            *__actions: AdaptiveCardAction,
            layout: Optional[ActionSetLayout]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        super().ensure_iterable_typing(__actions, AdaptiveCardAction)
        
        super().__init__(
            MaterialType.ACTION_SET, 
            id=id, 
            visible=visible, 
            actions=__actions, 
            **layout or {}
        )
    
    @staticmethod
    def empty() -> ActionSet:
        return ActionSet()