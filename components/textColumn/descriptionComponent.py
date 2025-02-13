from dash import html


DescriptionComponent = (
    html.H1(
        "Всерос-BI",
        className="dashboard-title"
    ),
    html.P(
        className="dashboard-description",
        children=(
            "Аналитический дашборд с прогнозами проходных баллов "
            "школьных олимпиад по экономике"
        )
    )
)