import flet
from flet import *
import requests
import datetime

api_key = ""

# _current = requests.get(
#     f"https://api.opentweathermap.org/data2.5/onecall?lat=&lon=&exclude=minutely,hourly,alert&units=metric&appid={api_key}"
# )

days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
]


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()

    def _top():
        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=450, curve="decelerate"),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment="start",
                spacing=10,
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Text(
                                "Toronto, CA",
                                size=16,
                                weight="w500",
                            )
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment="center",
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="./assets/default.png"
                                    )
                                ]
                            )
                        ],
                    ),
                ],
            ),
        )
        return top

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(width=300, height=550, controls=[_top()]),
    )

    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
