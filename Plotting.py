import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np

def plotRun(xvals, yvals):

    fig = px.scatter(x = xvals, y = yvals)

    fig.update_traces(marker=dict(size=12,
                                line=dict(width=0.5,
                                            color='DarkSlateGrey')),
                    selector=dict(mode='markers'))

    fig.update_layout(
        # title="<b>Main chamber power fraction with varying heat flux width - strike point on T4<b>",
        title="<b>Peak heat flux on OOLIM PFCs with varying heat flux width - strike point on T4<b>",
        # title="<b>Main chamber power fraction with varying heat flux width - strike point on T6<b>",
        # title="<b>Peak heat flux on OOLIM PFCs with varying heat flux width - strike point on T6<b>",
        margin=dict(
            l=100,
            r=100,
            b=100,
            t=100,
            pad=2
        ),
    )

    fig.update_layout(
        font=dict(
            size=20,
        )
    )
        
    fig.add_vline(x=0.3, line_width=3, line_dash="dash", line_color='rgba(255, 100, 0, 0.5)')
    fig.add_vline(x=0.6, line_width=3, line_dash="dash", line_color='rgba(255, 0, 0, 0.5)')

    # fig.update_yaxes(title_text="<b>$f_{mainChamber}$ [%]</b>")
    # # fig.update_yaxes(title_text="<b>Peak heat flux [MW/m^2]</b>")
    # fig.update_xaxes(title_text="<b>$\lambda_{q}$ \text{[mm]}</b>")

    fig.update_layout(
        xaxis_title=r'$\lambda_{q} \text{[mm]}$',
        # yaxis_title=r'$f_{mainChamber} \text{[%]}$'
        # yaxis_title=r'$f_{mainChamber} \text{[%]}$'
        yaxis_title=r'$\text{Peak heat flux} [\frac{\text{MW}}{m^{2}}]$'
    )

    fig.show()
    output_file = f"heatresults.html"
    pio.write_html(fig, output_file)

    return 

# xvals = [
#     0.3,
#     0.4,
#     0.5,
#     0.6,
#     0.7,
#     0.75,
#     0.8,
#     0.9,
#     1,
#     1.5,
#     2.1
# ]

xvals = [
    0.6,
    0.7,
    0.8,
    0.9,
    1,
    1.1,
    1.2,
    1.3,
    1.4,
    1.5,
    1.7,
    1.9,
    2.1,
    2.3,
    2.5,
    2.6,
    2.7,
    2.8
]

yvals = [
    0.00241526,
    0.00972653,
    0.0261131,
    0.0573877,
    0.106568,
    0.194081,
    0.323723,
    0.503065,
    0.732284,
    0.901,
    1.7043,
    2.5608,
    3.532,
    4.58009,
    5.65852,
    6.20912,
    6.75703,
    7.299
]

# yvals = [
#     0.608,
#     1.700,
#     3.02,
#     4.104,
#     5.331,
#     5.543,
#     6.167,
#     6.892,
#     7.359,
#     8.371,
#     11.4607
# ]

# yvals = [
#     0.4722308234,
#     1.757185081,
#     3.881210415,
#     6.598057706,
#     9.651344124,
#     11.24233638,
#     12.85156932,
#     16.07003519,
#     19.22668543,
#     33.08554539,
#     45.38381422
# ]




# xvals = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.6, 2.7, 2.8]
# yvals = [
#     0.003040112597,
#     0.01418719212,
#     0.04256157635,
#     0.09931034483,
#     0.1976073188,
#     0.346572836,
#     0.5553272343,
#     0.8269106263,
#     1.165376495,
#     1.5686981,
#     2.56382829,
#     3.783926812,
#     5.193525686,
#     6.753103448,
#     8.424152006,
#     9.290584096,
#     10.17323012,
#     11.06803659
# ]

# yvals = [
#     0.1444573849,
#     0.5600535274,
#     1.520564914,
#     3.26177,
#     5.940889,
#     9.616144,
#     14.2572,
#     19.76949,
#     26.02011681,
#     32.85955429,
#     47.7118988,
#     63.26176834,
#     78.70231628,
#     93.48904419,
#     107.2915802,
#     113.7649307,
#     119.9366913,
#     125.8016739    
# ]

plotRun(xvals, yvals)
