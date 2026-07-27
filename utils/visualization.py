"""
Shared Plotly Visualization Utilities
"""

from typing import Optional

import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Theme
# ==========================================================

COLOR_SEQUENCE = [

    "#38BDF8",

    "#A78BFA",

    "#22C55E",

    "#F59E0B",

    "#EF4444",

    "#14B8A6",

    "#F472B6",

]

DARK_LAYOUT = {

    "paper_bgcolor": "rgba(0,0,0,0)",

    "plot_bgcolor": "rgba(0,0,0,0)",

    "font": {

        "color": "#E5E7EB",

        "family": "Arial",

        "size": 13,

    },

    "margin": {

        "l": 20,

        "r": 20,

        "t": 45,

        "b": 20,

    },

    "legend": {

        "orientation": "h",

        "yanchor": "bottom",

        "y": 1.02,

        "xanchor": "right",

        "x": 1,

    },

    "xaxis": {

        "gridcolor": "#293548",

        "zeroline": False,

    },

    "yaxis": {

        "gridcolor": "#293548",

        "zeroline": False,

    },

}


# ==========================================================
# Apply Theme
# ==========================================================

def styled(

    fig: go.Figure,

) -> go.Figure:
    """
    Apply the shared dashboard theme.
    """

    fig.update_layout(

        **DARK_LAYOUT

    )

    return fig


# ==========================================================
# Bar Chart
# ==========================================================

def bar(

    df,

    x,

    y,

    color=None,

    title: str = "",

):

    fig = px.bar(

        df,

        x=x,

        y=y,

        color=color,

        title=title,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Line Chart
# ==========================================================

def line(

    df,

    x,

    y,

    color=None,

    title: str = "",

):

    fig = px.line(

        df,

        x=x,

        y=y,

        color=color,

        title=title,

        markers=True,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Pie Chart
# ==========================================================

def pie(

    df,

    values,

    names,

    title="",

):

    fig = px.pie(

        df,

        values=values,

        names=names,

        hole=0.55,

        title=title,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Scatter Plot
# ==========================================================

def scatter(

    df,

    x,

    y,

    color=None,

    size=None,

    title="",

):

    fig = px.scatter(

        df,

        x=x,

        y=y,

        color=color,

        size=size,

        title=title,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Horizontal Bar
# ==========================================================

def horizontal_bar(

    df,

    x,

    y,

    color=None,

    title="",

):

    fig = px.bar(

        df,

        x=x,

        y=y,

        orientation="h",

        color=color,

        title=title,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Histogram
# ==========================================================

def histogram(

    df,

    x,

    color=None,

    title="",

):

    fig = px.histogram(

        df,

        x=x,

        color=color,

        title=title,

        color_discrete_sequence=COLOR_SEQUENCE,

    )

    return styled(fig)


# ==========================================================
# Heatmap
# ==========================================================

def heatmap(

    matrix,

    x_labels=None,

    y_labels=None,

    title="",

):

    fig = go.Figure(

        data=go.Heatmap(

            z=matrix,

            x=x_labels,

            y=y_labels,

            colorscale="Viridis",

        )

    )

    fig.update_layout(

        title=title,

    )

    return styled(fig)


# ==========================================================
# Gauge Chart
# ==========================================================

def gauge(

    value,

    title,

    minimum=0,

    maximum=100,

):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            title={"text": title},

            gauge={

                "axis": {

                    "range": [

                        minimum,

                        maximum,

                    ]

                }

            },

        )

    )

    return styled(fig)


# ==========================================================
# Metric Card Figure
# ==========================================================

def indicator(

    value,

    title,

):

    fig = go.Figure(

        go.Indicator(

            mode="number",

            value=value,

            title={"text": title},

        )

    )

    return styled(fig)