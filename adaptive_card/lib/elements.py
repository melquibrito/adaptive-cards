from .material import *

class TextThemes(Enum):
    UNSET = None
    DEFAULT = "default"
    HEADING = "heading"
    COLUMN_HEADER = "columnHeader"

class FontTypes(Enum):
    UNSET = None
    DEFAULT = "Default"
    MONOSPACE = "Monospace"

class TextSizes(Enum):
    UNSET = None
    SMALL = "Small"
    DEFAULT = "Default"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "ExtraLarge"

class FontWeights(Enum):
    UNSET = None
    LIGHTER = "Lighter"
    DEFAULT = "Default"
    BOLDER = "Bolder"

class TextLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            wrap: bool=True,
            maximum_lines: int | None=None):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height,
            wrap=wrap,
            maxLines=maximum_lines
        )

class TextStyle(MaterialMapping):
    def __init__(
            self,
            theme: TextThemes=TextThemes.UNSET,
            font: FontTypes=FontTypes.UNSET,
            size: TextSizes=TextSizes.UNSET,
            weight: FontWeights=FontWeights.UNSET,
            color: MaterialColors=MaterialColors.UNSET,
            subtle: bool=False):
        
        super().__init__(
            style=theme,
            fontType=font,
            size=size,
            weight=weight,
            color=color,
            isSubtle=subtle or None
        )

class TextBlock(AdaptiveCardMaterial):
    def __init__(
            self,
            __text: str,
            layout: TextLayout | None=None,
            style: TextStyle | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().__init__(
            MaterialTypes.TEXT_BLOCK,
            id=id,
            visible=visible,
            text=__text,
            **layout or {},
            **style or {}
        )

class ImageSizes(Enum):
    UNSET = None
    AUTO = "Auto"
    STRETCH = "Stretch"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class ImageLayout(MaterialMapping):
    def __init__(
            self,
            separator: bool=False, 
            spacing: MaterialSpacings=MaterialSpacings.UNSET,
            horizontal_alignment: HorizontalAlignments=HorizontalAlignments.UNSET,
            size: ImageSizes=ImageSizes.UNSET,
            height: Pixels | None=None,
            width: Pixels | None=None):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            size=size,
            height=height,
            width=width
        )

class ImageThemes(Enum):
    UNSET = None
    DEFAULT = "Default"
    PERSON = "Person"

class ImageStyle(MaterialMapping):
    def __init__(
            self,
            theme: ImageThemes=ImageThemes.UNSET,
            background_color: str | None=None):
        
        super().__init__(
            style=theme,
            backgroundColor=background_color
        )

class Image(AdaptiveCardMaterial):
    def __init__(
            self,
            __url: str,
            alternate_text: str | None=None,
            layout: ImageLayout | None=None,
            style: ImageStyle | None=None,
            visible: bool=True,
            id: str | None=None):
        
        super().__init__(
            MaterialTypes.IMAGE,
            id=id,
            visible=visible,
            url=__url,
            altText=alternate_text,
            **layout or {},
            **style or {}
        )

class Media(AdaptiveCardMaterial):
    def __init__(self):
        raise NotImplementedError()