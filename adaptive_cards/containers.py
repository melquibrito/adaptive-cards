from __future__ import annotations
from typing import List, Optional
from enum import Enum

from .material import *
from .actions import AdaptiveCardAction
from .elements import Image, ImageSize


class ContainerTheme(Enum):
    UNSET = None
    DEFAULT = "default"
    EMPHASIS = "emphasis"
    ACCENT = "accent"
    GOOD = "good"
    ATTENTION = "attention"
    WARNING = "warning"

class ContainerStyle(MaterialMapping):
    def __init__(
            self, 
            theme: ContainerTheme=ContainerTheme.UNSET, 
            bleed: bool=False):
        
        super().__init__(style=theme, bleed=bleed)

class ContainerLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            vertical_content_alignment: VerticalAlignment=VerticalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            minimum_height: Optional[Pixels]=None,
            present_right_to_left: bool=False):
        
        super().__init__(
            separator=separator or None, 
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            verticalContentAlignment=vertical_content_alignment,
            height=height,
            minHeight=minimum_height,
            rtl=present_right_to_left or None
        )

class Container(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial]=[],
            layout: Optional[ContainerLayout]=None,
            style: Optional[ContainerStyle]=None,
            action: Optional[AdaptiveCardAction]=None,
            background_image: Optional[BackgroundImage]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(items)

        super().__init__(
            MaterialType.CONTAINER,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> Container:
        return Container()

class ColumnWidth(Enum):
    UNSET = None
    AUTO = "auto"
    STRETCH = "stretch"

class ColumnLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            vertical_content_alignment: VerticalAlignment=VerticalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            width: ColumnWidth | Weight | Pixels=ColumnWidth.UNSET,
            minimum_height: Optional[Pixels]=None,
            present_right_to_left: bool=False):
        
        super().__init__(
            separator=separator or None, 
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            verticalContentAlignment=vertical_content_alignment,
            height=height,
            width=width,
            minHeight=minimum_height,
            rtl=present_right_to_left or None
        )

class Column(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial]=[],
            layout: Optional[ColumnLayout]=None,
            style: Optional[ContainerStyle]=None,
            background_image: Optional[BackgroundImage]=None,
            action: Optional[AdaptiveCardAction]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(items)

        super().__init__(
            MaterialType.COLUMN,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )

    @staticmethod
    def empty() -> Column:
        return Column()

class ColumnSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: VerticalAlignment=VerticalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            minimum_height: Optional[Pixels]=None):

        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height,
            minHeight=minimum_height
        )

class ColumnSet(AdaptiveCardMaterial):
    def __init__(
            self,
            columns: List[Column]=[],
            layout: Optional[ColumnSetLayout]=None,
            style: Optional[ContainerStyle]=None,
            action: Optional[AdaptiveCardAction]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(columns, Column)

        super().__init__(
            MaterialType.COLUMN_SET,
            id=id,
            visible=visible,
            columns=columns,
            selectAction=action,
            **layout or {},
            **style or {}        
        )
    
    @staticmethod
    def empty() -> ColumnSet:
        return ColumnSet()

class FactSetLayout(MaterialMapping):
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

class Fact(MaterialMapping):
    def __init__(self, title: str, value: str):
        super().__init__(title=title, value=value)

class FactSet(AdaptiveCardMaterial):
    def __init__(
            self,
            facts: List[Fact]=[],
            layout: Optional[FactSetLayout]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(facts, Fact)

        super().__init__(
            MaterialType.FACT_SET,
            id=id,
            visible=visible,
            facts=facts,
            **layout or {}
        )
    
    @staticmethod
    def empty() -> FactSet:
        return FactSet()

class ImageSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET):

        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height
        )

class ImageSet(AdaptiveCardMaterial):
    def __init__(
            self,
            images: List[Image]=[],
            layout: Optional[ImageSetLayout]=None,
            image_size: ImageSize=ImageSize.UNSET,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(images, Image)

        super().__init__(
            MaterialType.IMAGE_SET,
            id=id,
            visible=visible,
            images=images,
            imageSize=image_size,
            **layout or {}
        )
    
    @staticmethod
    def empty() -> ImageSet:
        return ImageSet()

class TableLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            horizontal_cell_content_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            vertical_cell_content_alignment: VerticalAlignment=VerticalAlignment.UNSET):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height,
            horizontalCellContentAlignment=horizontal_cell_content_alignment,
            verticalCellContentAlignment=vertical_cell_content_alignment
        )

