from __future__ import annotations
from .material import *

class AdaptiveCardLayout(MaterialMapping):
    def __init__(
            self,
            minimum_height: Pixels | None=None,
            vertical_content_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            present_right_to_left: bool=False):
                
        super().__init__(
            minHeight=minimum_height.value if minimum_height else None,
            verticalContentAlignment=vertical_content_alignment.value,
            rtl=present_right_to_left
        )

class AdaptiveCard(AdaptiveCardMaterial):
    def __init__(
            self,
            body: List[AdaptiveCardMaterial],
            actions: List[AdaptiveCardAction] | None=None,
            select_action: AdaptiveCardAction | None=None,
            layout: AdaptiveCardLayout | None=None,
            background_image: BackgroundImage | None=None,
            version: float=1.6,
            schema: str | None=None,
            id: str | None=None):
        
        super().ensure_list_items_typing(body)
        super().ensure_list_items_typing(actions, AdaptiveCardAction)

        super().__init__(
            MaterialTypes.ADAPTIVE_CARD, 
            body=body,
            id=id, 
            version=str(version),
            selectAction=select_action,
            actions=actions,
            **layout or {},
            **background_image or {}
        )

        if schema:
            self.update(**{"$schema": schema})