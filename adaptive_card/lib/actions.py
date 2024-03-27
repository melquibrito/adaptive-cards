from __future__ import annotations
from .material import *
from typing import List
from .adaptive_card import AdaptiveCard

class AssociatedInputs(Enum):
    AUTO = "auto"
    NONE = "none"

class Submit(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            tooltip: str=None,
            enabled: bool=True,
            icon_url: str | None=None, 
            data: dict | str | None=None,
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            associated_inputs: AssociatedInputs=AssociatedInputs.AUTO,
            auto_disable: bool=False,
            id: str | None=None):
        
        super().__init__(
            ActionTypes.SUBMIT,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            role=role,
            icon_url=icon_url,
            style=style,
            id=id,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputsChange=auto_disable or None
        )
    
class OpenUrl(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            url: str,
            tooltip: str=None,
            enabled: bool=True,
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            icon_url: str=None, 
            id: str | None=None):

        super().__init__(
            ActionTypes.OPEN_URL,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=style,
            role=role,
            id=id,
            url=url
        )

class ShowCard(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            card: AdaptiveCard,
            tooltip: str=None,
            enabled: bool=True,
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            icon_url: str=None, 
            id: str | None=None):

        super().__init__(
            ActionTypes.SHOW_CARD,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=style,
            role=role,
            id=id,
            card=card
        )

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
            tooltip: str=None,
            enabled: bool=True,
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            icon_url: str=None, 
            id: str | None=None):

        super().ensure_list_items_typing(target_element_ids, str, TargetElement)
        
        super().__init__(
            ActionTypes.TOGGLE_VISIBILITY,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            icon_url=icon_url,
            style=style,
            role=role,
            id=id,
            targetElements=target_element_ids
        )

class Execute(AdaptiveCardAction):
    def __init__(
            self, 
            title: str, 
            tooltip: str=None,
            enabled: bool=True,
            verb: str | None=None,
            data: dict | str | None=None,
            icon_url: str | None=None, 
            mode: ActionModes=ActionModes.UNSET,
            style: ActionStyles=ActionStyles.UNSET,
            role: ActionRoles=ActionRoles.UNSET,
            associated_inputs: AssociatedInputs=AssociatedInputs.AUTO,
            auto_disable: bool=False,
            id: str | None=None):
        
        super().__init__(
            ActionTypes.EXECUTE,
            title=title,
            tooltip=tooltip,
            enabled=enabled,
            mode=mode,
            style=style,
            icon_url=icon_url,
            role=role,
            id=id,
            verb=verb,
            data=data,
            associatedInputs=associated_inputs,
            disabledUnlessAssociatedInputsChange=auto_disable or None
        )

class ActionSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False,
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alighment: HorizontalAlignments=HorizontalAlignments.UNSET,
            height: MaterialHeight | None=None):
        
        super().__init__(
            separator=separator, 
            spacing=spacing, 
            horizontalAlignment=horizontal_alighment if horizontal_alighment else None,
            height=height if height else None
        )

class ActionSet(AdaptiveCardMaterial):
    def __init__(
            self,
            actions: List[AdaptiveCardAction],
            layout: ActionSetLayout | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(actions, AdaptiveCardAction)
        
        super().__init__(
            MaterialTypes.ACTION_SET, 
            id=id, 
            visible=visible, 
            actions=actions, 
            **layout or {}
        )