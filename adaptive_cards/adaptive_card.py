from __future__ import annotations
from typing import List, Optional

from .material import *


class AdaptiveCardLayout(MaterialMapping):
    def __init__(
            self,
            minimum_height: Optional[Pixels]=None,
            vertical_content_alignment: VerticalAlignment=VerticalAlignment.UNSET,
            present_right_to_left: bool=False):
                
        super().__init__(
            minHeight=minimum_height.value if minimum_height else None,
            verticalContentAlignment=vertical_content_alignment.value,
            rtl=present_right_to_left
        )

class AdaptiveCard(AdaptiveCardMaterial):
    def __init__(
            self,
            body: List[AdaptiveCardMaterial]=[],
            actions: Optional[List[AdaptiveCardAction]]=None,
            select_action: Optional[AdaptiveCardAction]=None,
            layout: Optional[AdaptiveCardLayout]=None,
            background_image: Optional[BackgroundImage]=None,
            version: float=1.5,
            schema: Optional[str]=None,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(body)
        self.ensure_iterable_typing(actions, AdaptiveCardAction)

        super().__init__(
            MaterialType.ADAPTIVE_CARD, 
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
    
    @staticmethod
    def empty() -> AdaptiveCard:
        return AdaptiveCard()

__all__ = ['AdaptiveCardLayout', 'AdaptiveCard']