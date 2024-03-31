from __future__ import annotations
from .material import *

class TextTheme(Enum):
    UNSET = None
    DEFAULT = "default"
    HEADING = "heading"
    COLUMN_HEADER = "columnHeader"

class FontType(Enum):
    UNSET = None
    DEFAULT = "Default"
    MONOSPACE = "Monospace"

class TextSize(Enum):
    UNSET = None
    SMALL = "Small"
    DEFAULT = "Default"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "ExtraLarge"

class FontWeight(Enum):
    UNSET = None
    LIGHTER = "Lighter"
    DEFAULT = "Default"
    BOLDER = "Bolder"

class TextLayout(MaterialMapping):
    def __init__(
            self, 
            separator: bool=False, 
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            height: MaterialHeight=MaterialHeight.UNSET,
            maximum_lines: Optional[int]=None):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            height=height,
            maxLines=maximum_lines
        )

class TextStyle(MaterialMapping):
    def __init__(
            self,
            theme: TextTheme=TextTheme.UNSET,
            font: FontType=FontType.UNSET,
            size: TextSize=TextSize.UNSET,
            weight: FontWeight=FontWeight.UNSET,
            color: MaterialColor=MaterialColor.UNSET,
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
            layout: Optional[TextLayout]=None,
            style: Optional[TextStyle]=None,
            wrap: bool=True,
            visible: bool=True,
            id: Optional[str]=None):
        
        super().__init__(
            MaterialType.TEXT_BLOCK,
            id=id,
            visible=visible,
            text=__text,
            wrap=wrap,
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> TextBlock:
        return TextBlock("")

class ImageSize(Enum):
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
            spacing: MaterialSpacing=MaterialSpacing.UNSET,
            horizontal_alignment: HorizontalAlignment=HorizontalAlignment.UNSET,
            size: ImageSize=ImageSize.UNSET,
            height: Optional[Pixels]=None,
            width: Optional[Pixels]=None):
        
        super().__init__(
            separator=separator or None,
            spacing=spacing,
            horizontalAlignment=horizontal_alignment,
            size=size,
            height=height,
            width=width
        )

class ImageTheme(Enum):
    UNSET = None
    DEFAULT = "Default"
    PERSON = "Person"

class ImageStyle(MaterialMapping):
    def __init__(
            self,
            theme: ImageTheme=ImageTheme.UNSET,
            background_color: Optional[str]=None):
        
        super().__init__(
            style=theme,
            backgroundColor=background_color
        )

class Image(AdaptiveCardMaterial):
    def __init__(
            self,
            __url: str,
            alternate_text: Optional[str]=None,
            layout: Optional[ImageLayout]=None,
            style: Optional[ImageStyle]=None,
            select_action: Optional[AdaptiveCardAction]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        super().__init__(
            MaterialType.IMAGE,
            id=id,
            visible=visible,
            url=__url,
            altText=alternate_text,
            selectAction=select_action,
            **layout or {},
            **style or {}
        )
    
    @staticmethod
    def empty() -> Image:
        return Image("")

class MediaLayout(MaterialMapping):
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

class MediaMimeType(Enum):
    MP4 = "video/mp4"
    WEBM = "video/webm"
    MPEG = "video/mpeg"

class CaptionMimeType(Enum):
    WEBVTT = "text/vtt"
    SRT = "text/srt"
    TTML = "application/ttml+xml"
    DFXP = "application/ttaf+xml"

class MediaSource(MaterialMapping):
    def __init__(self, __url: str, mime_type: Optional[MediaMimeType | str]=None):
        
        super().__init__(
            url=__url,
            mimeType=mime_type
        )

class MediaCaptions(MaterialMapping):
    def __init__(self, __url: str, label: str, mime_type: Optional[CaptionMimeType | str]=None):
        
        super().__init__(
            url=__url,
            label=label,
            mimeType=mime_type
        )

class Media(AdaptiveCardMaterial):
    def __init__(
            self,
            *sources: MediaSource,
            captions: Optional[List[MediaCaptions]]=None,
            alternate_text: Optional[str]=None,
            layout: Optional[MediaLayout]=None,
            visible: bool=True,
            id: Optional[str]=None):
        
        self.ensure_iterable_typing(sources, MediaSource)
        self.ensure_iterable_typing(captions, MediaCaptions)

        super().__init__(
            MaterialType.MEDIA,
            id=id,
            visible=visible,
            sources=sources,
            captionSources=captions,
            altText=alternate_text,
            **layout or {}
        )
    
    @staticmethod
    def empty() -> Media:
        return Media()