import pandas as pd
import plotly.express as px


def build_point_fig(
        point_data: pd.DataFrame,
        title: str,
        forecast: int,
        point: int = None
):
    fig = px.histogram(
        data_frame=point_data,
        x='Зачетный балл',
        title=f'Распределение баллов {title}'
    )

    if point is not None:
        fig.add_vline(
            x=point,
            line_color="white",
            line_dash="dash",
            annotation_text=f'Проходной {point}'
        )
    else:
        fig.add_vline(
            x=forecast,
            line_color="white",
            line_dash="dash",
            annotation_text=f'Прогноз {forecast}'
        )

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(
            family='Inter',
            size=12,
            color='white'
        ),
        title_font=dict(family='Unbounded', color='white'),
        bargap=0.1,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='gray'
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='gray'
        )
    )

    fig.update_traces(
        marker=dict(color='#2F80ED'),
    )

    return fig


def build_point_history_fig(
    point_history: pd.DataFrame,
    title: str
):
    fig = px.line(
        line_shape='hv',
        data_frame=point_history,
        x='year',
        y='point',
        title=f'История проходных {title}'
    )

    for i in range(0, point_history.shape[0] - 1, 2):
        year = point_history.year[i]
        next_year = point_history.year[i+1]

        fig.add_vrect(
            x0=year,
            x1=next_year,
            fillcolor="lightgrey",
            opacity=0.1,
            line_width=0
        )

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(
            family='Inter',
            size=12,
            color='white'
        ),
        title_font=dict(family='Unbounded', color='white'),
        bargap=0.1,
        xaxis=dict(
            showgrid=False,
            showline=True,
            gridwidth=1,
            linecolor='lightgray'
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='lightgray'
        )
    )

    fig.update_traces(
        line=dict(color='#2F80ED')
    )

    return fig

