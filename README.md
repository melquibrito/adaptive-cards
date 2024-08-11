![](https://img.shields.io/badge/build-v1.3.2-green.svg) ![](https://img.shields.io/badge/python-3.7_|_3.8_|_3.9_|_3.10_|_3.11_|_3.12-yellow.svg)

# Adaptive Cards Framework
## Baseline
### What are Adaptive Cards? 
[Adaptive Cards](https://adaptivecards.io/) are platform-agnostic snippets of UI, authored in JSON, that apps and services can openly exchange. When delivered to a specific app, the JSON is transformed into native UI that automatically adapts to its surroundings. It helps design and integrate light-weight UI for all major platforms and frameworks.

### Why do I need a framework?
Building an application that effectively serves Adaptive Cards can be complex and time-consuming. Without a framework, you'd need to thoroughly navigate the entire Adaptive Cards documentation to ensure proper implementation, which can slow down development and hinder scalability. While tools like the [designer.io](https://adaptivecards.io/designer/) page can assist with prototyping and creating JSON components, relying solely on these can limit your application's growth potential. By leveraging a framework, you streamline the process, allowing you to focus on crafting your cards with confidence and efficiency, without the worry of underlying technical details.

## About
**adaptive-cards-io** is a Python package designed to simplify the creation, manipulation, and integration of Adaptive Cards in your applications. Adaptive Cards are a powerful way to build lightweight, responsive user interfaces that seamlessly adapt to different platforms and environments. With **adaptive-cards-io**, you can efficiently generate and manage these cards, ensuring they are optimized and correctly formatted for your specific needs.

This package offers a streamlined approach, allowing developers to focus on designing and deploying Adaptive Cards without getting bogged down by the intricacies of the underlying JSON structure. Whether you're building prototypes or scaling up to a production environment, **adaptive-cards-io** provides the tools and framework to enhance productivity and reduce development time.

## Installation
1. Make sure PIP is up-to-date:
```bash
python3 -m pip install --upgrade pip
```

2. Install the package:
```bash
python3 -m pip install adaptive-cards-io
```

## Usage
### Importing
```python
from adaptive_cards import *
```
By importing everything, all of the following will become available in your python module:

#### Enumerators
- MaterialType
- ActionType
- InputType
- MaterialColor
- MaterialHeight
- MaterialOrientation
- HorizontalAlignment
- VerticalAlignment
- MaterialSpacing
- ActionTheme
- ActionMode
- ActionRole
- BackgroundFillMode
- AssociatedInputs
- TargetFreezing
- ContainerTheme
- ColumnWidth
- TextTheme
- FontType
- TextSize
- FontWeight
- ImageSize
- ImageTheme
- MediaMimeType
- CaptionMimeType
- ChoiceSetMode
- InputTextMode

#### Building Blocks
- Material
- MaterialDynamic
- MaterialMapping
- MaterialLayout
- AdaptiveCardMaterial
- BackgroundImage
- AdaptiveCardAction

#### Units
- Weight
- Seconds
- Pixels

#### Base
- AdaptiveCardLayout
- AdaptiveCard

#### Actions
- ActionSubmit
- ActionOpenUrl
- ActionShowCard
- ActionToggleVisibility
- TargetElement
- ActionExecute
- ActionSetLayout
- ActionSet
- MSTeams
- ActionData

#### Containers
- ContainerStyle
- ContainerLayout
- Container
- ColumnLayout
- Column
- ColumnSetLayout
- ColumnSet
- FactSetLayout
- Fact
- FactSet
- ImageSetLayout
- ImageSet
- TableLayout
- TableCell
- TableRow
- GridStyle
- Table
- CarouselPage
- Carousel

#### Inputs
- InputValidation
- InputLayout
- AdaptiveCardInput
- InputChoice
- InputChoiceSet
- InputTextValidation
- InputText
- InputNumber
- InputDate
- InputTime
- InputToggle

#### General
- TextLayout
- TextStyle
- TextBlock
- ImageLayout
- ImageStyle
- Image
- MediaLayout
- MediaSource
- MediaCaptions
- Media

## Example
```python
from adaptive_cards import *
import json

official_example = AdaptiveCard(
    version=1.5,
    schema="http://adaptivecards.io/schemas/adaptive-card.json",
    body=[
        TextBlock("${title}", style=TextStyle(size=TextSize.MEDIUM, weight=FontWeight.BOLDER)),
        ColumnSet(
            columns=[
                Column(
                    layout=ColumnLayout(width=ColumnWidth.AUTO),
                    items=[
                        Image(
                            "${creator.profileImage}",
                            style=ImageStyle(theme=ImageTheme.PERSON),
                            layout=ImageLayout(size=ImageSize.SMALL),
                            alternate_text="${creator.name}"
                        )
                    ]
                ),
                Column(
                    items=[
                        TextBlock("${creator.name}", style=TextStyle(weight=FontWeight.BOLDER)),
                        TextBlock(
                            "Created {{DATE(${createdUtc},SHORT)}}", 
                            style=TextStyle(subtle=True),
                            layout=TextLayout(spacing=MaterialSpacing.NONE)
                        )
                    ]
                )
            ]
        ),
        TextBlock("${description}"),
        FactSet(
            facts=[
                Fact(title="${key}:", value="${value}").using("${properties}"),
            ]
        )
    ],
    actions=[
        ActionShowCard(
            title="Set due date",
            card=AdaptiveCard(
                schema="http://adaptivecards.io/schemas/adaptive-card.json",
                body=[
                    InputDate(id="dueDate"),
                    InputText(id="comment", placeholder="Add a comment", multiline=True)
                ],
                actions=[ActionSubmit(title="OK")]
            )
        ),
        ActionOpenUrl(title="View", url="${viewUrl}")
    ]
)

print(json.dumps(official_example.__dict__, indent=4))
```

### Output
```json
{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "text": "${title}",
            "wrap": true,
            "size": "Medium",
            "weight": "Bolder"
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "Image",
                            "url": "${creator.profileImage}",
                            "altText": "${creator.name}",
                            "size": "Small",
                            "style": "Person"
                        }
                    ],
                    "width": "auto"
                },
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "${creator.name}",
                            "wrap": true,
                            "weight": "Bolder"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Created {{DATE(${createdUtc},SHORT)}}",
                            "wrap": true,
                            "spacing": "None",
                            "isSubtle": true
                        }
                    ]
                }
            ]
        },
        {
            "type": "TextBlock",
            "text": "${description}",
            "wrap": true
        },
        {
            "type": "FactSet",
            "facts": [
                {
                    "$data": "${properties}",
                    "title": "${key}:",
                    "value": "${value}"
                }
            ]
        }
    ],
    "actions": [
        {
            "type": "Action.ShowCard",
            "title": "Set due date",
            "card": {
                "type": "AdaptiveCard",
                "body": [
                    {
                        "type": "Input.Date",
                        "id": "dueDate"
                    },
                    {
                        "type": "Input.Text",
                        "id": "comment",
                        "placeholder": "Add a comment",
                        "isMultiline": true
                    }
                ],
                "version": "1.6",
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "OK",
                        "associatedInputs": "auto"
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
            }
        },
        {
            "type": "Action.OpenUrl",
            "title": "View",
            "url": "${viewUrl}"
        }
    ],
    "version": "1.5",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
}
```
