from dash import html

from .filtersComponent import FiltersComponent
from .descriptionComponent import DescriptionComponent


TextColumn = html.Div(
    className="text-column",
    children=[
        DescriptionComponent,
        FiltersComponent,
    ]
)

__all__ = ('TextColumn', )