class TableCell(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial]=[],
            layout: Optional[ContainerLayout]=None,
            style: Optional[ContainerStyle]=None,
            action: Optional[AdaptiveCardAction]=None,
            background_image: Optional[BackgroundImage]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(items)

        super().__init__(
            MaterialType.TABLE_CELL,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> TableCell:
        return TableCell()

class TableRow(AdaptiveCardMaterial):
    def __init__(
            self,
            cells: List[TableCell]=[],
            layout: Optional[TableLayout]=None,
            theme: ContainerTheme=ContainerTheme.UNSET,
            visible: bool=True,
            id: Optional[str]=None):

        self.ensure_iterable_typing(cells, TableCell)

        super().__init__(
            MaterialType.TABLE_ROW,
            id=id,
            visible=visible,
            cells=cells,
            style=theme,
            **layout or {}
        )
    
    @staticmethod
    def empty() -> TableRow:
        return TableRow()

class GridStyle(MaterialMapping):
    def __init__(
            self,
            theme: Optional[ContainerTheme]=None,
            lines: bool=True):
        
        super().__init__(
            gridStyle=theme,
            showGridLines=lines
        )

class Table(AdaptiveCardMaterial):
    def __init__(
            self,
            rows: List[TableRow]=[],
            columns: Optional[List[Weight | Pixels] | int]=None,
            layout: Optional[TableLayout]=None,
            style: Optional[GridStyle]=None,
            first_row_as_headers: bool=True,
            visible: bool=True,
            id: Optional[str]=None):

        self.ensure_iterable_typing(rows, TableRow)

        if columns is None:
            columns = len(max([r.get("cells") for r in rows], key=len)) if rows else 1

        if isinstance(columns, int):
            columns = [dict(width=1) for _ in range(columns)]
        elif isinstance(columns, list):
            self.ensure_iterable_typing(columns, Weight, Pixels)
            columns = [dict(width=col.value) for col in columns]
        
        super().__init__(
            MaterialType.TABLE,
            id=id,
            visible=visible,
            columns=columns,
            rows=rows,
            firstRowAsHeaders=first_row_as_headers,
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> Table:
        return Table()

class CarouselPage(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial]=[],
            layout: Optional[ContainerLayout]=None,
            style: Optional[ContainerStyle]=None,
            action: Optional[AdaptiveCardAction]=None,
            background_image: Optional[BackgroundImage]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(items)

        super().__init__(
            MaterialType.CAROUSEL_PAGE,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> CarouselPage:
        return CarouselPage()

class Carousel(AdaptiveCardMaterial):
    def __init__(
            self,
            pages: List[CarouselPage]=[],
            layout: Optional[ContainerLayout]=None,
            timer: Seconds=Seconds(5000),
            initial_page: int=0,
            orientation: MaterialOrientation=MaterialOrientation.UNSET,
            height: Optional[Pixels]=None,
            loop: bool=True,
            background_image: Optional[BackgroundImage]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(pages, CarouselPage)

        last_page = len(pages) - 1

        if initial_page<0:
            initial_page = 0

        if initial_page>last_page:
            initial_page = last_page
        
        super().__init__(
            MaterialType.CAROUSEL,
            id=id,
            visible=visible,
            pages=pages,
            timer=timer,
            initialPage=initial_page,
            orientation=orientation,
            heightInPixels=height,
            loop=loop,
            **background_image or {},
            **layout or {}
        )
    
    @staticmethod
    def empty() -> Carousel:
        return Carousel()
    
__all__ = [
    'ContainerTheme',
    'ContainerStyle',
    'ContainerLayout',
    'Container',
    'ColumnWidth',
    'ColumnLayout',
    'Column',
    'ColumnSetLayout',
    'ColumnSet',
    'FactSetLayout',
    'Fact',
    'FactSet',
    'ImageSetLayout',
    'ImageSet',
    'TableLayout',
    'TableCell',
    'TableRow',
    'GridStyle',
    'Table',
    'CarouselPage',
    'Carousel'
]