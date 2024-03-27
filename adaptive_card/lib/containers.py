from __future__ import annotations
from .material import *
from .actions import AdaptiveCardAction
from .elements import Image, ImageSizes

class ContainerThemes(Enum):
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
            theme: ContainerThemes=ContainerThemes.UNSET, 
            bleed: bool=False):
        
        super().__init__(style=theme, bleed=bleed)

class ContainerLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            vertical_content_alignment: VerticalAlignments=VerticalAlignments.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            minimum_height: Pixels | None=None,
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
            items: List[AdaptiveCardMaterial],
            layout: ContainerLayout | None=None,
            style: ContainerStyle | None=None,
            action: AdaptiveCardAction | None=None,
            background_image: BackgroundImage | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(items)

        super().__init__(
            MaterialTypes.CONTAINER,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )

class ColumnWidth(Enum):
    UNSET = None
    AUTO = "auto"
    STRETCH = "stretch"

class ColumnLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            vertical_content_alignment: VerticalAlignments=VerticalAlignments.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            width: ColumnWidth | Weight | Pixels=ColumnWidth.UNSET,
            minimum_height: Pixels | None=None,
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
            items: List[AdaptiveCardMaterial],
            layout: ColumnLayout | None=None,
            style: ContainerStyle | None=None,
            background_image: BackgroundImage | None=None,
            action: AdaptiveCardAction | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(items)

        super().__init__(
            MaterialTypes.COLUMN,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )

class ColumnSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: VerticalAlignments=VerticalAlignments.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            minimum_height: Pixels | None=None):

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
            columns: List[Column],
            layout: ColumnSetLayout | None=None,
            style: ContainerStyle | None=None,
            action: AdaptiveCardAction | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(columns, Column)

        super().__init__(
            MaterialTypes.COLUMN_SET,
            id=id,
            visible=visible,
            columns=columns,
            selectAction=action,
            **layout or {},
            **style or {}        
        )

class FactSetLayout(MaterialMapping):
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

class Fact(MaterialMapping):
    def __init__(self, title: str, value: str):
        super().__init__(title=title, value=value)

class FactSet(AdaptiveCardMaterial):
    def __init__(
            self,
            facts: List[Fact],
            layout: FactSetLayout | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(facts, Fact)

        super().__init__(
            MaterialTypes.FACT_SET,
            id=id,
            visible=visible,
            facts=facts,
            **layout or {}
        )

class ImageSetLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
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
            images: List[Image],
            layout: ImageSetLayout | None=None,
            image_size: ImageSizes=ImageSizes.UNSET,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(images, Image)

        super().__init__(
            MaterialTypes.IMAGE_SET,
            id=id,
            visible=visible,
            images=images,
            imageSize=image_size,
            **layout or {}
        )

class TableLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            horizontal_cell_content_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            vertical_cell_content_alignment: VerticalAlignments=VerticalAlignments.UNSET):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height,
            horizontalCellContentAlignment=horizontal_cell_content_alignment,
            verticalCellContentAlignment=vertical_cell_content_alignment
        )

class TableColumn(MaterialMapping):
    def __init__(self, __width: Pixels | Weight=Weight(1)):
        super().__init__(width=__width)

class TableCell(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial]=[],
            layout: ContainerLayout | None=None,
            style: ContainerStyle | None=None,
            action: AdaptiveCardAction | None=None,
            background_image: BackgroundImage | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(items)

        super().__init__(
            MaterialTypes.TABLE_CELL,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )

class TableRow(AdaptiveCardMaterial):
    def __init__(
            self,
            cells: List[TableCell],
            layout: TableLayout | None=None,
            theme: ContainerThemes=ContainerThemes.UNSET,
            visible: bool=True,
            id: str | None=None):

        super().ensure_list_items_typing(cells, TableCell)

        super().__init__(
            MaterialTypes.TABLE_ROW,
            id=id,
            visible=visible,
            cells=cells,
            style=theme,
            **layout or {}
        )

class GridStyle(MaterialMapping):
    def __init__(
            self,
            theme: ContainerThemes | None=None,
            lines: bool=True):
        
        super().__init__(
            gridStyle=theme,
            showGridLines=lines
        )

class Table(AdaptiveCardMaterial):
    def __init__(
            self,
            rows: List[TableRow],
            columns: List[TableColumn] | int | None=None,
            layout: TableLayout | None=None,
            style: GridStyle | None=None,
            first_row_as_headers: bool=True,
            visible: bool=True,
            id: str | None=None):

        if columns is None:
            columns = len(max([r.get("cells") for r in rows], key=len))

        if isinstance(columns, int):
            columns = [TableColumn() for _ in range(columns)]
        
        super().__init__(
            MaterialTypes.TABLE,
            id=id,
            visible=visible,
            columns=columns,
            rows=rows,
            firstRowAsHeaders=first_row_as_headers,
            **layout or {},
            **style or {}
        )

class CarouselPage(AdaptiveCardMaterial):
    def __init__(
            self,
            items: List[AdaptiveCardMaterial],
            layout: ContainerLayout | None=None,
            style: ContainerStyle | None=None,
            action: AdaptiveCardAction | None=None,
            background_image: BackgroundImage | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().ensure_list_items_typing(items)

        super().__init__(
            MaterialTypes.CAROUSEL_PAGE,
            id=id,
            visible=visible,
            items=items,
            selectAction=action,
            **background_image or {},
            **layout or {},
            **style or {}
        )

class Carousel(AdaptiveCardMaterial):
    def __init__(
            self,
            pages: List[CarouselPage],
            layout: ContainerLayout | None=None,
            timer: Seconds=Seconds(5000),
            initial_page: int=0,
            orientation: MaterialOrientation=MaterialOrientation.UNSET,
            height: Pixels | None=None,
            loop: bool=True,
            background_image: BackgroundImage | None=None,
            visible: bool=True,
            id: str | None=None):
        
        last_page = len(pages) - 1

        if initial_page<0:
            initial_page = 0

        if initial_page>last_page:
            initial_page = last_page
        
        super().__init__(
            MaterialTypes.CAROUSEL,
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