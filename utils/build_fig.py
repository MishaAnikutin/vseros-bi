import pandas as pd
import plotly.express as px


def build_fig(df: pd.DataFrame, title: str):
    fig = px.histogram(
        data_frame=df,
        x='Зачетный балл',
        title=f'Распределение баллов {title}'
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
        marker=dict(color='#2F80ED')
    )

    return fig

