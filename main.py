import flet as ft
from deep_translator import GoogleTranslator


def main(page: ft.Page):
    page.title = "Translator App"
    page.theme_mode = ft.ThemeMode.LIGHT
    def change_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            button.icon = ft.icons.NIGHTLIGHT_SHARP
        else:
            page.theme_mode = "light"
            button.icon = ft.icons.WB_SUNNY_OUTLINED
        page.update()

    def translate(e):
        text.value = GoogleTranslator(source='auto', target='en').translate(textfield.value)
        page.update()

    button = ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme)
    page.appbar = ft.AppBar(
        title=ft.Text("Translator App"),
        bgcolor="blue", leading=ft.Icon(ft.icons.TRANSLATE), actions=[button]
    )
    textfield = ft.TextField(label="enter your text", multiline=True, width=500, height=150)
    text = ft.Text()
    app = ft.Column(
        controls=[
            ft.Container(
                content=textfield,
                alignment=ft.alignment.center
            ),
            ft.Container(ft.TextButton("Translate", style=ft.ButtonStyle(bgcolor="blue", color="black"), on_click=translate) , alignment=ft.alignment.center),
            ft.Container(content=text, alignment=ft.alignment.center)
        ]
    )

    page.add(app)

ft.app(target=main)