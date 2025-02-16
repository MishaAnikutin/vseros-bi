from dash import html


HeaderComponent = html.Div(
    className="header-component",
    children=[
        html.Img(src="/assets/icon.jpg", className="header-icon"),
        html.A(
            "Мы в Телеграме",
            href="https://t.me/your-telegram-link",
            className="telegram-button"
        )
    ]
)