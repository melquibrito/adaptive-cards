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