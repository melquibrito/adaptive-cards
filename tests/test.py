from adaptive_cards import *

my_adaptive_card = AdaptiveCard(
    body=[
        TextBlock(
            "This is supposed to be a title",
            style=TextStyle(
                theme=TextTheme.HEADING
            )
        ),
        Container(
            items=[
                TextBlock(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                )
            ],
            style=ContainerStyle(
                theme=ContainerTheme.EMPHASIS
            )
        ),
        ActionSet(
            actions=[
                ActionSubmit(
                    "I get it", 
                    data=ActionData(
                        msteams=MSTeams.message_back(text="they get it")
                    )
                ),
                ActionSubmit("I don't", 
                    data=ActionData(
                        msteams=MSTeams.message_back(text="they do not get it")
                    )
                )
            ],
            layout=ActionSetLayout(
                horizontal_alighment=HorizontalAlignment.RIGHT
            )
        )
    ]
)

print(my_adaptive_card)