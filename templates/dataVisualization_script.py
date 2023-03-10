{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "780681de-bdac-43b6-9700-002a3e5d3cb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import pprint\n",
    "import time\n",
    "from datetime import datetime\n",
    "import plotly.express as px\n",
    "import plotly.graph_objs as go"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5dedbfac-cc04-4cb3-a772-d7568e79c4a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"data_for_visualization.pkl\", \"rb\") as file:\n",
    "    data_for_visualization = pickle.load(file)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0c72557e-69bc-4b8b-a669-03a82dbe4420",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stockViz(data):\n",
    "    date = data_for_visualization[1]\n",
    "    stock_Price = data_for_visualization[2]\n",
    "    stock_Volume_Change = data_for_visualization[5]\n",
    "    stock_Volume_Change_abs = [abs(change) for change in stock_Volume_Change]\n",
    "    \n",
    "    priceTracker = px.line(x = date, y = stock_Price, title = \"Stock Price over time\" )\n",
    "\n",
    "    priceTracker.update_layout(\n",
    "        title='Stock Price',\n",
    "        yaxis_tickformat='$',\n",
    "        yaxis_title='Price',\n",
    "        xaxis_showgrid=False,   # Set the x-axis grid lines to show\n",
    "        # yaxis_showgrid=False,   # Set the y-axis grid lines to show\n",
    "        xaxis_gridcolor='lightgray',  # Set the x-axis grid color\n",
    "        yaxis_gridcolor='lightgray',  # Set the y-axis grid color\n",
    "        plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white\n",
    "    )\n",
    "    \n",
    "    changeTracker = px.scatter( x = date, y = stock_Volume_Change, title = 'Trade over time', size = stock_Volume_Change_abs)\n",
    "\n",
    "    changeTracker.update_layout(\n",
    "        yaxis_tickformat = '.2%',\n",
    "        yaxis_title = 'Percent Change',\n",
    "        xaxis_showgrid=False,   # Set the x-axis grid lines to show\n",
    "        # yaxis_showgrid=False,   # Set the y-axis grid lines to show\n",
    "        xaxis_gridcolor='lightgray',  # Set the x-axis grid color\n",
    "        yaxis_gridcolor='lightgray',  # Set the y-axis grid color\n",
    "        plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white\n",
    "    )\n",
    "    priceTracker.show()\n",
    "    changeTracker.show()\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "b689d29f-9223-45ab-9da2-792c34475d6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "x=%{x}<br>y=%{y}<extra></extra>",
         "legendgroup": "",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "marker": {
          "symbol": "circle"
         },
         "mode": "lines",
         "name": "",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          "2023-02-15T00:00:00",
          "2023-01-31T00:00:00",
          "2022-12-30T00:00:00",
          "2022-11-30T00:00:00",
          "2022-10-31T00:00:00",
          "2022-09-30T00:00:00",
          "2022-08-31T00:00:00",
          "2022-07-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-04-29T00:00:00",
          "2022-03-31T00:00:00",
          "2022-02-28T00:00:00",
          "2022-01-31T00:00:00",
          "2021-12-31T00:00:00",
          "2021-11-30T00:00:00",
          "2021-10-29T00:00:00",
          "2021-09-30T00:00:00",
          "2021-08-31T00:00:00",
          "2021-07-30T00:00:00",
          "2021-06-30T00:00:00",
          "2021-05-28T00:00:00",
          "2021-04-30T00:00:00",
          "2021-03-31T00:00:00",
          "2021-02-26T00:00:00",
          "2021-01-29T00:00:00",
          "2020-12-31T00:00:00",
          "2020-11-30T00:00:00",
          "2020-10-30T00:00:00",
          "2020-09-30T00:00:00",
          "2020-08-31T00:00:00",
          "2020-07-31T00:00:00",
          "2020-06-30T00:00:00",
          "2020-05-29T00:00:00",
          "2020-04-30T00:00:00",
          "2020-03-31T00:00:00",
          "2020-02-28T00:00:00",
          "2020-01-31T00:00:00",
          "2019-12-31T00:00:00",
          "2019-11-29T00:00:00",
          "2019-10-31T00:00:00",
          "2019-09-30T00:00:00",
          "2019-08-30T00:00:00",
          "2019-07-31T00:00:00",
          "2019-06-28T00:00:00",
          "2019-05-31T00:00:00",
          "2019-04-30T00:00:00",
          "2019-03-29T00:00:00",
          "2019-02-28T00:00:00",
          "2019-01-31T00:00:00",
          "2018-12-31T00:00:00",
          "2018-11-30T00:00:00",
          "2018-10-31T00:00:00",
          "2018-09-28T00:00:00",
          "2018-08-31T00:00:00",
          "2018-07-31T00:00:00",
          "2018-06-29T00:00:00",
          "2018-05-31T00:00:00",
          "2018-04-30T00:00:00",
          "2018-03-29T00:00:00",
          "2018-02-28T00:00:00",
          "2018-01-31T00:00:00",
          "2017-12-29T00:00:00",
          "2017-11-30T00:00:00",
          "2017-10-31T00:00:00",
          "2017-09-29T00:00:00",
          "2017-08-31T00:00:00",
          "2017-07-31T00:00:00",
          "2017-06-30T00:00:00",
          "2017-05-31T00:00:00",
          "2017-04-28T00:00:00",
          "2017-03-31T00:00:00",
          "2017-02-28T00:00:00",
          "2017-01-31T00:00:00",
          "2016-12-30T00:00:00",
          "2016-11-30T00:00:00",
          "2016-10-31T00:00:00",
          "2016-09-30T00:00:00",
          "2016-08-31T00:00:00",
          "2016-07-29T00:00:00",
          "2016-06-30T00:00:00",
          "2016-05-31T00:00:00",
          "2016-04-29T00:00:00",
          "2016-03-31T00:00:00",
          "2016-02-29T00:00:00",
          "2016-01-29T00:00:00",
          "2015-12-31T00:00:00",
          "2015-11-30T00:00:00",
          "2015-10-30T00:00:00",
          "2015-09-30T00:00:00",
          "2015-08-31T00:00:00",
          "2015-07-31T00:00:00",
          "2015-06-30T00:00:00",
          "2015-05-29T00:00:00",
          "2015-04-30T00:00:00",
          "2015-03-31T00:00:00",
          "2015-02-27T00:00:00",
          "2015-01-30T00:00:00",
          "2014-12-31T00:00:00",
          "2014-11-28T00:00:00",
          "2014-10-31T00:00:00",
          "2014-09-30T00:00:00",
          "2014-08-29T00:00:00",
          "2014-07-31T00:00:00",
          "2014-06-30T00:00:00",
          "2014-05-30T00:00:00",
          "2014-04-30T00:00:00",
          "2014-03-31T00:00:00",
          "2014-02-28T00:00:00",
          "2014-01-31T00:00:00",
          "2013-12-31T00:00:00",
          "2013-11-29T00:00:00",
          "2013-10-31T00:00:00",
          "2013-09-30T00:00:00",
          "2013-08-30T00:00:00",
          "2013-07-31T00:00:00",
          "2013-06-28T00:00:00",
          "2013-05-31T00:00:00",
          "2013-04-30T00:00:00",
          "2013-03-28T00:00:00",
          "2013-02-28T00:00:00",
          "2013-01-31T00:00:00",
          "2012-12-31T00:00:00",
          "2012-11-30T00:00:00",
          "2012-10-31T00:00:00",
          "2012-09-28T00:00:00",
          "2012-08-31T00:00:00",
          "2012-07-31T00:00:00",
          "2012-06-29T00:00:00",
          "2012-05-31T00:00:00",
          "2012-04-30T00:00:00",
          "2012-03-30T00:00:00",
          "2012-02-29T00:00:00",
          "2012-01-31T00:00:00",
          "2011-12-30T00:00:00",
          "2011-11-30T00:00:00",
          "2011-10-31T00:00:00",
          "2011-09-30T00:00:00",
          "2011-08-31T00:00:00",
          "2011-07-29T00:00:00",
          "2011-06-30T00:00:00",
          "2011-05-31T00:00:00",
          "2011-04-29T00:00:00",
          "2011-03-31T00:00:00",
          "2011-02-28T00:00:00",
          "2011-01-31T00:00:00",
          "2010-12-31T00:00:00",
          "2010-11-30T00:00:00",
          "2010-10-29T00:00:00",
          "2010-09-30T00:00:00",
          "2010-08-31T00:00:00",
          "2010-07-30T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          214.24,
          173.22,
          123.18,
          194.7,
          227.54,
          265.25,
          275.61,
          891.45,
          673.42,
          758.26,
          870.76,
          1077.6,
          870.43,
          936.72,
          1056.78,
          1144.76,
          1114,
          775.48,
          735.72,
          687.2,
          679.7,
          625.22,
          709.44,
          667.93,
          675.5,
          793.53,
          705.67,
          567.6,
          388.04,
          429.01,
          498.32,
          1430.76,
          1079.81,
          835,
          781.88,
          524,
          667.99,
          650.57,
          418.33,
          329.94,
          314.92,
          240.87,
          225.61,
          241.61,
          223.46,
          185.16,
          238.69,
          279.86,
          319.88,
          307.02,
          332.8,
          350.48,
          337.32,
          264.77,
          301.66,
          298.14,
          342.95,
          284.73,
          293.9,
          266.13,
          343.06,
          354.31,
          311.35,
          308.85,
          331.53,
          341.1,
          355.9,
          323.47,
          361.61,
          341.01,
          314.07,
          278.3,
          249.99,
          251.93,
          213.69,
          189.4,
          197.73,
          204.03,
          212.01,
          234.79,
          212.28,
          223.23,
          240.76,
          229.77,
          191.93,
          191.2,
          240.01,
          230.26,
          206.93,
          248.4,
          249.06,
          266.15,
          268.26,
          250.8,
          226.05,
          188.77,
          203.34,
          203.6,
          222.41,
          244.52,
          241.7,
          242.68,
          269.7,
          223.3,
          240.06,
          207.77,
          207.89,
          208.45,
          244.81,
          181.41,
          150.429,
          127.28,
          159.94,
          193.37,
          169,
          134.28,
          107.36,
          97.76,
          53.99,
          37.89,
          34.83,
          37.51,
          33.87,
          33.82,
          28.1314,
          29.28,
          28.52,
          27.42,
          31.29,
          29.5,
          33.13,
          37.24,
          33.41,
          29.07,
          28.56,
          32.74,
          29.37,
          24.39,
          24.74,
          28.17,
          29.13,
          30.14,
          27.6,
          27.75,
          23.89,
          24.1,
          26.63,
          35.33,
          21.84,
          20.405,
          19.48,
          19.94
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "tracegroupgap": 0
        },
        "plot_bgcolor": "rgb(255, 255, 255)",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Stock Price"
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "gridcolor": "lightgray",
         "range": [
          "2010-07-30",
          "2023-02-15"
         ],
         "showgrid": false,
         "title": {
          "text": "x"
         },
         "type": "date"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "gridcolor": "lightgray",
         "range": [
          -58.92444444444445,
          1509.1644444444444
         ],
         "tickformat": "$",
         "title": {
          "text": "Price"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "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",
      "text/html": [
       "<div>                            <div id=\"2772903e-4dc2-4063-9253-6bf43184f36f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"2772903e-4dc2-4063-9253-6bf43184f36f\")) {                    Plotly.newPlot(                        \"2772903e-4dc2-4063-9253-6bf43184f36f\",                        [{\"hovertemplate\":\"x=%{x}<br>y=%{y}<extra></extra>\",\"legendgroup\":\"\",\"line\":{\"color\":\"#636efa\",\"dash\":\"solid\"},\"marker\":{\"symbol\":\"circle\"},\"mode\":\"lines\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"2023-02-15T00:00:00\",\"2023-01-31T00:00:00\",\"2022-12-30T00:00:00\",\"2022-11-30T00:00:00\",\"2022-10-31T00:00:00\",\"2022-09-30T00:00:00\",\"2022-08-31T00:00:00\",\"2022-07-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-04-29T00:00:00\",\"2022-03-31T00:00:00\",\"2022-02-28T00:00:00\",\"2022-01-31T00:00:00\",\"2021-12-31T00:00:00\",\"2021-11-30T00:00:00\",\"2021-10-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-07-30T00:00:00\",\"2021-06-30T00:00:00\",\"2021-05-28T00:00:00\",\"2021-04-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-02-26T00:00:00\",\"2021-01-29T00:00:00\",\"2020-12-31T00:00:00\",\"2020-11-30T00:00:00\",\"2020-10-30T00:00:00\",\"2020-09-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-07-31T00:00:00\",\"2020-06-30T00:00:00\",\"2020-05-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-02-28T00:00:00\",\"2020-01-31T00:00:00\",\"2019-12-31T00:00:00\",\"2019-11-29T00:00:00\",\"2019-10-31T00:00:00\",\"2019-09-30T00:00:00\",\"2019-08-30T00:00:00\",\"2019-07-31T00:00:00\",\"2019-06-28T00:00:00\",\"2019-05-31T00:00:00\",\"2019-04-30T00:00:00\",\"2019-03-29T00:00:00\",\"2019-02-28T00:00:00\",\"2019-01-31T00:00:00\",\"2018-12-31T00:00:00\",\"2018-11-30T00:00:00\",\"2018-10-31T00:00:00\",\"2018-09-28T00:00:00\",\"2018-08-31T00:00:00\",\"2018-07-31T00:00:00\",\"2018-06-29T00:00:00\",\"2018-05-31T00:00:00\",\"2018-04-30T00:00:00\",\"2018-03-29T00:00:00\",\"2018-02-28T00:00:00\",\"2018-01-31T00:00:00\",\"2017-12-29T00:00:00\",\"2017-11-30T00:00:00\",\"2017-10-31T00:00:00\",\"2017-09-29T00:00:00\",\"2017-08-31T00:00:00\",\"2017-07-31T00:00:00\",\"2017-06-30T00:00:00\",\"2017-05-31T00:00:00\",\"2017-04-28T00:00:00\",\"2017-03-31T00:00:00\",\"2017-02-28T00:00:00\",\"2017-01-31T00:00:00\",\"2016-12-30T00:00:00\",\"2016-11-30T00:00:00\",\"2016-10-31T00:00:00\",\"2016-09-30T00:00:00\",\"2016-08-31T00:00:00\",\"2016-07-29T00:00:00\",\"2016-06-30T00:00:00\",\"2016-05-31T00:00:00\",\"2016-04-29T00:00:00\",\"2016-03-31T00:00:00\",\"2016-02-29T00:00:00\",\"2016-01-29T00:00:00\",\"2015-12-31T00:00:00\",\"2015-11-30T00:00:00\",\"2015-10-30T00:00:00\",\"2015-09-30T00:00:00\",\"2015-08-31T00:00:00\",\"2015-07-31T00:00:00\",\"2015-06-30T00:00:00\",\"2015-05-29T00:00:00\",\"2015-04-30T00:00:00\",\"2015-03-31T00:00:00\",\"2015-02-27T00:00:00\",\"2015-01-30T00:00:00\",\"2014-12-31T00:00:00\",\"2014-11-28T00:00:00\",\"2014-10-31T00:00:00\",\"2014-09-30T00:00:00\",\"2014-08-29T00:00:00\",\"2014-07-31T00:00:00\",\"2014-06-30T00:00:00\",\"2014-05-30T00:00:00\",\"2014-04-30T00:00:00\",\"2014-03-31T00:00:00\",\"2014-02-28T00:00:00\",\"2014-01-31T00:00:00\",\"2013-12-31T00:00:00\",\"2013-11-29T00:00:00\",\"2013-10-31T00:00:00\",\"2013-09-30T00:00:00\",\"2013-08-30T00:00:00\",\"2013-07-31T00:00:00\",\"2013-06-28T00:00:00\",\"2013-05-31T00:00:00\",\"2013-04-30T00:00:00\",\"2013-03-28T00:00:00\",\"2013-02-28T00:00:00\",\"2013-01-31T00:00:00\",\"2012-12-31T00:00:00\",\"2012-11-30T00:00:00\",\"2012-10-31T00:00:00\",\"2012-09-28T00:00:00\",\"2012-08-31T00:00:00\",\"2012-07-31T00:00:00\",\"2012-06-29T00:00:00\",\"2012-05-31T00:00:00\",\"2012-04-30T00:00:00\",\"2012-03-30T00:00:00\",\"2012-02-29T00:00:00\",\"2012-01-31T00:00:00\",\"2011-12-30T00:00:00\",\"2011-11-30T00:00:00\",\"2011-10-31T00:00:00\",\"2011-09-30T00:00:00\",\"2011-08-31T00:00:00\",\"2011-07-29T00:00:00\",\"2011-06-30T00:00:00\",\"2011-05-31T00:00:00\",\"2011-04-29T00:00:00\",\"2011-03-31T00:00:00\",\"2011-02-28T00:00:00\",\"2011-01-31T00:00:00\",\"2010-12-31T00:00:00\",\"2010-11-30T00:00:00\",\"2010-10-29T00:00:00\",\"2010-09-30T00:00:00\",\"2010-08-31T00:00:00\",\"2010-07-30T00:00:00\"],\"xaxis\":\"x\",\"y\":[214.24,173.22,123.18,194.7,227.54,265.25,275.61,891.45,673.42,758.26,870.76,1077.6,870.43,936.72,1056.78,1144.76,1114.0,775.48,735.72,687.2,679.7,625.22,709.44,667.93,675.5,793.53,705.67,567.6,388.04,429.01,498.32,1430.76,1079.81,835.0,781.88,524.0,667.99,650.57,418.33,329.94,314.92,240.87,225.61,241.61,223.46,185.16,238.69,279.86,319.88,307.02,332.8,350.48,337.32,264.77,301.66,298.14,342.95,284.73,293.9,266.13,343.06,354.31,311.35,308.85,331.53,341.1,355.9,323.47,361.61,341.01,314.07,278.3,249.99,251.93,213.69,189.4,197.73,204.03,212.01,234.79,212.28,223.23,240.76,229.77,191.93,191.2,240.01,230.26,206.93,248.4,249.06,266.15,268.26,250.8,226.05,188.77,203.34,203.6,222.41,244.52,241.7,242.68,269.7,223.3,240.06,207.77,207.89,208.45,244.81,181.41,150.429,127.28,159.94,193.37,169.0,134.28,107.36,97.76,53.99,37.89,34.83,37.51,33.87,33.82,28.1314,29.28,28.52,27.42,31.29,29.5,33.13,37.24,33.41,29.07,28.56,32.74,29.37,24.39,24.74,28.17,29.13,30.14,27.6,27.75,23.89,24.1,26.63,35.33,21.84,20.405,19.48,19.94],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"x\"},\"showgrid\":false,\"gridcolor\":\"lightgray\"},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Price\"},\"tickformat\":\"$\",\"gridcolor\":\"lightgray\"},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Stock Price\"},\"plot_bgcolor\":\"rgb(255, 255, 255)\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('2772903e-4dc2-4063-9253-6bf43184f36f');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "x=%{x}<br>y=%{y}<br>size=%{marker.size}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "size": [
           0,
           76.52,
           24.46,
           35.96,
           7.95,
           25.17,
           43.45,
           20.78,
           15.31,
           3.22,
           22.39,
           14.15,
           19.42,
           37.75,
           20.08,
           26.74,
           18.2,
           26.23,
           2.13,
           17.25,
           16.04,
           20.31,
           8.54,
           38.75,
           44.89,
           36.01,
           69.32,
           34.63,
           6.75,
           108.29,
           76.77,
           6.27,
           32.34,
           6.59,
           39.88,
           10.31,
           12.5,
           13.91,
           49.12,
           23.87,
           48.75,
           41.85,
           1.81,
           48.69,
           7.82,
           31.46,
           18.34,
           7.35,
           39.87,
           36.65,
           16.63,
           9.17,
           115.28,
           31.53,
           41.46,
           37.86,
           23.83,
           27.1,
           22.35,
           17.86,
           31.84,
           15.34,
           11.27,
           34.52,
           17.18,
           8.97,
           19.88,
           35.85,
           2.02,
           20.87,
           20.07,
           7.91,
           11.67,
           15.77,
           12.6,
           12.38,
           6.83,
           23.32,
           11.82,
           18.91,
           64.29,
           15.1,
           31.16,
           24.19,
           30.15,
           40.73,
           24.47,
           31.14,
           28.5,
           20.46,
           41.94,
           29.68,
           18.22,
           36.13,
           11.01,
           24.3,
           13.23,
           15.55,
           41.03,
           15.24,
           41.23,
           12.73,
           13.6,
           5.96,
           14.25,
           9.39,
           22.55,
           0.89,
           35.56,
           18.6,
           7.45,
           56.04,
           16.19,
           33.76,
           51.43,
           11.47,
           21.96,
           84.92,
           75.38,
           63.63,
           49.24,
           35.68,
           23.71,
           9.43,
           25.84,
           88.95,
           26.47,
           32.93,
           19.72,
           30.84,
           33.44,
           2.59,
           4.65,
           10.42,
           17.5,
           22.33,
           16.19,
           16.81,
           51.02,
           22.46,
           88.26,
           23.61,
           1.5,
           8.93,
           10.01,
           3.01,
           29.81,
           23.25,
           76.88,
           175.6,
           16.67,
           329.41
          ],
          "sizemode": "area",
          "sizeref": 0.8235250000000001,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          "2023-02-15T00:00:00",
          "2023-01-31T00:00:00",
          "2022-12-30T00:00:00",
          "2022-11-30T00:00:00",
          "2022-10-31T00:00:00",
          "2022-09-30T00:00:00",
          "2022-08-31T00:00:00",
          "2022-07-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-05-31T00:00:00",
          "2022-04-29T00:00:00",
          "2022-03-31T00:00:00",
          "2022-02-28T00:00:00",
          "2022-01-31T00:00:00",
          "2021-12-31T00:00:00",
          "2021-11-30T00:00:00",
          "2021-10-29T00:00:00",
          "2021-09-30T00:00:00",
          "2021-08-31T00:00:00",
          "2021-07-30T00:00:00",
          "2021-06-30T00:00:00",
          "2021-05-28T00:00:00",
          "2021-04-30T00:00:00",
          "2021-03-31T00:00:00",
          "2021-02-26T00:00:00",
          "2021-01-29T00:00:00",
          "2020-12-31T00:00:00",
          "2020-11-30T00:00:00",
          "2020-10-30T00:00:00",
          "2020-09-30T00:00:00",
          "2020-08-31T00:00:00",
          "2020-07-31T00:00:00",
          "2020-06-30T00:00:00",
          "2020-05-29T00:00:00",
          "2020-04-30T00:00:00",
          "2020-03-31T00:00:00",
          "2020-02-28T00:00:00",
          "2020-01-31T00:00:00",
          "2019-12-31T00:00:00",
          "2019-11-29T00:00:00",
          "2019-10-31T00:00:00",
          "2019-09-30T00:00:00",
          "2019-08-30T00:00:00",
          "2019-07-31T00:00:00",
          "2019-06-28T00:00:00",
          "2019-05-31T00:00:00",
          "2019-04-30T00:00:00",
          "2019-03-29T00:00:00",
          "2019-02-28T00:00:00",
          "2019-01-31T00:00:00",
          "2018-12-31T00:00:00",
          "2018-11-30T00:00:00",
          "2018-10-31T00:00:00",
          "2018-09-28T00:00:00",
          "2018-08-31T00:00:00",
          "2018-07-31T00:00:00",
          "2018-06-29T00:00:00",
          "2018-05-31T00:00:00",
          "2018-04-30T00:00:00",
          "2018-03-29T00:00:00",
          "2018-02-28T00:00:00",
          "2018-01-31T00:00:00",
          "2017-12-29T00:00:00",
          "2017-11-30T00:00:00",
          "2017-10-31T00:00:00",
          "2017-09-29T00:00:00",
          "2017-08-31T00:00:00",
          "2017-07-31T00:00:00",
          "2017-06-30T00:00:00",
          "2017-05-31T00:00:00",
          "2017-04-28T00:00:00",
          "2017-03-31T00:00:00",
          "2017-02-28T00:00:00",
          "2017-01-31T00:00:00",
          "2016-12-30T00:00:00",
          "2016-11-30T00:00:00",
          "2016-10-31T00:00:00",
          "2016-09-30T00:00:00",
          "2016-08-31T00:00:00",
          "2016-07-29T00:00:00",
          "2016-06-30T00:00:00",
          "2016-05-31T00:00:00",
          "2016-04-29T00:00:00",
          "2016-03-31T00:00:00",
          "2016-02-29T00:00:00",
          "2016-01-29T00:00:00",
          "2015-12-31T00:00:00",
          "2015-11-30T00:00:00",
          "2015-10-30T00:00:00",
          "2015-09-30T00:00:00",
          "2015-08-31T00:00:00",
          "2015-07-31T00:00:00",
          "2015-06-30T00:00:00",
          "2015-05-29T00:00:00",
          "2015-04-30T00:00:00",
          "2015-03-31T00:00:00",
          "2015-02-27T00:00:00",
          "2015-01-30T00:00:00",
          "2014-12-31T00:00:00",
          "2014-11-28T00:00:00",
          "2014-10-31T00:00:00",
          "2014-09-30T00:00:00",
          "2014-08-29T00:00:00",
          "2014-07-31T00:00:00",
          "2014-06-30T00:00:00",
          "2014-05-30T00:00:00",
          "2014-04-30T00:00:00",
          "2014-03-31T00:00:00",
          "2014-02-28T00:00:00",
          "2014-01-31T00:00:00",
          "2013-12-31T00:00:00",
          "2013-11-29T00:00:00",
          "2013-10-31T00:00:00",
          "2013-09-30T00:00:00",
          "2013-08-30T00:00:00",
          "2013-07-31T00:00:00",
          "2013-06-28T00:00:00",
          "2013-05-31T00:00:00",
          "2013-04-30T00:00:00",
          "2013-03-28T00:00:00",
          "2013-02-28T00:00:00",
          "2013-01-31T00:00:00",
          "2012-12-31T00:00:00",
          "2012-11-30T00:00:00",
          "2012-10-31T00:00:00",
          "2012-09-28T00:00:00",
          "2012-08-31T00:00:00",
          "2012-07-31T00:00:00",
          "2012-06-29T00:00:00",
          "2012-05-31T00:00:00",
          "2012-04-30T00:00:00",
          "2012-03-30T00:00:00",
          "2012-02-29T00:00:00",
          "2012-01-31T00:00:00",
          "2011-12-30T00:00:00",
          "2011-11-30T00:00:00",
          "2011-10-31T00:00:00",
          "2011-09-30T00:00:00",
          "2011-08-31T00:00:00",
          "2011-07-29T00:00:00",
          "2011-06-30T00:00:00",
          "2011-05-31T00:00:00",
          "2011-04-29T00:00:00",
          "2011-03-31T00:00:00",
          "2011-02-28T00:00:00",
          "2011-01-31T00:00:00",
          "2010-12-31T00:00:00",
          "2010-11-30T00:00:00",
          "2010-10-29T00:00:00",
          "2010-09-30T00:00:00",
          "2010-08-31T00:00:00",
          "2010-07-30T00:00:00"
         ],
         "xaxis": "x",
         "y": [
          0,
          76.52,
          -24.46,
          -35.96,
          -7.95,
          -25.17,
          -43.45,
          -20.78,
          15.31,
          -3.22,
          -22.39,
          14.15,
          -19.42,
          37.75,
          -20.08,
          26.74,
          -18.2,
          -26.23,
          -2.13,
          17.25,
          16.04,
          20.31,
          8.54,
          38.75,
          -44.89,
          36.01,
          69.32,
          -34.63,
          6.75,
          108.29,
          -76.77,
          -6.27,
          -32.34,
          6.59,
          39.88,
          10.31,
          12.5,
          -13.91,
          -49.12,
          -23.87,
          48.75,
          -41.85,
          -1.81,
          48.69,
          7.82,
          31.46,
          -18.34,
          -7.35,
          -39.87,
          36.65,
          -16.63,
          -9.17,
          115.28,
          -31.53,
          41.46,
          -37.86,
          23.83,
          -27.1,
          22.35,
          -17.86,
          -31.84,
          15.34,
          -11.27,
          34.52,
          -17.18,
          -8.97,
          19.88,
          35.85,
          2.02,
          -20.87,
          -20.07,
          -7.91,
          11.67,
          -15.77,
          -12.6,
          12.38,
          -6.83,
          -23.32,
          -11.82,
          18.91,
          64.29,
          -15.1,
          31.16,
          -24.19,
          30.15,
          -40.73,
          -24.47,
          31.14,
          28.5,
          -20.46,
          41.94,
          -29.68,
          -18.22,
          36.13,
          11.01,
          24.3,
          -13.23,
          -15.55,
          41.03,
          -15.24,
          41.23,
          -12.73,
          -13.6,
          -5.96,
          14.25,
          9.39,
          22.55,
          0.89,
          35.56,
          -18.6,
          7.45,
          56.04,
          -16.19,
          -33.76,
          51.43,
          -11.47,
          -21.96,
          84.92,
          -75.38,
          -63.63,
          49.24,
          -35.68,
          -23.71,
          9.43,
          -25.84,
          88.95,
          -26.47,
          32.93,
          -19.72,
          30.84,
          -33.44,
          -2.59,
          4.65,
          10.42,
          -17.5,
          22.33,
          -16.19,
          -16.81,
          51.02,
          -22.46,
          88.26,
          -23.61,
          -1.5,
          8.93,
          -10.01,
          -3.01,
          29.81,
          -23.25,
          -76.88,
          175.6,
          -16.67,
          329.41
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "itemsizing": "constant",
         "tracegroupgap": 0
        },
        "plot_bgcolor": "rgb(255, 255, 255)",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Trade over time"
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "gridcolor": "lightgray",
         "range": [
          "2009-08-10 00:50:17.9589",
          "2023-12-03 00:18:36.5197"
         ],
         "showgrid": false,
         "title": {
          "text": "x"
         },
         "type": "date"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "gridcolor": "lightgray",
         "range": [
          -125.67142886603742,
          402.16792931240246
         ],
         "tickformat": ".2%",
         "title": {
          "text": "Percent Change"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABEMAAAFoCAYAAAC8DzWwAAAAAXNSR0IArs4c6QAAIABJREFUeF7s3QuQFOW5+P+newYWhOV+Vy4CKiAIqCjeCAjxAuIFI6J4ISSEo7//SSWxsCSnUqlU6gRLyiSVnKOHEFFjEEREEQE1oohBEUQQVFC5itzv12VhZvpfT4+929M7192Z3emZb1elom5Pz/t+3p6Z7qef93kNy7IsYUMAAQQQQAABBBBAAAEEEEAAAQSKRMAgGFIkI003EUAAAQQQQAABBBBAAAEEEEDAFiAYwomAAAIIIIAAAggggAACCCCAAAJFJUAwpKiGm84igAACCCCAAAIIIIAAAggggADBEM4BBBBAAAEEEEAAAQQQQAABBBAoKgGCIUU13HQWAQQQQAABBBBAAAEEEEAAAQQIhnAOIIAAAggggAACCCCAAAIIIIBAUQkQDCmq4aazCCCAAAIIIIAAAggggAACCCBAMIRzAAEEEEAAAQQQQAABBBBAAAEEikqAYEhRDTedRQABBBBAAAEEEEAAAQQQQAABgiGcAwgggAACCCCAAAIIIIAAAgggUFQCBEOKarjpLAIIIIAAAggggAACCCCAAAIIEAzhHEAAAQQQQAABBBBAAAEEEEAAgaISIBhSVMNNZxFAAAEEEEAAAQQQQAABBBBAgGAI5wACCCCAAAIIIIAAAggggAACCBSVAMGQohpuOosAAggggAACCCCAAAIIIIAAAgRDOAcQQAABBBBAAAEEEEAAAQQQQKCoBAiGFNVw01kEEEAAAQQQQAABBBBAAAEEECAYwjmAAAIIIIAAAggggAACCCCAAAJFJUAwpKiGm84igAACCCCAAAIIIIAAAggggADBEM4BBBBAAAEEEEAAAQQQQAABBBAoKgGCIUU13HQWAQQQQAABBBBAAAEEEEAAAQQIhnAOIIAAAggggAACCCCAAAIIIIBAUQkQDCmq4aazCCCAAAIIIIAAAggggAACCCBAMIRzAAEEEEAAAQQQQAABBBBAAAEEikqAYEhRDTedRQABBBBAAAEEEEAAAQQQQAABgiGcAwgggAACCCCAAAIIIIAAAgggUFQCBEOKarjpLAIIIIAAAggggAACCCCAAAIIEAzhHEAAAQQQQAABBBBAAAEEEEAAgaISIBhSVMNNZxFAAAEEEEAAAQQQQAABBBBAgGAI5wACCCCAAAIIIIAAAggggAACCBSVAMGQohpuOosAAggggAACCCCAAAIIIIAAAgRDOAcQQAABBBBAAAEEEEAAAQQQQKCoBAiGFNVw01kEEEAAAQQQQAABBBBAAAEEECAYwjmAAAIIIIAAAggggAACCCCAAAJFJUAwpKiGm84igAACCCCAAAIIIIAAAggggADBEM4BBBBAAAEEEEAAAQQQQAABBBAoKgGCITkc7sNHj8tDj/1JRo8cLKOGD8rhO3FoBBBAAAEEEEAAAQQQQAABBBBIV6BggyHzFi2T3zwxI6VDn55d5enHfynNm5am3DfTHQiGiPxx2hxZuXZjFWPHplOHNvK7SeOlYYP6mfKyPwIIIIAAAggggAACCCCAAALVEijYYIhXoy4CE3XxntU6C3L4IoIhOcTl0AgggAACCCCAAAIIIIAAAtUSIBhSLbb0XkQwJHFmSHqC7IUAAggggAACCCCAAAIIIIBA9gWKPhiyefsumfjok/Lwg7dJxw5tZNwvHreVf3LPcPnxmJvtmh/rN2yJkde//Wri6Cqj4Z2a06fH+XLg8DH72O6aIWWnz8hvp86QhUtWVBzj94+Oz6iuiGZcPDNrUcXr3W1yjq9/9E5BSfQ3b9tHDB0Y81onsHNFvx5y203X2ma79x4U735uFG8b9W/t27aUaU88Ii2aldq2ejzHUtswZ8FS+cPkCfLrKdMr3J2pTIeOHK94Xz1WoilOq9ZurBjHZPtl/+PEERFAAAEEEEAAAQQQQAABBPwgQDDk+2CI3th7gxwaAJjyl5ky+edjK2qKuIMC7oCI3vgvevdj+0a/W+cO9ti7Ay1OMMT5b8Ovv7IiCJDomPFOoHjBjHj1N5yAwHN/fkwG9OtRcShvm5zjfbtrX0xdD+/0Fuc9NDCULADibXOqaTLeYIjWeXEHOdzvG++/u1+v7x1vHDTI8tTz82PGxg8fTtqIAAIIIIAAAggggAACCCCQGwGCIa7MkHRXfHEyGJzCq06AYcrkCTGBh3jTZPRmfc++Q1UyNtK9YU+0nzfIkSjA4m27Bk0mT5leJVCQ7vFSnZaZBkM0M8Rb0NbbZuc9Mx0Hb+AkVdv5OwIIIIAAAggggAACCCCAQGEKEAxJIxgSb7qHO0shUYDCGwxJVkMkUUDFe9olCqbEC3542xVvn0THczJG2rVpYWewZJK94m5zbQZDEgVNtD2J+lmYH2t6hQACCCCAAAIIIIAAAgggkEyAYEiSYIgToGjVomlMtoL3pjvVDf/okYPteiDO8XRKTqLNO63FvV+mtUC82R3eLJB4tUu87XKmDvkhGBIvaOXuTybTe/jaQAABBBBAAAEEEEAAAQQQKFwBgiFJgiGJghzeYEiijIRMMkPSPcUyyQzRYzr7a90TrX+im7uoaroZE34IhiTLDEnXl/0QQAABBBBAAAEEEEAAAQQKX4BgSIJgSLIsjHh1N3QVGm9WhzcYkuyY6Z5q6dYMcY7nFFKd/J9j5bk5b4q3rkm6tUqqGwxJFSiKt5pMdWuGJCoam64t+yGAAAIIIIAAAggggAACCBSHAMGQJJkh8QIFzhK07poh8YIc7iko7mVznakrl/a+ICZDQ/ef+vRsGTtqWMVqNPFOwXirv8RbTcZ5rbsd8Zaidf7+6effVCmiqn3VTaf4VDcYkihAkajGSU0KqGpbnaky3sCUtuODj9fFXRK5OD7q9BIBBBBAAAEEEEAAAQQQQMARIBiSooCqE/xwwDSwoZv3pt1bf6N925Z2FsaT0+aIUzMkXoDCfSp6l/ZNdpp662Mke63TB3dQxntsbz/17+ksZZvOR8l9bHXR5YdbNCuVhx77k2QzM8RpixOAcbfNeV9n2eN02s0+CCCAAAIIIIAAAggggAAChSlQNMGQwhw+eoUAAggggAACCCCAAAIIIIAAApkKEAzJVIz9EUAAAQQQQAABBBBAAAEEEEDA1wIEQ3w9fDQeAQQQQAABBBBAAAEEEEAAAQQyFSAYkqkY+yOAAAIIIIAAAggggAACCCCAgK8FCIb4evhoPAIIIIAAAggggAACCCCAAAIIZCpAMCRTMfZHAAEEEEAAAQQQQAABBBBAAAFfCxAM8fXw0XgEEEAAAQQQQAABBBBAAAEEEMhUgGBIpmLsjwACCCCAAAIIIIAAAggggAACvhYgGOLr4aPxCCCAAAIIIIAAAggggAACCCCQqQDBkEzF2B8BBBBAAAEEEEAAAQQQQAABBHwtQDDE18NH4xFAAAEEEEAAAQQQQAABBBBAIFMBgiGZirE/AggggAACCCCAAAIIIIAAAgj4WoBgiK+Hj8YjgAACCCCAAAIIIIAAAggggECmAgRDMhVjfwQQQAABBBBAAAEEEEAAAQQQ8LUAwRBfDx+NRwABBBBAAAEEEEAAAQQQQACBTAUIhmQqxv4IIIAAAggggAACCCCAAAIIIOBrAYIhvh4+Go8AAggggAACCCCAAAIIIIAAApkKEAzJVIz9EUAAAQQQQAABBBBAAAEEEEDA1wIEQ3w9fDQeAQQQQAABBBBAAAEEEEAAAQQyFSAYkqkY+yOAAAIIIIAAAggggAACCCCAgK8FCIb4evhoPAIIIIAAAggggAACCCCAAAIIZCpAMCRTMfZHAAEEEEAAAQQQQAABBBBAAAFfCxAM8fXw0XgEEEAAAQQQQAABBBBAAAEEEMhUgGBIpmLsjwACCCCAAAIIIIAAAggggAACvhYgGOLr4aPxCCCAAAIIIIAAAggggAACCCCQqQDBkEzF2B8BBBBAAAEEEEAAAQQQQAABBHwtQDDE18NH4xFAAAEEEEAAAQQQQAABBBBAIFMBgiGZirE/AggggAACCCCAAAIIIIAAAgj4WoBgiK+Hj8YjgAACCCCAAAIIIIAAAggggECmAgRDMhVjfwQQQAABBBBAAAEEEEAAAQQQ8LUAwRBfDx+NRwABBBBAAAEEEEAAAQQQQACBTAUIhmQqxv4IIIAAAggggAACCCCAAAIIIOBrAYIhvh4+Go8AAggggAACCCCAAAIIIIAAApkKEAzJVIz9EUAAAQQQQAABBBBAAAEEEEDA1wIEQ3w9fDQeAQQQQAABBBBAAAEEEEAAAQQyFSAYkqkY+yOAAAIIIIAAAggggAACCCCAgK8FCIb4evhoPAIIIIAAAggggAACCCCAAAIIZCpAMCRTMfZHAAEEEEAAAQQQQAABBBBAAAFfCxAM8fXw0XgEEEAAAQQQQAABBBBAAAEEEMhUgGBIpmLsjwACCCCAAAIIIIAAAggggAACvhYgGOLr4aPxCCCAAAIIIIAAAggggAACCCCQqQDBkEzF2B8BBBBAAAEEEEAAAQQQQAABBHwtQDDE18NH4xFAAAEEEEAAAQQQQAABBBBAIFMBgiGZirE/AggggAACCCCAAAIIIIAAAgj4WoBgiK+Hj8YjgAACCCCAAAIIIIAAAggggECmAgRDMhVjfwQQQAABBBBAAAEEEEAAAQQQ8LVAwQRDVq3dKON+8bg89+fHZEC/HvaglJ0+I7+dOkMWLllh//vvHx0vo4YPqhgw5zX6H/r07CpPP/5Lad60tOLv8xYtk988McP+9xFDB8rvJo2Xhg3q2/9++OhxeeixP8n6DVvsf3e/b7wzItX+ydriboe7D3rMyX+YLpMeHiPdOnfw9YlI4xFAAAEEEEAAAQQQQAABBBCoLYGCCIa4AwnuoMQfp82xHX81cXRF8OKRiaPtYMnm7bvkv6ZMl/+ePMEOJGjAYcXqLysCHnrMJ6fNqQiQuI/lBFkGXtbLDq54j+UdvFT7J2vL6fJymfKXmTL552Ptwzr/rEEbbbNu7gBPbZ04vA8CCCCAAAIIIIAAAggggAACfhXwfTBEAwlTn5otj/6/e+TXU6aLE+yIlzXhDmhoIGHbjj12oEQ3b0BC9+3SsV1FoMEdHDl05Lj9nlN+PcHOJPEGO7wng9PGRPsna4sea+a8d2TSQ2Psw059eraMHTVMWjQrjQmM+PUEpN0IIIAAAggggAACCCCAAAII1LaAr4Mh7gCGBgd02kqizA+FdWd/PP38a7a1EwxxprHo63v36GpPr3EyP7zBkkOHj8Vkjejf3YEW7yB6s0y8+3tf625L9/PPjZsZ8t7yNfbbkBVS2x8Z3g8BBBBAAAEEEEAAAQQQQMDvAr4NhngzP9wBBGcajDt7I14wxJ35ES8YctfIwRX1R9yBFw2GvLxgaUwNkVTBkGT7e7NQvH3x1gwZck3/igDJs7MXyzOzFtnnYaq6JX4/WWk/AggggAACCCCAAAIIIIAAAtkQ8G0wRIMTEx99UnbvPVjFQYMCLZo3iakJEi8Yov8t3zNDnGKw7k46tUL6Xty9YgrNrr0HYqbuZOPk4BgIIIAAAggggAACCCCAAAIIFKKAb4Mh3sHwZlMUSs0Q7yox2i+niOqmrTsrMlTchVbdK+IU4klLnxBAAAEEEEAAAQQQQAABBBCoiUDBBkMUpa5Wk3ECM6NHDrZretRkNRlnKV9nkN0ryGh2jFNclcyQmnwMeC0CCCCAAAIIIIAAAggggEAxCRR0MMQJQixcssIe098/Oj6m4Kh7Sd4+PbtWLKPrDjz85okZ9r+OGDowpkaIE/BYv2GL/Xd3vQ5vMET/nmx//Xuqtug+7uCHEyRx1xOhZkgxfXTpKwIIIIAAAggggAACCCCAQHUFCiYYUl0AXocAAggggAACCCCAAAIIIIAAAsUlQDCkuMab3iKAAAIIIIAAAggggAACCCBQ9AIEQ4r+FAAAAQQQQAABBBBAAAEEEEAAgeISIBhSXONNbxFAAAEEEEAAAQQQQAABBBAoegGCIUV/CgCAAAIIIIAAAggggAACCCCAQHEJEAwprvEuuN6eOGlJIGDY/bIskUjEksaNov/OhgACCCCAAAIIIIAAAggggEA8AYIhnBe+EgiFRMIREQ137N4Xkf0HLNl/QGTfAUvatTGkTSuR1q0MadfGFN03EBSpF/RVF2ksAggggAACCCCAAAIIIIBAjgUIhuQYmMNnR6D8jMiZsyJbt4flkzWWnDiZ+riNG4lcOzAg7Vob0qRJ6v3ZAwEEEEAAAQQQQAABBBBAoDgECIYUxzj7updlp0UMQ+SNN8Oya6+VcV/O72TIiBtMCUcMskQy1uMFCCCAAAIIIIAAAggggEDhCRAMKbwxLagenSwT2b4jIu8sjdS4X7fcGJA2LUUaN6amSI0xOQACCCCAAAIIIIAAAggg4GMBgiE+HrxCb/rJMks2b7Fk6fKaB0Icq5uHBqTjeYY0KCl0PfqHAAIIIIAAAggggAACCCCQSIBgCOdGXgqcDYkcPWrJi6+Es96+n94flGBApH79rB+aAyKAAAIIIIAAAggggAACCPhAgGCIDwapGJt4ulxk1tyQHE+jUGqmPm1bGzLihybTZTKFY38EEEAAAQQQQAABBBBAoEAECIYUyEAWUjfKykRWrQnL2s8zL5aarsPVVxjSp1dASsgOSZeM/RBAAAEEEEAAAQQQQACBghEgGFIwQ1k4Hdm1x5K5r2d/eoxX6N47A9KqJcVUC+fMoScIIIAAAggggAACCCCAQHoCBEPSc2KvWhT4ZrMli5fkPhjyo1sD0qEdwZBaHFreCgEEEEAAAQQQQAABBBDICwGCIXkxDDTCETh2TGTt57mdIuO8l06V6XGBKY0bERDhDEQAAQQQQAABBBBAAAEEikmAYEgxjbYP+nr8uMjbS8Oyc3fu6oU4DBd0NeSaKwPSpNQHMDQRAQQQQAABBBBAAAEEEEAgawIEQ7JGyYGyIRAKizzzQkjKz2TjaMmP0bypyF23B6VBSe7fi3dAAAEEEEAAAQQQQAABBBDIHwGCIfkzFrRERPYfsmTW3NzXC3Gwf3JfUBqdAz0CCCCAAAIIIIAAAggggEAxCRAMKabR9kFfQyGRp2aEaqWl9YIiPxsXkIBJzZBaAedNEEAAAQQQQAABBBBAAIE8ESAYkicDQTOiAqfLLZk9LyzHjudepH0bQ24eZkrjxgRDcq/NOyCAAAIIIIAAAggggAAC+SNAMCR/xoKWiMiRo5YsXxmRzVtzX0D1kl6GXHpJQJo0gR4BBBBAAAEEEEAAAQQQQKCYBAiGFNNo+6CvJ8tEvtgQlhWf5D4YMnSQKRd1NyUY9AEMTUQAAQQQQAABBBBAAAEEEMiaAMGQrFFyoGwJ7Nwt8sqC3NcNuX90UJo3y1arOQ4CCCCAAAIIIIAAAggggIBfBHwdDNm8fZdMfPRJ2b33oO09YuhA+d2k8dKwQX3738tOn5HfTp0hC5essP/994+Ol1HDB1WMzaq1G2XcLx63/71Pz67y9OO/lOZNSyv+Pm/RMvnNEzPiHvvw0ePy0GN/kvUbtth/f+7Pj8mAfj0Sjnuq/ZO1xd0Odx/0mJP/MF0mPTxGunXu4JdzLmU7T5wSee7FkEQiKXet9g7nNBS590dB0f9nQwABBBBAAAEEEEAAAQQQKC4BXwdDNEjQsUObiiDEH6fNsUfvVxNH2//v/ncnGPHIxNH2/hpI+a8p0+W/J0+wAwl6rBWrv6wIpmhw4slpcyoCJO5jOUGWgZf1soMr3mN5T6FU+ydry+nycpnyl5ky+edj7cM6/6xBG22zbu4ATyGcvmfOiuzZa8lri3K3xO7YHwWkZQsKpxbC+UIfEEAAAQQQQAABBBBAAIFMBXwdDPF21h3Q0CCCN2vCHdDQfbft2FMROPEGJHTfLh3bVQQa3MGRQ0eOy9SnZsuUX0+wM0m8wQ5vu/TYyfZP1hY91sx578ikh8bYh5369GwZO2qYtGhWGhMYyXTg833/Q4ct+XRdRL78Kvu1Qy7vZ0ivCwPSjCky+X4a0D4EEEAAAQQQQAABBBBAICcCBRMMcQIS7dq0sAMc8bI13MGSp59/zQZ1skjcmSO9e3S1p9c4mR+6n/t4hw4fi8ka0b97s1Lco+XNMvHu732tuy3dzz83bmbIe8vX2G9RaFkhbrezZ0VmzAxJ+ZnsnftaI+TOkQE5pyFZIdlT5UgIIIAAAggggAACCCCAgL8ECiIYosGEZ2YtiqkZ4s3G0GHxBkPcmR/xgiF3jRxcMQXHGwx5ecHSmPokqYIhyfb3ZqF4p/R4a4YMuaZ/RYDk2dmL7b7r5q5b8u233/rrTIzT2mAwKOVnmsqc+dkpHlK/nsjddxgSCR+RSC4Lkvheng74XcCysp9R5XcT2l/4AvXr15czZ7IYPS98MnqIQMEIGAYPuQpmMOlIRgKdOnXKaH92jhUoiGCI0yV3sGPX3gMxNUHiBUP0v+V7Zki8oqxOrZC+F3evmEKj/XVPxTl69GhBnOuhcECalJbIG2+HZev26t/g9bjAkOuvC8iZM2XCjWJBnBp0IokAF4WcHsUooOc93+/FOPL0GQHhs89JULQCTZs2Ldq+Z6PjCYMh7pVY2rdtKdOeeEQ6tG1VZfpINhqRrWO4s0H0mIVQM8S7SoxmjThFVDdt3SlOxom70Kp7RZxs2db1cQ4fEdm7LyJvL80sS8Q0RUbeGJBmTQ1p2qSue8H7I4AAAggggAACCCCAAAII5INAwmCIM3Xj5usHVhTt1BtzrX/hnfJRVx352z8XyNDrLqtYVlbbvGffoYrpK3W1mowzzWX0yMF2TY+arCbjLBPsGLtXkNHgj1Nc1ZsZUldjksv3LSsTqV8isnJ1WA4eFtl/wJLjJ6q+owY9WreKBj+uHhCQUEikXr1ctoxjI4AAAggggAACCCCAAAII+EkgbjBEb+adrArNBnFWMNFgSLxaHHXVYQ3MjPvF4xVvP2LowJg6Hu7sFt3p94+Ojyk46n59n55dK5bRdQcefvPEDPtfvcd2Ah7rN2yx/+6u1+ENhujfk+2vf0/VFt3HHfxwgiTueiLuNtTVmNTG+4YjIqfKROoFRMyAJYcPi2zeFpELuprSvJkhujSvlkwoqS8SDNZGi3gPBBBAAAEEEEAAAQQQQAABPwlkHAzJp8wQP0HTVgQQQAABBBBAAAEEEEAAAQQQyA+BhNNknGKkk38+Vv4641UZO2qYtGhWKg899idxpn/kRxdoBQIIIIAAAggggAACCCCAAAIIIJC+QNLVZLzTUPSwxTIVI31C9kQAAQQQQAABBBBAAAEEEEAAAT8JFNTSun6Cp60IIIAAAggggAACCCCAAAIIIFA3AgRD6sadd0UAAQQQQAABBBBAAAEEEEAAgToSSFhAVWuDOCulJGqbd3WWOuoDb4sAAggggAACCCCAAAIIIIAAAgikLZAwM+SP0+ZIl47tYpaidZaqvWvkYOndo6v8duoMGXhZr5h90n5ndkQAAQQQQAABBBBAAAEEEEAAAQTqQCDl0rrdOneIaZauMrNtxx751cTRwjK7dTBivCUCCCCAAAIIIIAAAggggAACCNRIIONgiDsAsmvvAZn61GyZ8usJ0rxpaY0awosRQAABBBBAAAEEEEAAAQQQQACB2hCIGwxxT4cZ0K9HTDvcwZDPN26RJ6fNkacf/yXBkNoYLd4DAQQQQAABBBBAAAEEEEAAAQRqLJCwZogGPSZPmS7TnnhEnKkyh48eFy2s+sjE0aJBEp0ys2L1l/K7SeOlYYP6NW4MB0AAAQQQQAABBBBAAAEEEEAAAQRyLZB0ad3N23fJxEeflN17D1a047k/P2YHQtgQQAABBBBAAAEEEEAAAQQQQAABPwokDYb4sUO0GQEEEEAAAQQQQAABBBBAAAEEEEgmQDCE8wMBBBBAAAEEEEAAAQQQQAABBIpKIGEwxKkPsn7DliogfXp2pWhqUZ0mdBYBBBBAAAEEEEAAAQQQQACBwhFIGAz547Q5di9/NXF04fSWniCAAAIIIIAAAggggAACCCCAQNELxA2GaFbI5D9Ml0kPj6lYSabopQBAAAEEEEAAAQQQQAABBBBAAIGCECAYUhDDSCcQQAABBBBAAAEEEEAAAQQQQCBdgaTTZLp0bCejhg9K91jshwACCCCAAAIIIIAAAggggAACCOS9QMJgyObtu2TmvHdk0kNjpGGD+nnfERqIAAIIIIAAAggggAACCCCAAAIIpCOQcJrMQ4/9SeKtJKMHZTWZdGjZBwEEEEAAAQQQQAABBBBAAAEE8lEgYWZIPjaWNiGAAAIIIIAAAggggAACCCCAAAI1FSAYUlNBXo8AAggggAACCCCAAAIIIIAAAr4SSFozZOKjT8ruvQerdIhpMr4aYxqLAAIIIIAAAggggAACCCCAAAIugbjBkLLTZ+S3U2fIwMt6Sd+Lu8cUUv3jtDly3ZWXyIB+PYBEAAEEEEAAAQQQQAABBBBAAAEEfCeQsIDq5D9Ml0kPj7E7NPWp2TLl1xOkedNSWbV2o7y8YKn8btL4Ol9lRtsy7hePV6CPGDowpl1OUGfhkhX2Pr9/dHzMUsHu18fLdpm3aJn85okZ9mu9xz589Li4i8w+9+fHkgaIUu2frC3udrj7oMd0xqlb5w6+O/loMAIIIIAAAggggAACCCCAAAJ1IZAyGNKiWalM+ctMmfzzsXYwRJfcdQdH6qLRzntqkKBjhzZ2EMIJfLRr00J+NXG0vYtmseim/+4EIx6ZONreX/vxX1Omy39PniAaSNBjrVj9ZUUwRYMTT06bI08//ku73+5juTNnRg0fVOVYXpNU+ydry+ny8gp/Pa57LLTNumkb2BBAAAEEEEAAAQQQQAABBBBAID2BlNNk9EZbAwFdOrazb7q9QYP03qZ29nK3TYMI3qwJd0BD9922Y09F4MQbkHD3WVvvDo4cOnI8JiDkDXZ4e+sNIHn3T9YWPdbMee/7lFzGAAAgAElEQVTIpIe+z9J5eraMHTVMvEGq2hHmXRBAAAEEEEAAAQQQQAABBBDwv0Baq8m4p3i0b9tSpj3xiJ1NkW+bO9jhDW5oW93Bkqeff81uvpNF4s4c6d2ja0XNFCfrwn28Q4ePxWSN6HHc7+118WaZePf3vtbdlu7nnxs3M+S95WvstyErJPlZGAqLRMLRfQ4fsWTHzoicDYmc3ykgzZqJBAMihikSMPPtbKY9CCCAAAIIIIAAAggggAACuRJIKxiSqzfP5nG9AYd403m8wRAn28W+Uf6+BohOo3GCIXeNHFxRB8QbDPHWTUkVDEm2vzcLxTulx1szZMg1/SsCJM/OXizPzFpkU7rrluzevTubvL47lmEYUlJSKlu+FfnwY0tOl8fvQoMSkcv6mdLzApEzZ45LJBLxXV9pMAIIIICASL169eTs2bNQIIAAAgggUDQC7du3L5q+5qKjBREM0UDI5CnTYzJWCiUzJN6qPU6tEPdKP7v2HoiZunPwYNUlkXNxAuXjMUMhU0pLG8n8xWHZtdtKq4mtWorcPiIo5adPSSDwfSpJWq9kJwQQQACBfBDQILhlpfednw/tpQ0IIIAAAgjUVKBly5Y1PURRvz5hMMS7+olbKd7KK3WlGC8Qom2Jt9KKH2uGeKcjab+cIqqbtu6sWNnHXWhVC74W81Z22pLp/6heQGPcPUFpUtx8xXzq0HcEEEAAAQQQQAABBBAoEoGEwZBk0z7yxSZeLQ532+pqNRknkDR65GC7pkdNVpNp2KB+DLd7BRnNfnGKq3ozQ/JljGq7HWfOiMx9PSQHDlXvnRudI/LA3UGpV696r+dVCCCAAAIIIIAAAggggAAC+S+QcmndfCyU6rBqsMOpl+H8N3eBVycIsXDJCvvPv390fEzBUQ2mjPvF4/bf4mW7uGt1jBg6sGLZXd3fmznjrtfhDYak2l//nqotuo87+OEESdxtdLch/0+97LdQi6V+tj4iy1fWrO6H1hAZ0N+U+gREsj9IHBEBBBBAAAEEEEAAAQQQyAMBXwdD8sCPJuSRwJGjlvzjpepNj/F2Y/TtAWnXxsij3tEUBBBAAAEEEEAAAQQQQACBbAkknSbjXm0lW2/IcRDIlcD+A5bMmpedYMgtN5rStTPr7eZqrDguAggggAACCCCAAAIIIFCXAgmDIfGmZNRlQ3lvBFIJfPpZWP79cXZWErj0EkOuHRhI9Zb8HQEEEEAAAQQQQAABBBBAwIcCFcGQZKvHePuVT6vJ+NCcJudA4OxZkfc+CMvGTdkJhnQ615CbhwWkpCQHjeWQCCCAAAIIIIAAAggggAACdSqQMDOkTlvFmyOQocCpMpGFb4Vk974MX5hg92alInePChIMyQ4nR0EAAQQQQAABBBBAAAEE8kqAYEheDQeNqYnAByvCsmZddjJDenQ3ZMiggNQL1qRFvBYBBBBAAAEEEEAAAQQQQCAfBaoEQ5wlXuMt05rsb/nYOdpUXAJbt1uy4K3sFFC97ipD+vehZkhxnUH0FgEEEEAAAQQQQAABBIpFoEow5I/T5th9/9XE0XENUv29WODoZ/4JnDghMuPFUFYadu+dQWnVMiuH4iAIIIAAAggggAACCCCAAAJ5JhATDHGKqD4ycbQM6NcjblM1O+TJaXPk6cd/Kc2bluZZd2hOMQucPi0ya15Ijp+omUJJfZH77w7KOQ1rdhxejQACCCCAAAIIIIAAAgggkJ8CVYIhk/8wXSY9PEa6de4Qt8W65O7Up2bLlF9PIBiSn2Na1K06cVJkxsyaZYeM/VFQWrYoakY6jwACCCCAAAIIIIAAAggUtEBMMKTs9Bn57dQZctfIwUkzQ15esFR+N2m8NGxQv6Bx6Jz/BMIRkXWfR+SDFZFqNX5AP1Mu629K/XrVejkvQgABBBBAAAEEEEAAAQQQ8IFAlZoh8xYtk2079iStGdKlYzsZNXyQD7pHE4tR4OgxS77eLPLRqsyKqfbuacjl/UxpUmoUIxt9RgABBBBAAAEEEEAAAQSKRqBKMMTJDlEBd/aH89+/3bWPeiFFc3r4t6NnzoocPWrJvDfCUn4meT8MQ+SOEQFp1dKQBiX+7TMtRwABBBBAAAEEEEAAAQQQSE+gSjDEeZlmiPzmiRkxR/n9o+PJCEnPlb3yRCActuSLjRE5cEhk/wGRAwct0ak0rVuJtG5pSLs2hlzcwxBDIyJsCCCAAAIIIIAAAggggAACRSGQMBhSFL2nk0UjcPasiGWJ1KsnEo5YEgkbYpoiwWDRENBRBBBAAAEEEEAAAQQQQACB7wUIhnAqIIAAAggggAACCCCAAAIIIIBAUQkQDCmq4aazCCCAAAIIIIBAYQlonTCd7HqqzJJzGhoSiYiUUAOssAaZ3iCAAAI5ECAYkgNUDokAAggggAACCCCQWwGtC7ZqjSUHD1my/6Alx46LNG8qdkH05s1MubyfwXTY3A4BR0cAAQR8LUAwxNfDR+MRQAABBBBAAIHiEig7LXLypCWvLEi+YlyTUpFRtwSkYQPDrhnGhgACCCCAgFsgbjDk8NHjMvkP02XSw2OkW+cOMWKr1m6UlxcsjVl2F1IEEEAAAQQQQAABBGpDYOfuaCAk3e2+uwLSojmrxqXrlS/7hUJiz3/SDKDDR7QQviEtmkWL34fCIiX186WltAMBBPwqkHEwZPP2XTL1qdky5dcTpHnTUr/2m3YjgAACCCCAAAII+EwgHBb532f0Ljn9rV5Q5GcPBiUQSP817Fm3AroK4OrPLPl8Q1hOlcW2pWEDkYsuMGXg5abUJ+OnbgeKd0fA5wIZB0PmLVomK1Z/SWaIzwee5iOAAAIIIIAAAn4SOF0u8vrikOzZl3mru3Yx5IbBAalPNkHmeLX8iiNHRBa8FZLDR5O/sU6Duu3mgDRvRtZPLQ8Rb4dAwQjEBEM062Pio0/K7r0HE3awfduWMu2JR6pMnykYETqCAAIIIIAAAgggkHcClmXJ/z4TtleLyXQrbSxy/+ggBVUzhavl/XX6y3MvhqpkgyRqhmaGTHiArJ9aHibeDoGCEcg4M6Rgek5HEEAAAQQQQAABBHwjcPyEyLMvZjZFxt25h8cTDMnnwdapMStWR2TNusyiXX16mXL1AJPllPN5cGkbAnkqwGoyeTowNAsBBBBAAAEEEECgUuCrTRF5693MbpTdfqNuCcp5sesCwJtHAmVlItNfqF6wa/zYoDRulEedoSkIIOALgYIIhiQq6lp2+oz8duoMWbhkhT0Yv390vIwaPqhiYHRlnHG/eNz+9z49u8rTj/8ypiis1kf5zRMz7L+PGDowpk6Krrjz0GN/kvUbtth/f+7Pj8mAfj0SDnqq/ZO1xd0Odx+Srfrji7OPRiKAAAIIIIAAAmkK7NlnyZzX0l9FxnvYB8YEpVmTNN+M3WpdYO9+S156tXrj+6ORAenQntohtT5ovCECPhdIGAzx3ry7+xkvcFAXDu42xmvTH6fNsZv1q4mjxdn3kYmj7aCFBlD+a8p0+e/JE+z6J97CsBqceHLanIoAiftYTpBl4GW97OCK91hei1T7J2vL6fJymfKXmTL552Ptwzr/rCv5aJt1cwd46mIceM/aEdBq6rqcHJXT0/MuLxcxTJGyMksaNjRELKFwXnp07IUAAgjkpcCZMyL/91z1Mge0Qz//WTAv+0WjogJrPw/Lsg+tanEMvNyQKy5luaBq4fEiBIpYIGEwxH3zn+8+8TJD4mVNuPukgYRtO/bYgRLdvAEJ3bdLx3YVgQZ3cOTQkeMxywt7gx1eL2/7vPsna4sea+a8d2TSQ2Psw059eraMHTVMWjQrjQmM5PsY0b7qCZwut2TXHpGduyKya68lLZsZ0q6tIU2biLRpbUoJVfGrwJaXW7L1W5Gt2yNy4KBlV6PXivOtWxrSvq0hF/dgXnH1zkZehQACCNStQKbFNd2tbd1SRKfJlJTUbR9498QC7y4Ly+cbqxcM6XFhdLUgNgQQQCATgYIooBovGBIvW8Od/fH086/ZTk4wxJ050rtHV3t6jZP54Q2WHDp8LCZrRP+eLHjkzTLx7u99rbst3c8/N25myHvL19jtJyskk9PdP/tqkbhjxy15ZUHidNErLjWlXx9DGpSQFuqM7ImTliz7MCKbtia+mNI02puGBKRx47o/H06dssQwDTl4SGTz1rBcdIEpzZuJWBFDGjSo+/bRAgQQQCCfBMIRkU/XRuSjTzKvG3LT0IB07Wywmkw+DainLdt3WDJ/cfWmyQwfFpDuXbkeyuPhpWkI5KVAQQdDpj41W6b8ekJFHRBvMMSd+REvGHLXyMEVdUDcwRUNhry8YGlMDZFUwZBk+3uzULxTerw1Q4Zc078iQPLs7MXyzKxF9snlrluyf//+vDzhaFRqgUCgRPYeqC8L3059sdelk8gPBxtypvxE6gMX+B716jeWxe9YsnN36o42aSxy748CUlZ2LPXOudjDqCdiNZC5CyJy8lTVN2jbWp9gBuTEyZNiGtW7MMxFszkmAvksEAwGJRSq/hSKfO4bbasUKCkplXkLNfMvfZUu54kMHWxI6Cy/lemr1e6epmmKmI3l2ZnV+817YLQpweApCYer9/ra7S3vhkD2BFq3bp29gxXhkZJOk3EHC/LZppAzQ+IVZXVqhfS9uHvFFJpdew/ETN3Zs2dPPg8ZbUsgoBcDDRo0kWnPp/9jPuRaQ7p0PCOh0OmidQ0ES2THzhJZsiz99NrL+xnSp2dIQqE40YgcSppmiRw6UiIL3krd1nvuNKWk3gku7nI4Hhy6cAQCgQCflcIZzoQ9MQxDItJEXn0jfjDZ+8IWzUVuuykgodCRItDxdxfr1Wsis+ZZUpbh5YzWUrv3R4aEQ3X0gMPf7EXTev3u0N+JSCRi/69Qtnbt2hVKV+qkHwmDIRpgcGpVNGyQ34UJCrlmiBZ3dW+aNeIUUd20dWdFhoq70KoWV2Xzp4BeAPzrvbBs25H6Rtndw5/cF5BG5xRveuiZsyIvzQvZ9UHS3QKmyEPjg6IPo2pzy6QAoNaE+ekDQdG2siGAAAIIVAqcPSuy8tOIrP4s8U3NVZfrdFJT6tVDzi8CR4+JPD87swwvzfRs1aJ4r4H8MrZ12c7yMyLBgMh3uyJ2zT0NoOm0OxYlqMtRyY/3TjhNxr1srLep+bKajNOuREvr1tVqMs40l9EjB9s1PWqymow3EOVeQcYdsPJmhuTH6UUrMhXQi7vZGd7U63s8OCZoF1Ut1k0D/P/z98wuntRq/NigNG5Ue2qny0XmLwrJ3gxmsfXpZcqgq0wJUBeu9gaKd0IAAV8IaCD8+HFLdLW1nbsjokvvdmhnyLntDSmpb0jzZvok2BddoZHfC2iR3G82R+RfS9N7cn/9IFMu7GqyWhxnUFwBDYLs3mPJ0uVhOXa8chcNgrRrY8jtI/iCKPZTJ2FmiB9g4i3/+5N7hlcURXWCEAuXrLC78/tHx8cUHNXCpuN+8bj9t3gBHnetjhFDB8bUCPG+t7tehzcYosdPtr/+PVVbdJ942TruNrrb4Ifxo41VBap7Uz/8hwHpfn7xPhXZuTt5sdlE59qwH5jS66LaS7vQqczT/xESvYBPd2vfxpBbhwdYOShdMPZDAIGiFSgrE2nYsGi7XzAd1wcHR49Ff9eTlQG6c2TAfhDUuFHxXv8UzKDnoCMaJF35aVjWfZE82/qeUQFp3YpzKAdD4ItD+joY4gthGolABgKZTKFwH/b660zp3bP2buoz6FKt7HrylCXP/DP9OitOo+6+IyBtW9feD6BOg9JgSCZbMCjyH+NqfzpPJm1kXwQQQAABBLItoA8O9Kn+jp3Rgrn6wEhrRZ7X3pT27STlanoaSDl1SqT8rMjWbyPSrrUhrVoaor/6BM2yPVr5dbyzIZEvNkbsFQZTbQ0bRDOFySJLJVWYfycYUpjjSq98KqDTZGbODcWk8qXTlftHB+0lWYt10wuk/3tOi6FmJqA1Q+oFM3tNTfbevUfk5dczbKSI/PT+oJzD086a0PNaBBBAAAEfC5SXRxtfUpJeJ06fFlm/wZKPVlV9UNKkVGT0bQEJBHU6VXrHYy9/Cew/IDJrXvrXW5f0MuU6piT7a5Cz1NqEwRD3FJP2bVvKtCcekQ5tW8lvp86QgZf1iplukqW2cBgEil5Af+zffDcs2zMsoPqzB4LSoEHx8mlK7asLQrL/UPoGegF0z50BaVJae5khliXy1+np/zhrb5o3FRkzKkgBwPSHlj19IqC1AQ4fsUSnj32zJSLt2pjSuqUhDUqkqL/PfDJ8NBOBvBXQLNsly8LyzZbk0yOKvd5a3g5gFhq2Z68lc+annzGsdYZG3hig9kwW7P12iJRL6958/UCZ+vRsGTtqmOjKJlrb4uUFS2PqZ/it07QXgXwWOHbCkudeTP8LfODlplx6iSk6naKYtxOnRGb8M/1Aw923B6Rtm9oLhOjYaNDmlddDcvBw+iOltWCGXGdKwwa129b0W8ieCGQucPyEyNebIrJ8ZdUUZuepbb36Rq1mbmXeC16BAAL5JqBBVv1ueef91NMjNONSAyKsNpRvo1jz9mitkBWfpL8yoxZUnaCr91FPteb4PjtCwtVkJv9hukx6eIydDeIOhiRaucVn/aa5COStgD4l3fB1RN79IPUPeeuWIj+6lR9yHUx127rdkkXvpA4kDbralF4X1k31eZ23vODN1GPrnKA/vicopayWnbefVxqWucDpcktWfBJJWdSu2JcMz1yWVyCAwJkzlsx8OSzHT6ZncetNpnTpVLw119JT8t9eyz8Oy+rP0g+G6APFCfcHpF49Hjz5b7Rr1uKMgyFkhtQMnFcjkI7AyVPRomHJbux7dDfkuqsCFAFzgeoc4aPHIzL39YgdHIm3jbzJtIumntOwbn7wdJm39/8dlo2bUv9ID742GrTJVdbPiZOWBAMi3+225Lz2hoQjhjQ6J50zlH0QqL7AN5stWbwkddBSM0TuviMoWtyODQEEEEhHIBSy5KkZqb9fnGNd1teQa64kHSAdWz/t890uS+a9kf550L6tIbfdzDQZP41xttqacJqMLtm6YvWXMvnnY+WvM161p8m0aFYqDz32Jxk9cjA1Q7I1AhwHgQQCWgxUb5y/3hQWLQS1e68lLZprJXSR1q1MOa9DdG49W1UBDSadKrNkx3cR2bnHEl2etuO5pjRoaEjTPMiyOHFSZN0XEflkbeIMkRuHmNLxPDMnhVN1StHBg5Ysficcs8yvponeNDRgn2MsVcgnKxcCujrEv94Ly+ZtqYOB+v7j7qnduj656DPHRACB2hPQDNEFb6V/E3xee5EbhwZ5EFB7Q1Qr77T/oMisV9KfOn1Rd0OGDQ5IgCShWhmffHqTpKvJaBbIuF88HtPe5/78mAzo1yOf+kBbECh4AV1lRp92GGbiAIjOk42ELdEirAcPG9KhncjZkCWNzqmbDIh8GRQNKuUqs6ImfdRAl2b/7NkXXTLwwCHLzlhp3Urkgq6mNGpk2FkbyTatQVJWZsm+/ZZdFb9NK8Oe+5zsSbpmzGz8JiJLliUOxFx/nSE9Lwwwd7YmA8xr4wpkumLWiBsC0q1LcX+HcSohgED6AmSGpG9VyHvqtd+n6yL2lMxUmwZAdHVBk0BIKqqC/DtL6xbksNKpYhNIVIywcaPo8nElJdGbZLbsCoQjIgcOWnL0mMiW7RFp1VykVUtTNN0y3eX/tEXl5ZZYliGGKWkt86eV8s+GRF56NSSaZeLeWjQTGXVLUM5JMN1FM4xeTqPC+p0jA6LV1dkQyKZAWZnIc7NC9vmbzjagnyFXXUEKezpW7OM/AQ2K67fsocOWlJWLHRDXG7J0sz5PnRLR36Fvd1rSsrlIaSOR+lp4uIh/7/Um+IU5IdHronQ2nRrRuSO/delY+W0fnTr93r9Tryqk0zHbtvZb72hvtgSSriazZ9+hmFVjnOV2WVo3W/wcB4GaC6RTjHD82KBoYIQtewI6FWf7jvgV6zu0N+SGwZren733cx/p7FlLnn42eRrwz38Wf3mhf68Iy6frUk9RuPQSQ64dyE1obkaweI+qmWsL3g7Lrt2pz0FV0uWvdbldNgQKTUADg+/+Oyybt8Z+FjSoceetwaQBEc2w0s/SrHkhKTsdK9O3tymX9zOLdtqHZsl+lSL70RHT1WTG3RtMmYVZaOdeMfVHHx7p0u0ffBSJmRasBm1a6SIEAYlYhug0YbbiFIgbDHGCHneNHFxlSgwFVIvzRKHX+Suw8WtL3l6a/Ma4tLHI3bcnzhbI397lb8u2fWvJ628mdu/QzpBbb8p+MS59erjwzZDs2pvc5vxOIjdeH5T69Sv302k1Widkx87UN6IdzzXk5mGBtJ9Q5u9IFWbLdCz16a/f5jfrNK1lH0Vk/ZepU5d15B4YE5RmTQpzDOlV8QroDdrc10Ny4FB8A80O+X8/CYhhxA8E6oop//dc4t+frp0NGfaDgDQo0uLD6rtkWeqMAF1WtynfLwX/QdQAmf72RCKW7Noj0qKZIc2a6TRjyUldtoIHLbAOplxNplvnDjFdZmndAjsD6I6vBfQLXp/0r/si9c3tQz9mCd5sDbZmhfxzTsgucJtsu3loQC7olt2n2jrmz86s+jTQ247mzUTG3BE75vokceHbYXv1mFSbri6j9Royme6T6ph18ffTpy0JhQ3Zu0+kQQPLnj7U+Jz4aeQnTohELJH9ByNybjvT/md9cpgvW7R2kMiXX2tmhUijRiKtWmh9F9NXafF6Ufr3F1J/fob9wJQLu+VuNaV8GVfaEV9Av18PH7Hk4CHLngrSto0hzZsWxhNcrWOw8tPkAcGuXQy5YUigyhNrDYTOXxSSvfuTnzlDrg1In17Z/f3xvqN+J+nYaMxGa1wF8iiZUKdIrPsyfs0ILaR+121Bu56Y+4EBn0UEECg+ATJDim/M6XEBCZw6Zcn8N6OrzaTaNEuhS6fcXhilakOh/F2DCtOeT1304Ir+hgwckN2rw8NHLXnhpfQq5Y8bE5AmTWLH/IMVYVmTxjSZ/pcYcvUAfxdR1Tnjb71XdUqGppBf3MOQpt/baBBEXV9dGOvavKnIHbcE8mJlHa2xoQGdeW9UPe/sdo4ISuPG/vmEacHgV98IV0nxd3pwzRWmXHSByfQ+/wxpVlt67Lgl77wfEV0e071pQOTmoaY0KfXvb5n+frz7QeqshZYtNIU/WKWOlAYTp/8jVCXl3zsA+h1+XY6mOur3kT5VX/FJWPbus6RBiX6figwbbIpp5s/YaPBY66qUn7Hk680Ru55X2zamaBMbphHo1gyT4ycs+3tKg3M6ZU8LlPu5Jov2SSRabL9+SbRQez4FsbL6RcLBEEhDIGHNEJ0OM3nKdJn2xCPiZIdoVsjER5+Uhx+8jaV108BlFwRyLaCFN3VVkE2eOcfx3pclKrM3GqmmyDjvdH5nQ268vuqTvZq0JBIRmfZc6gKUOjXq/tHRJ1/u7dvvRF5blDqQk05ROV2+WC+C9cmg1jE5p2H+XATrhd5ri8Kyd3/8LJjL+5syoF80o2LnbkteWRA/wKTziCc8EMzaxaJeiKrXrt0RadrUkJL60YvrVCseaTbSM/9MPG4d2kYzedK5wK/J+ZfN1+pN3YcrI/aTfx0nDebozYZmurRrU5xFIHWc6wVFdu2xRKeqnQ2LNHBNdauuv2aU6Q1sQx8sx66fXZ3Op0VB421aZPT24dnLWtObXL2hP3I0+r/OHU27eHSqz2R1x+JUmcic10Jy7HjqI4y7J1il9pQWW/3ny6kD4h3ai9ycgyVjNcCwa68lr3mCx05v/FCjLJrVacl3Oy1p3dqwi9iWNo79/Tp6XOSrTRFZsSo2g0eLrf5wcCCvsgZTn0nRPSxL5I23Q3LokIj2r3VLkfM7m9K7p5EXQf90+8F+CGRTIOlqMk7wY/fegxXvydK62eTnWAjUXGD5yrCsXpt62sN//DhYEAWi9ELZDIicPBW9+bYiUutTOfQm7n+fSR1QuG6gIf0vyW5miD6N02DG/sqv5bgn0XnnGjI8Ts2PM2dFvtwYses2JNoGDTSlV08z4fmixzh61JI33g5XVOzXAr1ao6RJqVXlorLmZ3nmR9i63ZIFbyW/YRh3b0DqBQ15cW5I9CY00XbFpaYMvLzma+7p2L31btWbvNtHBOzpLsmm5KxaE5aPViX/nP/sweRFFzNXrJ1X6Gdab9Q1MKVPbP381LUmYpoNMff1cMwKUXpTftNQLYZZvUCjThX4anPEnm6iq17pkuuX9Q3k9RKSBw9FZObc5FNI7ro1IO3bVc/EPUaaPbZ6bVjWfRn72dJgsmZbNWtakxGN/9p0H2LoymC6yoX382AHxJ8PiU5RSbblKrtPz6UX5iT+blW70bcHqn3OZl889ognT0a/h93TRXWajxZrbloaDcLqb/zazy1Z/nH8fmpA5MYh/qrJon2akWCKrQZDNBtPVx5kQ6DYBFhat9hGnP7WSECf6OhTu3y6WLcsS/73mbDoBVKi7eorTOnXO7/n3jtPRMvP6lKDVtynFJru+snaiL2MrT5V09Vaup9vyqV9zVp9SnPypCVzF4Ttm4tk2x0jTOl4bs1vor3voU8v/5FiqsxP79cnV/EvbPQGYM9eS95+L2xnKTibFuPUOert2hqiF7SJtv0HLZn1SvyLRF3W97zYUlM1+sxV98Ufrw7Lx6uTBw/uvj0grVsZ8j9/Tx7Y6tbFkB/GmbufSdtSPe0e+6OgaFp8vE1rBOjF+/YdyfuTzlQ4/Q6LhEX27o/YT7/NQGY1GLQt7pqOJQmyFnTJ5zNnLTl10pCmTS17uc9E+2biWKj76hPbv06Pfx62aWXY07Uy9dPMrVWfRuSzODWl7rsrIC2a5+eNzzebLVm8JHkg89orDbm0b80CzXpzuGqNJSs/jf9eOv1Mp6lUJ9tKP+/HT1qiQVnN8DnnHEOauL5TNVwP2lYAACAASURBVCNKf8uSbed3MmTY4ICdOebe0q0Zcv21Aemdg5oh6WQX/se42OLd+fK51cw8LXyumVfxtp/cFw3iaKbj356P/X307n//6IA0b5afnyFvW/Vcf//DiHy+IfE5l4saZ/ky7rQDgWQCGRdQhROBYhTQQMP7H4blwEERLbzVpo0h3bqYSW8Ya9Np995omn+8gIhG/K/oH8jbegL6dEsvGl9+LVxRkFQDTnpj17x55dNyfZr2/vKIbNxU9SKm54WGDLo685uFmoyRZqY888/EF+yDrjKl50Vmxjcw6bRJMzP2H0g8teOu26KZBsmCdprqrBeGWiRUlznV5YD1qbwWk0uWHq79fuX1sBxJEAjSG7b77graxT3rcvvgw7Cs+Tx58ECnAqnTMzOTB0N0ZaDhP6xZWrQ+9X9uVuLzRadU/TDB6g8asFr677B8sTF5f7wBFX0Cagaic8Pr1TPssZ41NyR6M+VsesN1/SC9AUg+WnrO6WW/Tl/QJ8N6nmg9Gn066j5fNMPjwEFLXp4f21dqgCT3TXW+apZCx3Mz+0RpxsPylfHPGf2cjr0rP5dcr61giJ7TL80LyeGjiV3H3xeUxik+G95X6+fu9TerZu/dOTIgOsVHPy96s/3i3LA9VSHR9p8TgjGBx5iAyGmRv/0j8fdWp/M0oyg3q4FpvZPPNyT/LhrxQ1O6nZ/9BwGZfQKq7r3vgCWz5yX+Hu7R3ZAh1wXkxMnk2S965BuvN+Wi7vnXx3hGOi3o9UVh2b0v8bgN6G/IVVmucVbT8eL1CNSGAMGQ2lDmPXwtoDfrTz9b9aLjyssM6dc7e/OWa4qkGSIfrorY2QpHj1nSvo3xfdAmWpcgX7dktRA01VZrB+immQxzPDdY7j65962Nvup5of+bMz927rdmV+gqGB3a5zZYpu+tN7U7vovY87d1KcYO7Uzp2lkDGrkbbz3P/jo9+VPbfFi56NvvLLtmSLJtwv1BqVc/9eo8l15iyLU1LET45VcRuyBkok2DEffemfgp9Oq1EVm+MvmT5B/fG7QDtPY0pmOWzJ0ftqef6KaZB5f2NUSf6mqNDvemq1ZoICbZykEaPHtqRtXvQX0/DX45gbdkKfQaIOzTy8xa/ZXa+JzXxnskmj7lfu/L+xly9RXpZ0JooPNfS8OyeVvim5+f3h+s1Yy6dC010DsryQ2rHicb02SOHRN5bnbyQKhmhPW8IP3vUx3LN94Kye598Xv74D3RqRi66Q332+9VLRJb2kjkzlsDSYvE6ve/vteseVVXZdIb+quv1OLD6bc73bHR/TRDbf7i5N+t+Tplb+3nEVn2YeLvUZ2aNGpk0A78Tn8h+bmhdWs06JQPm2Z+7NmnmUgRO+NLx75VK0PO+T6rSK+zZr0SEs0MTLR172rIsEEBVtfJhwGlDbUqkHCazB+nzZHrrrxEBvTrUasN4s0QyCcBvdlc+HZIdu6O36o7RgTsFNh82rRqejhs2Dc2emOe6aZPEDJNx870Pdz769LAnyZY3cS+SRsczfj47POwvP9h4gt7DUD0uqgaHa5J40Vrl4hdW+O73SKtW4kEvq95kKvie/Gaqze/Wg2+OuOdafcjEUv+5+8pLoQf0LnUsZ8L/SyFQtGCq7VhozcLL8wJxdRfcPfVmfqiQaTVayz5OEGqvL4mneLDemOj9UdWfxaWC7qaUlpq2JlaTh0QvVCd81piNy1kp1OMEgUkUj1J1jovvXtFp8JpW2bMjH0vzQ7R1PDbbw7I9u8iVTJ7/nNCQAz3/BcXln4nvLss8eoXOg1PV+jRLdn0pFa6OsZthVG7KNPPTbL99TvbLoS9JfH3W6b1h/SmZ+7rITmSJOshF0/vtVCrfvKTrU6hQYjGpZqRpktDR78XGruKV6aaUpatAqra1udnJa8XdN/ogLTIYCpEqu/HW24IiP6uOZv2tfysJQcORFc8ad/GlAYNdBnw9M4wzdQ7e9awg+LNmumUtOi0twY5LJR78JDIzLmJAwX6nXf3HYG8qB3lVdyyLVrrKtGmUwdH3hgQ59xwgsnx9r/nzqBdgLSuNw10/+35qkExnUrWu2c0uKHXCP96L3lw9PrrtJBq7V9D1bUf749AwmCIFk+dOe8dmfTQGGmYjVLmWCPgQwH9AXnhpcQXS0OuM6VPgfx46A3P4cMR+XyjZf/AX9g9IOGQ5HR6jaYTL34nJLv2xj859KJKn5afc47I5q2WLPxX4ouYW24wpWsXfshz/THTm6yXXwslTO+2p8mMriyep7UjdOm+Dd+E5etNluiUph4XmhIOGdWai59J/w4dia54oG1wb+d1MOSGwWbFDZgurbtyTfzUb336p4UadepWoi3eUplaUPb2EUHRJ426aTbGzLmJz99u50ezM/TCNdGm7Vz0Tth+Aujerh1oyoXdKpeh1QK57yyLffqpK1Bo1lj/PoadtaSZKu7t1ptM6dIp/udH+/fy/JAcOhK/ZRd0jU610VjK4n+FZPt3ifswbkxQmjTJZBSLY19dsWLlmsRPrG8fbkqn89L/ftPfLp1atfGbxAGWieM00JydYL4GhTUA+dWmsF18sseF0SC2d/rVkSOWfLAiIlu/jbZLM4v0nOzeVZewrhzrZEvr3jjElGZNa95uba8+7Ph2Z+JzbPy9mS1ZvXNPdBphoq1Pz+g0DD9vGij4bmdEXn8z/vnqZKjlYx937YnI3NcTf856XGDI0EEBO5Nu2w5LFiW45risrylXXhZbh00/c5pBp1tt1pZLNm3pgbsriwBv3xGR+YsT933ig4mD8fk4lrQJgWwJJJwm89Bjf5L1G7bEfZ8+PbvK04//Uppr8QQ2BApYQH/Y/vFS4qfLQweZcnGP9C9Q85VKbxY/XFn1wlkzX7SYZrIbwZr0SS+al30UlvWeSv7OMTXr5ubvV0TZuTsiryxI/EOejbTpmvSlmF67b78ls1+Nf8GvN9XnnWvaARDdNMimSwF7t2Tz4bNpqTfyBw5F04e1EGLrlqY9b9+bgaHt1No7Bw5E5MBhkU7nRoMGejOX6vw/cEjsFWm8W59ehr1yhxb61RsIffKvRWvjbT//WZJoi+sF2p+IZdlP1bVmh3PD6X4S//a74Sq1dZzMEF1u89I+AfnCEwxJNh5qs/Ct2NUX3H3oe7Eh110VXaFkxSdhWflp/BtwLRCrBSlTZZ7pTareWOj3Uotmlpw5a6SsaZLNc6YujqV91t+aeKsaXXSByBWXBuWTT8PSpZMhF3Qz7cBDqkLeyb4ztUbQLT/MzmoYmp2waUukSube1QMMuegCnS4YDVxo4eZ1X8Zf/Sxewc1ogN6Sg4ct+/Ojv0U6xSSbWQ9606vfT3q+eTfNbtDviky3v/wtcdZEdWq/ZPr+tbF/2eloBtrHn0TsZbH1M61ZKVpDSLdkQd3aaF+i99BzSgPBH8RZTU2/53V6j/Ndqv3bszdavNpdaPyK/qb07GHa9eOcTb+rNOC88ZuIHUi5sJshbVqZOa+dlSrjw11HSrMzt30bsadmebc7R+py0v6/lq3Lc4v39q8Aq8n4d+xoeS0I6I/HondC8l2CJ0eZPq2rhSZX6y3C4eiKNN5Nn/jqTY77iV213iDJizZtiRrH2669MrpSjG46B14vNJYur/pDPvS6gHTvxmoV2R6bRMfTC2Fd0Wbh2+GKOciaxaMr0egKDDpFRDcNdn2+MSzvL696c6zLhWo2g983DZj+++OwrIuzYocGXOxist8XYDx+wrIzRD5Za4kW8mvUUKRZMy0WnLhQYnV8NOiiGSTuTcdix05LLutnSOuWRkzGgM5715UEEk3R0T5+tCoia9bHD0YOuTYgGvjRLVmBwoGXBey6JcmmSelNvk7n+WhVWPYdiE7Z0yLQfXvn9nuoOs7Zfo2m5Gumghbq1gwsDaJptk6bVlKl3sz/99NgyuVxT50W2bfPslfPcG8aCNGb1kQrRmngwQlmptNHbetrC0OiQUH3pu0fM0qLeEbPjdOnLXnptfircA251pA+veomY0I/G8s/jthB07Iyyw6ADLwimtmSKhDq9dHz998fR2T9l1U/Kxq8Gj82dTAwHfN82UcLm1ti2FM0tUBzqkBnPrRbg3Ja92T9hrDsPxDNTmrRXOS2m6sGpPW7T8dU+6aryLVqadh1mNz91OvEr76pOo33uqsM6XVhdMqNTgXTz1T9EsP+HOhnYs26sHTuZErL5tHi1jq9KdNN/f+1VFfYix+AvmdUdMU0Z9P+7D8YkRMnDdmxM2KvxteyReEHmzN1Zf/iEiAYUlzjTW+rIaA/HlpAVaP97m3wNab0vNBM+XSuGm9Z6y/56puIvBXnaYE2ZNy9wZglAbPduERPKwZeHpDePXRJwsp3PFkWLRi6aasl+/db0qa1PiU1RFf7yFWxuGz3t5COd+qUJSUlhp0arBdz3iUg7WlQ74bsLAbv1lVXTxlSdQUgfcKmF9Z6Y67ZDNVZ1rK2jRPVs9F6CDpVxqkb4rRLA3v6RK9+veiNRLZvIPTmTueQe+e76/sOvyEgyz4M28FF3ewpQ0NSBxr0c6pzzp3pDU5fdAWC/n20zkH0gltvHDQgoqtbuTf9PGthx1RTZHT8NcimT5vd270/iq78U+ib+mnRDV1GXM8bzbb532eqBot1mpdON0u16WdTp0edLo9+Z3bqZEijhlUzo/Q4+p4nyyz7Rl6zeHpeGJ36lCogsHe/yEuvxg9ou4tM6jk0e15swWmn/T+4OhrwqstNv2/0rFPz6tyYOm3Xm23NkNrwdeU5rAHRO0dWTlmoy37y3mJ/N1oRfchi2d9dWt+putks+p315jthu5C5e9Pi71rzbN0X0axbzXTt29uUUNiQ+YsqPy/6AGHMqMoi1JmOz5JliVcae/DugJ2xU51NjfR3QmvZaPAmk6k/Tobbhq+ivwO6sp5l6XVadVrCaxDIrUDCYEjZ6TPy26kzZOGSFdK+bUuZ9sQj0qFtK/u/Dbysl4waPii3LePoCOSRgAZCPlz1/dK6TUTatdHCqZa9Hn0hbHrzFO+CW+sYaGFG50l/rvqqF+wHD0efHOr/mpQa9rK6idKhNdVVL2Tsi9YkNRZy1V6Om56AjuvXm+OvojLyRlPO7xx7M6dP0Ba/HZatOyw7VVlvtPv0DOR9QEQzZabHWeZy4OWGXNwzULFkcW0UuHVGRp/Wz18YrfOhKd7NmopdPNV+Xh0x7NUuOp1n2YEnb7HbRKOrN4vfbInYS+dqsKpVC1M6dawazNGL6NOnoxfR+jS1aRMNakYLO6baEk3B6nWRIcN+UP2bZQ0+6fe41qzQ7zMrYkmjDFbb0D7p904krOdm7T1J3fZtdJlW76bfzTddH8jqyjzeegoajHlwTOqbtFNllrz6Rtj+DndvmhmiRSadYJ9mRq37IiKrP6v6FLvQ6hVo4CdgWrJztyFt21j275V+Bvyw6c29aVp2hla3Lqa9apk30O2HftRWG4+dsGTWK2E7eO/e9PpEP6OLl4QrHqbpZ0prxmjA173p6kHntqve+aHXb7rSl/eB3ZWXGnJp30C1Htjp952u4KcF7vcf1GteQ/QBoD6ASmdTi2nPx35vxZsKl86x2AeBXAskXU2mS8d2cvP1A2Xq07Nl7Khh0q1zB1m1dqO8vGCp/G7SeAqr5np0OH7eCZSVR5+SZZJC7HRCf7D0piSdG4La7vixY5Z88HHELlLq3m4fHrRXSPFeCOnFr/7wbvjKsp90nD5jSWkGNxa13b903k9vdPRmXC/cqzO+6bxHMe4T70KtpJ7IhHFBO6PEfjL3/QozW7ZF5I23Y9PL/XABpU+Cd3wXlnVfRrMi9POiN6uX9DLFMA1ZuTpsFyXu3jU7hR/TPY/0glRT8zVrR//ZW8wy3eN499MxTbZaSHWPq6/Tc+LZF0OiASb3NnyYaftVd9MnnPo01lnyVKcL9b04dUaMvp9ma2gASJcu1//v3Utfm7ulS9191IDSCy9VTkdz/nbbcFM6Z1BQNZWben/wYdVaM6NvD0q7Nslfrb8fW7ZHZNlHsb8fGgzU7BL3dBxd3Wbp8rDo0te66TmpBVQv6h7IeX2FVAb8PRrw0yK4S/8dHR8Nlk54QOsBGSKGJTu+E3sakV7LJJpmVWyOmgH5ydqwfOaZKqnFWPV78ouNlZ8L/e7UIrpan+qwa6Un/T66JoOls73Gej2my2jv3BWxp9c1a6rT64xqf6Y0IKYZJzqdyNk0IH3V5VoHJXVA5JM1YflwVez3wTVXRmtosSGQbwIJC6hO/sN0mfTwGDsbxB0M0VVmpj41W6b8ekJRF1A9fPS4uIvMPvfnx5IuQ5xqfw0yjfvF4/b54S1QO2/RMvnNEzPsv/3+0fEVWTl6TGecNFDFlr8C+sPy2RdhOXZcZEA/0553mm+bXgTt3Rexf7j1xu2i7qadMqxZGt5t996IvDy/8qb14fHBWlkuNVdmOrd+yfth2bnLkisuM+TiixLXT8hVG/LpuE4Ksabr6+inKtSYrO16c6tPyLSAqdZ80eWPO3c0paxM7Dnba9ZZdlHI6weZoitqeC8ob705IF065t/nxdtnDTZoME2L7ulSnPr/uuLF//y98oldJheT+XQ+1GZbNL1a08pXram8kNbzR2tk1GSLN5XjofHBlFNA9D01W+2d92Pn5dck/TyTfmiQYuu2sHywwrJvVHU7v7PWeNGVLLL3udBg0ao14SpZGw+OCdiZPak2Pd+10K3WTtApBxddEP0OLfWkxWtgSTMNNOtv196IvZSsft9kK1CXqp11+XdnCpQG1HTKV02+V3PVD71WefWNUMyNuhbC1Ycec+aHRZfV1W3EDQF7emo+ZIzkMjibyFnPYR1HrcPUTx8IlVvy/oeRiiCfFuC+akBAvvw6tkC8fjbuuysgL74Smxky4YFgXlg6/dXlr2e+ErIDwc7WtEm0AHY6n9WNX0fk7aWxDzZuvN60ryvZEMg3gYyDIWSGiDhTiJzpQhog+q8p0+W/J0+ws2e8W6r9va/X4MeK1V/a2Teny8tlyl9myuSfj7UP6/yzruSj++nGlKV8+1hVbc8nayPy4croD0P7toaMvEmLyuVnu/XiW+eJJ2vf4nfC8s2WypuVq6805fLvC53mZ6+St+qzz3UlhMof7ny7MKlt00OHReYvDtlPBe+4RZ/spr4ZSqeNesPlTGvSlPlnX6y8INSLa30C/cw/K/+bXmg/eE8wL7Op0umvd4pDdKnogG/S5dPpYy720Rsyndaydn1YOp9n2Etma6ApVe2KZG3R7B3NOHE2vVH/ydhAWgEFDdzNeyMUMw1kxA1B6dYlF72vekz1KKlvyXe7ojVe9MYrW59J97tp1oauaONsHdqJ3HJjMKPfKv2M6y9Dtuvg1I50bt9FA8O6RLVOO9BzZ9gP8m8pUw1GvrUkduUoLXatAbGXXCuI6Xf1iB9qNk/V3wY9X9dviEjb1qa0bZXZdLRMRkBrVmn9MM3Gu6J/IGU9okyOnWrf73ZZMu+N6G9V+zaG3HJjwA7q6Xe8Zmlo4DIQ1NWQIrL4nUjFKlFaVLXLeQF7VaWvNkWDYhf31OtCM+6Dp1TtyNXf9Tz4eHXscvPOtE8t/J1q08yh/5sRqliFRzNk9KGZXluyIZBvAgmnyTg35HoT/tcZr9rTZFo0K7WzIUaPHFzUN+De7BhvsMM7yKn2V+ttO/bIryaOtl/qDo7ov8+c945MemiM/TcnS0fHwh0YybcTi/ZUCugF0PsfVha40mJZd92e2QVmvnlq6uT8xZU3rRPuD9p1HTRjZN3nllx1RXQ5Ub9sekG16F+V/Ul3mVO/9C+TdupTtjeXhO2UW90u7B6tTZDtzTunWJf2a9HMlCPHIrL+C63rIPay1fXq5cfTx+r0X2/o/zE7VLHijs7h7nNxoEpB1eocm9dkJqBBXi1qqct46xP56wYa0qVjQBo3Tn0cPVd1Goiu2qCbfrc9cHfq1VxSHzm/9jhxSuwVjnTpUV2BQm+A9eYlH6d25pdceq3ZtduSua7CwveNDthZZPm0aSaA1op494OwHD0eXWJcH97opnWRnCWINVuk10Ua2I1tvV7vLP+4csqI1ozRTNNcbDrV6rVF0d/tiy8yZPC12a2hk6zNK1dHZMXq6PeBBv7uGx0/Y0KnVusMIzXt3NGQEycsadzYsIMjWn/IDBh25mQ+ZNh4+3vshMiWrdEHX1qsWQPT8TKF4znpeaQBEM2c0U2Lx2pWTLKVxHJxjnBMBNIRSLqajHvqhnOwVNNB0nlTv++jLk9OmyNPP/7LiqlCf5w2x+6WE9Bw9zHV/t7XOlNqHpk4Wrqff27czJD3lq+x34KsEH+cTfrETQMi+kN4zZUBe1qAnzedI6vLEOq0h359TGnyfebA3AUhOXwkuhTm9ddl/wY6V2Z6o7R6bdj+4R44IChtW1tyTkN/j1FNrHbuFnllQfQJ8Zg7AmkXTcvkPfVp+/bvIvLJmohdX6N/n4A0aBA9go6HZqX4vTiu3jho/RldbaZDe9POCPFOG8jEjH1rJqDfv8F60VUR9PxLJxDivKN+5+n5qHP9tZigYdYsU8U5bjqZeDXrNa/OFwENFGjGnX6/aj2JQVfnZ4ao3sDrr59m+eiNuq4AouepZjusXhOW9u0M0eW4E63gpqsRvffvaKDAeVCSizHQ2mV/fyEaDBn2A9Oegllbm3poEVRdKl2zPbqfH/D971U8O50OFA5bUlI/+ZLoteXO+yCQCwGW1q2GarypQqmCId6is+799Z+1WK0T2HAHQwb062FPh3HXDBlyTf+KAMmzsxfLM7MW2b0gUFWNwczSSzQlMNVKERop1/+5n6ToRUdAn7wVwIoo2jetPq9BBa2W3tz1xMs9PSJL5Fk/jGZEaDv9sJRr1jvvOaDWUNGbeP2fpv5mmvKuS3QeOmzJeeemDijpTame/7kqyJlrK46PQE0ENBi4Z39EbhySetWWmrwPr617AXtFo4glOmWrSZPUqyvpd68+Tc/0+7eue6rf/zp1RWujaTDFu7R4ttp38pQlpmHYGSxNS2v/t1tXzNLrhmC97I2RjnkobEnDktS/ndlyzNZxdCojxeezpclxalMgbjBEb86dG+yf3DM8brZDbTYy394rVaaHt72p9k+WGaLBEO/m1Arpe3H3iik0u/YeoLBtHZwo+uW/ZVvYLgh3QddAxqmOGjw4fMSypwMUyqZPTNwpn1p88I23w3LrTcGCCPoUyjjlsh96DoQjljTO0lKSGmjTqQ2HjugTKi226L8LxVx6c+yqAnrjGQpZUi+Y+0KVNQno6WvtGk3fZ0VlOpZ1UTwy0zYW2v46bUqT/3Nd92vPPsteynpA//zMIMnGuOoS4CdPRezVT2pSEygbbcmHY+zbHy0srsVXcxVEykU/NTCkiwS0bROQ89rndjqMM1WL6Xu5GMniPGaVYIi7eGfDBvXFm7VQnEyxvU5VA8RrlGr/ZDVDvAVZNWvEqRWyaevOimWO3YVWtbgqW+0IaNroBx9Fp7/cODRaDVyLZ23ZbknrFob9xCDZD5peCOgLNH2+UDf9kZz/ZkjuGE4wpKZjfOKEZlBYdoq+JjLn+mK8pu3N5uv/8rfotJ3bRwTseeyJNg1M6tPU2vhc6effb09tszkmtX0sO7suFH0aq1uypT31O/iNt8LSqoWI1i1IVLjPfTzNTsrkhqzstCW6HLSufHNJr2gNheoGNTK11O9V/f3QOig9LzLt5U4zuXnSG3rTtORsSOfyWwmnPGTarnzaX/uo/1Ojvn0C9hQ1b42LTNurGQ9aYLRBg2jRzFzWenBW6NF25+PKM5naeffXm9o168Ly8WrLXiHphiGBov8+PXrUkt37LOl0npnR57mmY1HT1+t30fOzQtLxPEOG/SB3wTt9eOgsRjDw8oC0bFHTlvN6BHTVcEtv3aKbUwj0rpGDK5aJZSndqqdJqtVhnGkuTqHZVPsnW01GA1Luzb2CjL7OKa5KZkjsONnzsEUkYmmxvOgc8VxtekPkFJnTKv8L3ozY88p1q+15rIn6qGm5ehMdsaTiab0W8AqHRAL1LCmpl3w+qE4D0hvM6jrqe6WzHFuuxqgQjussOfrJWl1JQmTwNQFp2yaz4qLHj1tiiWFPSdGLa788WXGvcnHlpaZc1s+0A0JffR2RI8cs6ds7YAch9UO/aXNYNnwdvbjWZfzc07Wc80Dn7uuF+LHjlrRsrv9sJDw/7VToiCVnzuj3iGXfBJWfseSbzRHR5Vr7Xqxz582M6k8UwvlYnT5Ev5d19QeRc9sbdh0CrUeQ7qY3oss/jogWotTCvoOuir8EtqbpawB2/4HokXXVC61L4920YOixY5asWR+tb9Bf6x81MUR/drUeQbTgn2EvERvvu89ds0Bff//o2OmB6farOvtp26Y9F7KDQ7rpcp0tmkf7qK6au9CwQfygoQYI9Nx9+71ocV89h6+41JSGBVYnSY10aWtn+/G9Qfu70319UD/Fb597bPQ7Q1dS0wLiumnGxlUD/P0gQz8rp89EV27qe7EpJSX6fVadMzLz1+i599rCkBw4FJ1m/ON7WWkrc8X8eIUGqqN3k5bUr5+bz4Rehy55Pywbv4l+/rTujl4HFcI08/wYxeJtRUwwRG/iJ/9hukx6eEzFErHx/lvxclX23Al4rN+wxf6P7nod3mCI/j3Z/vp3d7HaPj27xhRndd7VHfxwgiTueiLUDIlK6Q/stu0R2bhJb1x0RQqt2J6bpQi9n4XDhy154eXKVUn0qeTtI4J1FuHXH6jycste5k6flPa60JDu3QISDkVvAPRH5dx2hn1zqSsHeC+CNIiiN45fbNQnYfrjExDDsGptmoI+BSgtNeyc5OMnRXQlnmLddH60e9lZfRKsVf7TeRqsY6hTTNauj8jXmy3p1sWQ/peY0rJF+oFCfUppmobs2RuRLp1M0fbkYnnPeON78qQleBlqwwAAIABJREFUh4+K6HKGvXua9hPt+YvC9hKVzvYf44J2QVZdxtDZ+vcx5PL+VZ/eatG7t94N2xfhmtlx9RW6fGugSkBEAyGaqv7Rquh76RKKetO4eXtEPt9QubT0g2OC0rRJ9c9M50LyyFFLtn0bkf6XBKrUF0p1dF3O0tSaxZZmDhnSMM+W7tabdl1mctE7ETl2PBpcGHytIZ076hPQ1BfPetP24cqwfPl1pfvIG005v3P8KYZ6w6qrIrVpbcjtw/V7q6qgXlz/zRVQ0DZNeDBoB1tWrokGXXQpWx1zDTx6AyI6TfLZmaHvgw8i/zkhaBeZ1MwVO3vFEHscNPBo1wLQ+3IrmkJe0yf9R4+JPD+78kZ/6KCAdO9qiH5ON34dsb8ve/cwpVnTqt/rGsR5462IfW4720/GBqVRmjfBmn119JglWihTb0jatTHzcpWIXbsjMndB5ffBkGtN6Xa+KZu26A1VtIBun14BadpYa3ik+oRF//7NZksWL4n+xo+7J2ivLKSe4bBhFxTXgIJ+ntO1TO9dc7OXBsW+2RKWdz+oPA/0M3lht9w92ff2RB8caebOpZcEpV07kZJ6uelroRzVrjtj6dQikQ1fh+XyftHfikQBLN1Pr9n0NZaVONClvz36e37qtD4uiWad5mLlF50WqN+L2h79Dsz0AduadRH5YEX0M33tlaZc2rdwppgXyjnqx36kFQzR5XR1ZZN49Sv82GnaXNgCm7dGZOG/Ki+AtLeZ3KxoAEBvkPbsi0ib1tELm2Tp2G5NLcA59/Xokw7drhto2jed6W56kXnmjD6RNCQQjM53jzcVQm8MNDihF19du5j2RbZGx71P+vUi7ZUFYXuFF2e7sJthB0DeW15ppP0dPzZgZ9E4m/7o7ttvybw3KoM70QtAXTY39c1Lun1OtN+RI5Z8uj4im7ZEf8j1Qr9f7+gNfG1seqOjN+H6brr8nV4Y1Ma0FD0H9AJh525L9GK+X5+AXVBNL7bdNz+a0aCBtnQybvTm8/3lYdn6beVFb+tWIrfeGJBGjVJ76o2dBh++2x19vVrcMNiUjueZdZLWrDdxc16LPS8v72fYSxiuXFPZR71AvPfOYMzUBQ0afLImLOu+rNxPL8p+9kCwShFXDfi8vjg26HJue7GnJHy6rvL1OkVCl3Ws7qbn97MvhkTb5mw3DDHl/E76pDb1UfU7a/PWsHy9Ofo9cEFXXe3BTPt7S9/BCVDolAl9spfJzboGjbQPoYglhl5wx1muVi+CdUUtDcY5m47PfXelN31Og9w67cV9A3/V5YYdHNNAh2YPRW9oo9NF9Ebv7FnLzuxINHVl63aRBW9VBhT01TcPDcqmbWH7ptfZdFrW0B+oZ+xnRfuk2Yer1kTksr4B0eDK3r0ROzNp115L9Lu2b2/Tnkqxd58lX222JGiKXNDNkDatzBrdMOt7r/8ybJ/vmmVzy42mlJcbMmNmbH9G3hiQdm1jM8jUctHbYbuNzvaT+zQYmPq7QM+1lavD8sVXla/t0tGQ6wcFai2jIPUnIrqH/i5q0FOXCdcHE3ffEbRrcLz9Xuz1Qbp912M6S6Ke08iwA1xWROTdZSHZvK2yVddeaciF3evOQ69Z7CVdJRrA1nM03soveh68vjhkZ2o5m047uH14er8r6Y5Dqv30N682fltTtcMPf9dg6/xFIdmzr7K1P7haH3KZ0sgTVNbP6sZvwvY1lL5Ofxd0xR1vtqR+f//74+h3np7T+n131RX6EDE2aKvXhGfKo8sBf7UpYgdbNUsy0apCXk8N1GqdvK826bVt9HuwbWsz6feGZnHpvk5gRs9ZDVLr1qGdTnuL/52l++nEh0DAEM3YbtYk9XebH8afNuZGgGBIblw5ah0J6PKH7y4Ly9bv01idZvTrHV3GLtWmr9ciUP9/e2ceLUV17/tfdx8VVERQmQQRBAVExQlFjbNGQRxQiUNiFKNczXtZGZaueO+6Kysr615dcZnc9d67ernGKYnRYJyCYhxQRFBEUVAZHBFQZEbFAb2nu9/6VlHnVFdXd1f36T6nq/uz/1FOV1ft/dm7d+393b9Bk7VeJLvvZjZqRMKxiIhqOqqN49K3s9a7lzlmy1F9irXIWrnKPbHSplPpG4fv5wZm9T9bk/zCxWl73bcZ69/XPf0MbmA2bMzafQ/lbhp1MqlsL7PnpbebNbpUgqbk2gjKJN0zSfTYHX1Ewg4+sLYnR19+bbZkWdrmv9q+4NbzDx+TsINHpfI2eXpJK1Dr5i2J7Z9lHcEmyEOMd9zBNdP/eLvQIAEr2LfalG7e4o6FFSu398VQswOGR7PEKDXOCn2udmz9ImvTH063mb/r2qMOSzjPfnVR2hlbcnM57YSE7TMoWj/oFPee+wPjwMwmn9ti/fqUrq0sLh6dmbuB6LOna5kSRYwp/YTyrtDGW+bv7U6eZudPTFq6NWGPPNHezsMOTthhY1K2sy84pRZXf3uk1bZ8nvvMSWelHCsAf5GI+KfpuZtLmd4ff0zS5m4/ndL1545POuJDpeX9DzP2+FO5fPX7P/O0pPUoIVZprL7+Zu58oHpogawxU2qT4QkwS992x5ZSZo4YnnROvKMscuVqJIsdiRzKICRLAc0PGqP+uU9xlR54NO1YLPiLxBDNlaWKNndr17aLFzKrn3JpizNPLHvXtRySQDjqAHcjGmVcSnjW78J1K3Hre/H5Kbvz3vzfymXfSzlWFsWK353Lu263Xc1JM+4fl/pM6ThH7R/u5lOKhfe5a/knAcwVsPRemPdy7pwpEVmm5H4LMm1+1m3IOu9K9Yd+J4cekrJdukd7she/x3/1VZe5MbOCReOrW7esbdxkzjtNG5NunZgpQxtttXfn7u4hg4J5a0PmL0cemnACVlZSwuZWcZDVSDmCYiXPDvuONpwSyhYvca0A9+ydsOFDzfbb13UB8xdxeWZO2j74sJ3H4EEJO/3EFFnVqtUhHbiPft8av5pLZe08Yv+krd+QsRlPZZw+9oqsEr93ruIVtfevfncrVqbtubm5Y/2gUe6hkieI6BkrVmXsH7Ny3z9yKzx2rGtZ5hW9+zSHa+7wiubb444u/Z6Ri64slOXm6y8nHJuwA2SJ5Js7VCdZs+hASBaYAwe4a69WWcCECO1hc46sinVYuHadEhQkbOQBrittFEvaDnQZX40pgTwxRFYgnutHoTYVcuOIKQOq3UAEZAnx2uJMzqmtmnfq8UkbVSJji5Madl3+pk/fv+SClLOoqGXZ/KnZnwMbLz3vvAkpZxHpLay0Wb7rL/mL9ZO/k7RhQ5M5mx+dBsiv3F+0SdDifMaTuff48ZW5J+MSXXSqtvrj3JeXXizfObq2fpqyfHlwRquzwfEXBZK78JyU7eo7odVGRubwwXqeeYprQu+dKGjToFNlXSsuXhk5PGHHjdPpbXv/6p63/zGXm64/45SkDdrbPemtRZEYJ8Fj8ZJc5tr4XXtli+MCptNuCT2yWnFciCKUMAsHLQpkMRVlwa5xIIEwWPxxCiJUo2qXqO1yVXlpgXviNWJYwk44TubCWceff8nyjBMjYtiQVJ77iuNG8G7GXlzQ3h6dgJ0/URuAXJ7awMvtRgHtvDJULkYHJezlV7O2aYvrejbm4Gib70IAnpmd6/7hXXfZZLldSGjI2PD9XFe24NiTmHfv31od8dZfBvRN2PjTS4t3WiD+39vzx/pZp6esf7/iYq6eKRFFARD9RWPrsotacizVvvoqa28szdiC19qvHdjfDZoYZYGr+2uBv8MOWVv9sdnQwQlH0Hz48dxFvK679IKWSIH19DsXP1lYqMhlQgv+p57LXfBLJDvtxHwR1t9mieCvvJ7OaZ8+1/1OPj5pSqHrt/yJKnaV86MJE0N0GiwxJJgyXJssbTgkEGTSxd069BvTNYmku9H+0/T894/EeAlp/qJN099nph0rhbbfz2DXiirq4UJY+z1LJM3tGk1RYx9JDF/wWtre9FmF6f4TTnPdZyop815O28LF+XNjGI9K7l/udxQX7LY7Wh0rJX+RK+DI/XPnKVnOOH30hCu+i6csifS7r0WKVDdWUzaSW1y57W7E6yUgznoh7ViVeUXCx9jDUvb07Nzf4PcntziWHF7R73TmM2lHUPCXoFCn38STz6Xto8A6T9/xW0yp795bkW9VpeuCzw79zX5jNv3hVvs0cAgxoF/CzjxFFqrt39LYlfuhk2DAV5SRsF/f4lZEmteWv5O2OS/ltltzxI9+0FIT159GHHvN1qbQ1LrNBoH2NhaB4OmcNpJTLy89CWoj+tKr7ulosBx+SMIJllarQE1abCqqun+j4NVByrtOrbyTznnz07bQZxXiXSef9rPPyI2PoI3fs3My9qHPUmbsYQnbZ++k86L0XjZHHZ5w0vv6T4L1Ml25OmNPzc5dVX3vvJTjJlBp0eZDQS+1oemzp+uS1FuZd3wHcxK1nno2Y6sCL2hZwIw/LXdBV2gxqvr5XXq0EVHwOy+4rb/+wZe5gskFX6a6ftgQd2PhxGaw6p9wSuj68wNpxzUrWLRgkFlplKJNqk69dWqpcZFIuBvHZ57POPdOJs10IjNkULSN6OqP8zeduq+siTqyqYnSlkLXaBEnqwcJIMqI4bmyaYPrBL5MWUEXE8VbePd919RfG135+ffsGRITQpuF9VlbuNj9DWljKXeIPfZwT+TT6ay1pBIdPkWVO9r9D+cubmWqvNdeCVu4qP33J3PhiyblBumURZTEUS+QpsdLi+YLzi5t7i5hKOg2oHtI9DnhWDcDR6Hy9XY3PAm5wXLhOUnr3zd3gylXHKUiF/ch+7hzjuKFRBHkgvd3Mqm8kra3lufP13KZUqyYqJtkTxzVXCT3uDVrsvbSwozT9xKVjjoi6biaFPNv1/c0h7/0Sm59JJKceFzSEegl4nlFG8/LJucKux35Pei7mu+DVi3KeKK6+62joj5HIsaG9VlbvNRlIRdFueRIGFFMFa9I/FLwWAXf9Ip+n3Lrc+KkBMpBo5J2zNjyXew0d239Mmuzns+Y4v5I4NEG8LunqK+jzY0bNmXtvgfbf2sae4o3VCjbUClWmgem3ZPbSMW2uvDclpJWWaXuXcnnym70WMDKTPfZaw+zs8/Mnw+07tmpmzmxioYOTjpiV7XjnbhZl7LOu1furxJbjjhU7m2JyL/RqCz0W9bvVEJ1790TTuyeWq3botapkus2bs7aG0tyY1PpPmqPDqQ05+q9oTJAovKJsuZr/w0UOsxyher234v6W5aFQYuN4Bh2RJNZ7a6y/jbJ2uSkEm6iqs8f/pQ/GWjOveTClpz3jCxVlIggWGS1dMIxudYq3jVtWcGyZo8/nS8C6bpzzkw6MaooEAgSQAxhTDQcAWUI0MJPJ5Y9dpX5esJZkJVacMsa4bl5aXt/Rf7ievSIhI07KlWzoIR60cye6/o2B4uEB0fk2G7C/N4HbhDCYBk9MmFHHZ5/Qq22r1mbcfxBlV5QbLSZ16ngJ+tc/1DHjHjn/KGgxfWq1a6vuxYUBx6gjAWuZUIlRe2c+XS+ICF3C52Ueqfe2tBqUTdrTm47jx+XsBH7t5tkanH83AtpJ1huWNHJ+u7bT0uCAUj918v9RqctWkRJrHlubr4lhE7QtcE86vCkvbEk64g4OtE+6TtJSylYRRWKRKDn52Xs3Q/y2/NPV5Re8IuHFlEyZfUXbTy/M84VLiRwKc6MxnvURa82eo8/1Z5FQW3XBkQBRaPEtKgCmqrfQu2XKCThpFi6TS8IcSarPq587BdrgH5nCmi8dLlr6dJ3L3MWbQp6vHFT4GSvu9ml57dnXVDgO1kd+AOL6lkSOEePKu76IMsXmcmv+ii8dl6AyEJ1/+wzs3v+GrLbNXNSzYbFUXECvSaVySq6ZVPY87W4VmYBfxwc7zoJyMdqvq7QgksLa21yNXemtscKihLoTy5Dd9+X+9vTnDHuiJT949ncv6uOR4wJX9hXOthlffPNtwknsKI4a9PUc7fiPvmFnqXf/KqP3PTE/qJ58MARZn37JO25FzKOqHXYIQnr3TuZ837UBvj2P+ZbkOheElRkgeDfpMpFUOLVJ2uztucebsamoJuWBJB7/5Z/T81rP/heS6RgjHoPyJ3gzSVp26N30nQy7WRKKxC4U5+pzXJVCCsSZxSw9rXF7m9XrrXjxiadA4eumBsVGypoWah6S+xRNp3OFq91Uv/GW2mbH7AeU52qnX1Jz/IOPJw4ajsoLkXS5NobJR5Opb+7WnxPoofEA78Vq56jv8s6QvGkFryWMR0QHR0i1oqF1orPvpC7hlLmqIMPzI0bImuNP/qCMes5YiZLIu+QQQcsi99K51ld69rvnpx0MrcVK3pPvfiKGwPOX1QfxUXzApBr7feM5vWV4Wu6YMw6vZ8lNG/5NOOsY3fvabb3gITNeSljEvr8RYdJOlSiQCBIADGEMQGB7QS0AF61Oj/4qj5WPIK9+9dWUV6xMmMznswXOU46LmFDBueewIf5bKuOCspXSvQpt8M9f3rXIDl6DJTgc7S5kBCyek34S27SWS2Ob6hXtNn5ZK3r9yzT3wP2S1i/vrkLe91Tkf21aA8rkyYmbeD2flP/3nZn+MbtmCNdn3lZEal8vCZjDz6W2xdahCh4ZvduScfH1ivaJMnySBu8jhbVUcHBHvXFvdA9JViddHzSepYQoRSzQZYlYUVBDk8/WW5UlQk32ujp5FebFS02FEgtSvDVjjJplu9rsanNu6ymdtox4YhPSiUbVq66TBv99n7UdXIPfG+FG5hOLkKHHSzhsjQ9ueAE/cX1LW1yJfx9+FHWBg9MOHXSRsqfYWDrVrOnZoefwv3wIi1wKxtrpWvtZmdZuSpcGJ50VtIGDqjCDzJKRXzXSICQePXWsowTR0XxUw4cmXR83Z+dm7ZN2wNrK3ixsr/0kjVSDbJnSFjQfFWpGKQmSSz8w5/D50uJA+eckbI990w4QQrlXhZ0qyh0uqt7a4N1sQIbbw8OLJFcVj7+oKwSXCefl3JSwYuRLKAk8gZdJz38sjSRuFStIhFkydsZW7cu6whie+3hxtIJy7AhVjvu5M7de+0pS7zaBAT1rPo+25p13gX6DQRjAoUJcmKiYL7HjFXw82oRinafQoc3+rbEIrm0VUOgEZv7H8p3rfXmstNOKh3XIlqLOueq/2nN2n/dlRvXzXuy4nzJQlabfwl7hVJ/653y3goFRnWzCh4wLGHDh2neyW2DBEIFAl7+XsaJlSbLLR14BeMuBa2qvLv8rx+lnEC9xYrmJK1PdNjjxRyRRctJx7YHxddaU797ZTh68tn8d1/PHmbfm9Q+b6jPpz/a2jav6vkScRUr77wJSVv6tgKDt9+no7G9OqfneUpXEEAM6QrqPLNuCcgqQCelnnqtzfFIuakckcyLJ1DtRmiB+cCjuVHCFRBQEfD9CzAtHHUCqABpiuMgyxcJBQP6JSP73le77lHup8Wlgl4WKjK1PH6cG3jRK18psKHvnRgW/KrQSZju8aPvt5+gf/65TsHdTUqwBE/A5XqhQHty5VHRxkLfP++slL2yKNfcXZ9LxDnr9GhZMUqxkmWTTFffeS9tGza6p7tDBiubTfHFhvi+8FL4qaD3zGuuyM0YVKoufN41BCQ4PfD3cFFLNZo0ocUG7p1bN7kH7rKzm1ZXm3KdUEcpEhr/ny9miJMVptWcLFhaVPqD5Z19hrtw9bKq6PRRQfqenp37m5Jli5v2uXZiiNqmxbBiAPmtQ0bu71pBlQocG4VNJdd4blqaMySQaqOnemrj6sRlSLlZDiQsRrE2qaQO1fhOWDBY/31PPSHpZKYoVNTm2+4Kn+/1zjrjZDdoojZ0T0c4Cda7+b8C8a/8z95/WMKJhRXVNaoYIwVflNta0F1RfXnB2Z2TTS1YP83vDz3mbvxkLaBNozK/6J3kt0yUdaGsJf3ZbXQv57Bkr2Snj7mXF+bHFPK3beoPW6piQbNkedZmzSk8Z0aJ4SILPYm+cgtVbDBt4KMEYq7G7y14D/3+lHLYn33Lu0Yx8AYOTNhugexWYfXQekLrWIkdSo1XLICoM0cVieniib1L38k4lhtOsOxRSSejSxROjsXdtqxjpqTfqeLHJBMJ27Q5Y2s3uAFTZQm9e8+kbd6ctYVv5B5IyV199EjXikR9M3uuAvznXqPfidwRv9xmNv4U1z1RxcmY+P1o1mO16E/uWd8EEEPqu3+oXRcQkF+7Tk90yrrfvgn7/AszKdK1Llrsean65MMpU0YtlndQmsuW3Kc7UcYVG0Gpw5Iy5a7cYqPW7fLur5gLCtRWqCh+iHyay432XcgcW5uiE45pN8XWBk8+y3JH8k4Xxe6Q0TLzzg80qReqXCNeW5x2TEDlfiLzY5lqB4sTjFTZAwL91BG23qZKpuRR7itLmhn/aLV1Gwo/VQHI9t2nI7Xiu51BoNhGUs+XJZIWd9UoigshyWKZssm8k7VBA3QSn3AWm4vfyrdUu+BsuRa0b4IV5yabVarFtK3fYCZ3vb0HJB3XgijjtqNt+PxzuXtlnc2fYrpowR41FXpHn93I3++oGKL3k4Jgb9qST+nU41Mm8UIif1imKv83BvRJ2MQzU861/31Pa15sHO/agw90s1p0NPCnBL57H2h1UuiGFaXoVeYpf+aOzhgHYdag3nN/cnXui0fvDllNyq1Bp+/Dhyad9uh951jZfJN1YqxICK3WPFKIgQQKCRWFyiXnpxy3qI4UCY86CPCnSw/eb9yRbty3sKL5VkLIgzPa46jpOolfCtgu4bIaIls5bdRacOPGjD0yM5Mz5rU2VYyzjo7zcuriv1YHVBJWxFx10Hiq1LpNaywJ2UFXHq3VtPZWjBC5u6jNwbTA6jMFDtd6PVhUN91D8e0WLko7lpLKCCmrkXLXl5Vy4nvxIoAYEq/+orYQiC0BvaD+847CliGKy6LFbLnBziQiaTf32qK0bfrUbNedtRlSKrX8rC/a+GVas85LUQEBlX1HIkIpM125IdwfTFEc6Aml+Sx1n1p2njavspJZ9k7hhefVl7XkpLCrZX24d+UEtJBb+nbGZs/LFyOOOyplo0dVf3H+xVdZRxR55z1lfXGD7xbcDE6U5UUgTec3rsWD332ncgJ8s6sJaPN8RwE3GdXt/IktjttgsSIz/edeaHXS937xhYKdJmz/4Wb7ye1ze4pMic1zA+mA/ffU5uXyS1qstTVrjzwu17HwJyqw4iGjO+4mUyguif+pV/2gpcNBk6P2r95vT8xqtZWrC39j8CCzM08pbJkocUSpTTWfyOpFliWyOh24d9JJnxrm+hO1fqWuW/ZOxp4OBGH3viNxRhlLqiEszZ0fHs/Ce5ay7Y0eGT4+wlKo+9vVVe92xaPRfCpLFcWyU2wNrW9kPVupAFGqvzrz82KudLLwOHxM0g49SOMza9u2yWKkvXYSQe6+r/B6UmL8GSe7AVO13uvKtVlnMuVZlRFADKmMG9+CAATKJCDR4dEnWh3Xj7Byxikpx6+5I0WCgGMpU4MYWcVO5pTRQO5MXb1AeWuZTlnCrW+0qdBJiefi0BHOfLf2BOQq9f6HGccdTqbx2rzIQslNsVub52vjJeutNesKC2py/fjxlSknEwSlcQlIkFu9Jjyrg8zVDx8TzRVJc7I2JhpbEro1P/s33y+/mraXfemWg0RluXDFpW6aZgVVnXZ3/vwma6Rjx+oEv+P9oawaLy4obMGoJ4w/1U1j3xlFWcGU/eazkBNw7/k6Ob/kgtxU1t5nSlP6wYqMPTErX1jVNbLIlLBVq3dXsRN8xc0ZsX+iLVZXR3jqECCYbtZ/P1nzKHNYsEiwU9yJYLBN/3XahF94TkuHYvB0pG2N+F0Jckq77U9bH2ynLAuvvjzXDcy7xokX8ki45Zl3zbVTSmeRbES2tKl8Aogh5TPjGxCAQIUEFMxKp3vBXPOnHJ+0ffdJRvI7rfDRHfqaFvIvzM/YkuXhC8qTj0vZiAPygwh26KEVfFkngIvfTNuC1/M3s0rjufvubGArwNplX9GGVJuZb7ZZ20l0rTYtaqTG+aMlFqjSQH58ZXUCBncZWB4ciYBM4jduzNqbS12f/j16KS17wg4YXr3sHIrh9NBjhcUHZRlTNjXFF1HRzDZnXtpxv9EpuURCBamthnWB7v/RGjc2R7Fy6QUpJ3ZOZ5RSJ+BeHQoFLJZ7519CMvD46654XRKTyrXKjNp+ueXMfCZtGza48U7kdjxubMoJxL3L9ix5Ue9V6DrNXYofJHfcYJELlTI6hYllmmNvLRBY3X+f/31V5emXO9q2Rvy+3IBu/2N46m1/eyWEhqV3V78pi5o/xbf/e5o3lFYct5hGHD3VbxNiSPWZckcIQKAIAb0EFSDyw1UZx1dYUcv77Jmo2UKsWp0h/9bnX8pPDXfc2KQdMDyZl6ZWiz751iqNcWf6G+u5Kz7M2sbNGfvsc7P+fc2JiUKBQCkCcmWbPa+4j78bMwF3q1IsG+lzWXcoI46sgjxRolrtU2yLR2amcwL1+u998fkpJ5NLsMjS0ImpVeVsPOs3uMFTi5UrLk5ZjwrTy5fLLcoJeDHLxFdeT9tLrxS29FJ9nJhXF9XOOkTP8DLhqN922jHrZB+ptnuOgse+/GrWVn3svvvEZeiQpB08snBwebkfyWK1VFHgXKVhplSHgN41EkM0txQrV/+wPXtM8Dq53r26KD9WjLLlnDO+awIdV4cOd+lsAoghnU2c50EAArElIKFBASM3bXLTSeokrXev3PgNmUzW5i3I2JYtZkpFJ6FHmT2+c0znCxJaaHSmEBPbjqXibQQ0xqcVydpx3oQWGxTIZAM+CHSEgILePvVs2j76JHfTfsHElPXq1bnBwXXivGR52p5/MVxAUNawfQbmuvp0pO2lviux6MVXMo51TqGiVKjHHJnMs3xQMFhxDbOWCN5ryiUtdZ2NrhQn73PxkmigjewCAAAaTklEQVQnYUTZrPT/xdxmS2W5031lDaf0sbgGRu2F0tcpVfaMf2SKu8nsYDbl0pST4adQ0ftK8d82bMo48d/kCjWwf7LqImnpFnFFnAkghsS596g7BCBQNwR08iWT5AceLXyqOPmclPXuXf3gl3UDgYrEnoAENAUUlD+2Yj34i+L69O9n1mMXTkhj39F11gBln0kkzUmvKXccxRbxgqx2dlW1qZL7joJySqhRUQDGU09IOeJ3Zwdj1AZ/xpOttmZtPokB/cwmfjc8Pa2bfjRty98tbhmiu8r1rRaxtjq778p9nvr34cda2zLMhX1/rz1kaVB+prty69Js10vE+OsjhddLCoosF7iuypzTbP3RzO1FDGnm3qftEIBA1Qh89ZXZH4pkX/Ae9E+XyzebzWTVwHOjmhDQJuHLr7L2zvsZ23eQe+rca/f8NN81eTg3hUAXE3Di9aSzjjWARALFpOhepfgWlTRN7qXzF2Rs3casbdiYtb32TFifvRI27shk0RTWCsD8fEhWKn8dFMPjovOLn8BXUue4fEfi1x/+VNhV5porautCFBdO1a6nBNA1a7P22FP5gsi4I1N2wH4J261GwcKr3RbuF28CiCHx7j9q30ECOjlJbt+XZrK4FHQQZ9N+fdu3Zg/+vdXJ+lGoyEdW5rbyZz3tpBbbbdf2eCLV9p1u2o6g4RCAAAQalICCKadbzbSJVOwWiTRRrDmKZUITqtNPStrwoclI96o1Wq+NsmVR2yRKdatClqBi9Xbje2Xt4cfStvlTN2i13skKzjtpYotl0laVTEW1ZhfH+6t/N2/JOtmSVnyYcYLq9tjVrF/fJC6+cezQmNYZMSSmHUe1O0ZAE/D8hYrrIF9D14RUQdrkn3z04cpr3rH78+3mIpDNZu0/70ib/I+DRX+TEKITEP2/Av796Acp+8esjCOOfPfklA0akOjSU8fm6i1aCwEIQKB5COjd87e/h7sjHDEmYYccmMoLAN5VdJQeVxl01m/MOpthrcvkWjr2sNpvjuWOpDhg6zfquW7Q12qka+4qljwXAhCIRgAxJBonrmogAls+zdrDj7f7AgebJn/g8yakHJNwCgSiENiwyey+B/PNbBVzQelu5RvrLxeek7Jl72QdNwSVQw9O2NhDw1P/RXk+10AAAhCAAAQKEZAQP+/ltBMPaOuXWevfN2F790/Y4EHJmltelOoVWeh++qnZ/Q8XdlWRRaVSpbIuK0WTzyEAgXIJIIaUS4zrY0+glMmo18CfXI15SOw7u5MaoBOlaffkL+RkEbLqo/zgdVMvb7Hn5qadkyevjD8tZfsOqn66wU5CwGMgAAEIQKDOCSiLh0wSFaC22mmJK226st78d8j7M3g/pQC+/JIWAmpWCprvQQACoQQQQxgYTUNAAdBmPp22VR+XjqwuKPsMTJg2qKQmbZohUnFDW9Nmd93b6liBeEUnces3ZHP+ps+UIeGi81ps1pxcs+UdWsx+eDER6yvuBL4IAQhAAAKxIqDgpYq3teWzaNU+cETCjjtawV6jXc9VEIAABEoRQAwpRYjPG4aAXBZuvaPVCY4Vpejk5NorW5y4DhQIFCMgM9+58zP21rL2waXxpvSMik/jL6NHJm1Av4S9+0H+QLz6hy1dbrJMT0MAAhCAAAQ6g4CsI2+7q7B7TLAOu/Uwu/TClqIZdDqj3jwDAhBoHAKIIY3Tl7SkBIEvvjC78y/RX7q63ZRLWpyTfAoEShEIWoeEucgoSvrkc1L27NxwRW7C6S22376lnsTnEIAABCAAgfgTUDytvz4SHty1UOuuuSJlO+zAKVX8e58WQKA+CCCG1Ec/UItOIPDeirTNfDqai4xXnfGnJWzYkFQn1I5HNAIBWYE8MSttK1a648z7r/5/2JCEnXBs0p6flylonXTReSnrsxeLvEYYC7QBAhCAAASKE1i4KGPzFkQ0191+qwvOlnVlErQQgAAEqkIAMaQqGLlJHAhEDdLlbwtuC3Ho2fqq4zffmn35ZdY2bzGbtyBt/fokrMeuCUtnsvb6G8XFuGunpKylBTGkvnqU2kAAAhCAQC0IbP40a3+eXp5lCMHta9ET3BMCzUsAMaR5+77pWi7f1Lvvyw1yWQxCt53MrrikpW4irjddh8W8wbISWfJ21t77IGOfbzXb+kVxIUS+0Bee02K77BzzhlN9CEAAAhCAQAQCek/eemd09+U9e5tNmkhsrQhouQQCEIhIoCHEkPdXrrGbb73fbvznq6xXzx5tTf9627f2q5vvtMdnzXf+9pvrp9ik8ce3ff7KouV2+U9vcv590MihdttNP8v5/kMz59i//vZO5/MJpxxtv75uinXv5oaw3vLZVrvml7+3N5d94Pz77v/4pR05ZkRB7KWuL1YXfz38bdA9b/j32+26ay+y/QYPiNjlzXuZYjq8tTRjc16KZpJ5/LikjR6VJI1b8w6ZDrc8nc7aH/6UNlmLlCoS3hRThAIBCEAAAhBoBgIKPv7aoowteD3auuzc8S22z8BmIEMbIQCBziIQazHELzCEiRm/mzbd4fjzqZPbxItfTJ3siBYSUP7lxtvt3264yhESJDjMX7i0TfCQOHHLtOltAon/Xp7IcvThoxxxJXivYOeVur5YXbZ9843d+H/utRt+cqlzW+//Jfqozip+gaezBk5cnyPrkBlPpp0sH8XKwL0TNuHUlO20U1xbSr3rhcDGzVl7+LF0Xopdf/3OnZCy/n0TRMivl06jHhCAAAQg0CkE/qfVbPrDrbZpS/HHjRmdsKOOIK1up3QKD4FAExGItRji9VOYZUiY1YRf0JCQ8OHqtY5QohIUJHTtvoP6tQkNfnFk86dbcyxRgmJHcPwE6xe8vlhddK97H3rGrrvmIue2N992v1066VTrvXuPHGGkicZsh5v69TazV1/P2Otvhp9EHHpQ0o4Yk7Tu3Tv8KG4AAYeAMsvMnpexDRsztmGTmdLu9upp1nO3hJ15asoSScMCibECAQhAAAJNSUAHVS8uyNjiJeHrMlnqDhuSJLtfU44OGg2B2hJoWDEkzFrDb/1x2z2POGQ9McSzMpHlyOgRQx33Gs/yIyiWbN7yeY7ViD73Cy3BLgtamQSvD37XX5dhQ/YOtQx5bt7rzmOwCqnsByLTzPUbsrb1C7NP1rkv3/59k46bgrJ57LhDZfflWxAoRMBxlclmbccdzRTMN5VMmNxouncnYCqjBgIQgAAEmpuA3oubt2Ttq6/NVq3O2E7dzAYNSFm3bma9e3Fg0Nyjg9ZDoHYEGloMCcYRCYohfsuPMDHkwokntsUB8YsrEkMemDE7J4ZIKTGk2PVBKxR/XeTSE4wZctKxh7YJJHfd/4Tdcd9MZ4T445Z8+eWXtRs1DXLnRCJhyWTSsll3M5pIZC2TyVhWx/YUCEAAAhCIFQHN55rDKRCAQDwJeOuyTDZpqWTWWY+xLotnX1LrziOwyy67dN7DGvBJdSmGSHiYev0t9sm6TXnIw2KDhLnJNIplSFhQVi9WyCEHDmtzoVmzbmOO686KFSsacLjSJAhAAAIQgEA4gR133NG+/TZCtGIAQgACEIAABBqEwJAhQxqkJV3TjLoUQ8pF0cgxQ4JZYmQ14gVRfW/Fx20WKv5Aq/6MOuWy5HoIQAACEIAABCAAAQhAAAIQgECjE2hYMUQd11XZZDw3l8kTT3RienQkm4yXytcbiP4MMhKBvOCqQcuQRh+4tA8CEIAABCAAAQhAAAIQgAAEIFApgViLIf7Uuh6AKy8e3xYU1RMhHp813/n4N9dPyQk4qsCml//0JuezMPcbf6yOCaccnRMjJPhsf7yOoBii+xe7Xp+Xqouu8Ysfnkjir6O/DpUOCL4HAQhAAAIQgAAEIAABCEAAAhBodAKxFkMavXNoHwQgAAEIQAACEIAABCAAAQhAAALVJ4AYUn2m3BECEIAABCAAAQhAAAIQgAAEIACBOiaAGFLHnUPVIAABCEAAAhCAAAQgAAEIQAACEKg+AcSQ6jPljhCAAAQgAAEIQAACEIAABCAAAQjUMQHEkDruHKoGAQhAAAIQgAAEIAABCEAAAhCAQPUJIIZUnyl3hAAEIAABCEAAAhCAAAQgAAEIQKCOCSCG1HHnUDUIQAACEIAABCAAAQhAAAIQgAAEqk8AMaT6TLkjBCAAAQhAAAIQgAAEIAABCEAAAnVMADGkjjuHqkEAAhCAAAQgAAEIQAACEIAABCBQfQKIIdVnGqs7vrJouV3+05va6jzhlKPt19dNse7ddnT+9vW2b+1XN99pj8+a7/z7N9dPsUnjj89p45bPttoN/367XXftRbbf4AE5nz00c47962/vdP4WvHesQDVQZX83bbrdcd/MthYF+1T9ec0vf29vLvvAuebu//ilHTlmRA6B91eusZtvvd9u/OerrFfPHm2flbp3A2GMVVNK9Yt/Hjho5FC77aaf5fSrGluozz0Q3lyhf/vnkFiBapDKqq+mXn+LfbJuk9OisD6NMjdr3Ow7qF/enK97+sfUlRePt59Pndwg9OLZjFJ9HuVd7vVrWJ/7+7vQHBFPcvGtdan1W7F3ebXGS3zpxbPmpd7lxfq81Hgpde94EqPWEChNADGkNKOGvkIL4kED+jibXW+x1K9P77aFrSZHFS10vUn2F1Mn51wvoaR/3z1s2m9/kSOGaOK9Zdr0to2V/14NDbWOG6c+vu2eR+yKi850NrvegujGG67K6dOjDx/lbID0+b/ceLv92w1XOX3rf9EGF8Sl7l3HWBq6aqX6JdjHmhPmL1zaJmgU6/OgEKK5ANGz64eT5t7Va9a3iRiae9eu39zWp6XmZr9QEiaAM5d3fR8Ha1Cqz4u9y3WvYn0enBOC/64/Gs1Ro2LrN289V+hd3tHx0hyE66uVpd7lpfq81HgptjasLxLUBgLVJYAYUl2esb+bf5Gz7Ztv8iw+whbBhSxDgqeKwQV47GE1QAPCXp5+i4/g516TS1kJ6LpC320AbLFuQrBf9Jv/cPXaNgE0KI5E6XPvt65r/UJKrEE1UOXDxA//6X+huTnMMkTXPjBjNtY/dT4+/H2qqgatNwsJWmF9HryWd3l9dr5//bZm3cYc681S7+NKx0t9kmiOWlW6fvPoFBM1S42X5iBMK5uFAGJIs/R0xHb6Fz1hm6KwyTNMDAmbSAttsiJWjctqQCBo7RO2yA1bNEcRQ4L3rkH1uWUFBIL9EuzfQv1WzDVK1ZD1GCfGFXRIJ3zF3y96nFwfvRNj/bvQ3By2MfZbEHhVD3Ol64Rm8YgiBIIbY7+Fn75W6Lca1ueeBeH4k49yfufF3KfolK4j4J/Lo77LwzbGElKijpeuay1PrnT95pErZuHH+o3x1UwEEEOaqbdLtDX48gzb/JQrhlw48cS2eBOIIfU32MJO/IKnvpWKIZjS119/q0bBfglubMoRQ4JWJYgh9dfnwXnXE6qjzM2FrASCViU33Hh7nptk/ZFonhoF+zzqu9ybH4IxQ7wx89nWL23ugjdDY9A0D936bGlw/RZmwVXondyR8VKfNJqjVpWu30SnlHUX67fmGEO00iWAGMJIcAhoYgwuaLEMaezBEYwjUOgFWYkYEnbvxqYZj9aF9UtHLEP0XX8wXo8CcUPqYzwEYwKpVuVY7UURQzCnro++9moR1udR3+WFxJDgOJDoOX3G7NBAy/VFozlqE7Z+i2oZ0tHx0hyE66+VHVm/hY0XfwtZv9Vff1Oj2hJADKkt31jcvdDEGOb+ErYxJmZILLo5p5KFXnbBE8RKYobwIq3P8VCoX6oRM8RrMZYh9dP3YZscr3bBzW05MUOC4yXM0qR+KDRXTQr1edR3eZgYUo4lUXPRro/WFlq/RXmXV2O81AeF5qpFR9ZvCCHNNVZobTQCiCHRODXsVeWYyhUyny8khpTKWNCwUOu8YcXMH0tFI/efPhZKratrSLNZX4OgWJ+XyiZTqs/9LUUMqY9+L+WSGHVuLhY/wstAVeodUh9EGr8WpfrcPwcUiwdQyBrIn40Iy5D6GE/Ffnul3uXVGi/1QaJ5atGR9VupuRrXmOYZR7Q0lwBiSJOPiDAzd3+aXO+FqpSZKv40i8HP9HnQPN4fbA/T+a4fbMEc9F6N/H1TLE992PevvHh8TurlN5d9kNNQ+r1r+z1Kn2uRdPlPb3IqGkyZXKzPgy1DDOnavvaeHhbkVJ/5A50Wm5uD3w+mTvePl7C06vVBoblqUarPi73LRapYnwe/G5wjmot0/bS21Pqt2Lu8o+Olfig0T02ivMuL9Xmx8dJ79x52zS9/b6zfmmc80dJ2AoghjAYIQAACEIAABCAAAQhAAAIQgAAEmooAYkhTdTeNhQAEIAABCEAAAhCAAAQgAAEIQAAxhDEAAQhAAAIQgAAEIAABCEAAAhCAQFMRQAxpqu6msRCAAAQgAAEIQAACEIAABCAAAQgghjAGIAABCEAAAhCAAAQgAAEIQAACEGgqAoghTdXdNBYCEIAABCAAAQhAAAIQgAAEIAABxBDGAAQgAAEIQAACEIAABCAAAQhAAAJNRQAxpKm6m8ZCAAIQgAAEIAABCEAAAhCAAAQggBjCGIAABCAAAQhAAAIQgAAEIAABCECgqQgghjRVd9NYCEAAAhCAAAQgAAEIQAACEIAABBBDGAMQgAAEIAABCEAAAhCAAAQgAAEINBUBxJCm6m4aCwEIQAACEIAABCAAAQhAAAIQgABiCGMAAhCAAAQgAAEIQAACEIAABCAAgaYigBjSVN1NYyEAAQhAAAIQgAAEIAABCEAAAhBADGEMQAACEIAABCAAAQhAAAIQgAAEINBUBBBDmqq7aSwEIAABCEAAAhCAAAQgAAEIQAACiCGMAQhAAAIQgAAEIAABCEAAAhCAAASaigBiSFN1N42FAAQgAAEIQAACEIAABCAAAQhAADGEMQABCEAAAhCAAAQgAAEIQAACEIBAUxFADGmq7qaxEIAABCAAgcYgsOWzrXbNL39v+wzoY7++bop177aj07DfTZtuCxYtt9tu+pn16tmjMRpLKyAAAQhAAAIQqDoBxJCqI+WGEIAABCAAAQh0BgFPEJk88USbNP54e2XRcrtl2nSEkM6AzzMgAAEIQAACMSeAGBLzDqT6EIAABCAAgWYmIAHkhhtvtxtvuMoRQn4xdbIdOWZEMyOh7RCAAAQgAAEIRCCAGBIBEpdAAAIQgAAEIFC/BOQac8d9M+03109xLEQoEIAABCAAAQhAoBQBxJBShPgcAhCAAAQgAIG6JuCJIVdePN5+PnVyXdeVykEAAhCAAAQgUB8EEEPqox+oBQQgAAEIQAACFRDw4oTIPcZzl8FNpgKQfAUCEIAABCDQZAQQQ5qsw2kuBCAAAQhAoFEIvL9yjU29/hYnXogEkIdmzrFb73nUpv32F7bf4AGN0kzaAQEIQAACEIBADQgghtQAKreEAAQgAAEIQKC2BLxMMmPHjGhzjfl627f2q5vvtFVr1pNRprb4uTsEIAABCEAg9gQQQ2LfhTQAAhCAAAQgAAEIQAACEIAABCAAgXIIIIaUQ4trIQABCEAAAhCAAAQgAAEIQAACEIg9AcSQ2HchDYAABCAAAQhAAAIQgAAEIAABCECgHAKIIeXQ4loIQAACEIAABCAAAQhAAAIQgAAEYk8AMST2XUgDIAABCEAAAhCAAAQgAAEIQAACECiHAGJIObS4FgIQgAAEIAABCEAAAhCAAAQgAIHYE0AMiX0X0gAIQAACEIAABCAAAQhAAAIQgAAEyiGAGFIOLa6FAAQgAAEIQAACEIAABCAAAQhAIPYEEENi34U0AAIQgAAEIAABCEAAAhCAAAQgAIFyCCCGlEOLayEAAQhAAAIQgAAEIAABCEAAAhCIPQHEkNh3IQ2AAAQgAAEIQAACEIAABCAAAQhAoBwCiCHl0OJaCEAAAhCAAAQgAAEIQAACEIAABGJPADEk9l1IAyAAAQhAAAIQgAAEIAABCEAAAhAohwBiSDm0uBYCEIAABCAAAQhAAAIQgAAEIACB2BNADIl9F9IACEAAAhCAAAQgAAEIQAACEIAABMohgBhSDi2uhQAEIAABCEAAAhCAAAQgAAEIQCD2BBBDYt+FNAACEIAABCAAAQhAAAIQgAAEIACBcggghpRDi2shAAEIQAACEIAABCAAAQhAAAIQiD0BxJDYdyENgAAEIAABCEAAAhCAAAQgAAEIQKAcAogh5dDiWghAAAIQgAAEIAABCEAAAhCAAARiTwAxJPZdSAMgAAEIQAACEIAABCAAAQhAAAIQKIcAYkg5tLgWAhCAAAQgAAEIQAACEIAABCAAgdgTQAyJfRfSAAhAAAIQgAAEIAABCEAAAhCAAATKIYAYUg4troUABCAAAQhAAAIQgAAEIAABCEAg9gQQQ2LfhTQAAhCAAAQgAAEIQAACEIAABCAAgXIIIIaUQ4trIQABCEAAAhCAAAQgAAEIQAACEIg9AcSQ2HchDYAABCAAAQhAAAIQgAAEIAABCECgHAKIIeXQ4loIQAACEIAABCAAAQhAAAIQgAAEYk8AMST2XUgDIAABCEAAAhCAAAQgAAEIQAACECiHAGJIObS4FgIQgAAEIAABCEAAAhCAAAQgAIHYE0AMiX0X0gAIQAACEIAABCAAAQhAAAIQgAAEyiGAGFIOLa6FAAQgAAEIQAACEIAABCAAAQhAIPYEEENi34U0AAIQgAAEIAABCEAAAhCAAAQgAIFyCCCGlEOLayEAAQhAAAIQgAAEIAABCEAAAhCIPQHEkNh3IQ2AAAQgAAEIQAACEIAABCAAAQhAoBwCiCHl0OJaCEAAAhCAAAQgAAEIQAACEIAABGJPADEk9l1IAyAAAQhAAAIQgAAEIAABCEAAAhAohwBiSDm0uBYCEIAABCAAAQhAAAIQgAAEIACB2BNADIl9F9IACEAAAhCAAAQgAAEIQAACEIAABMohgBhSDi2uhQAEIAABCEAAAhCAAAQgAAEIQCD2BP4/t3k0AQX+AD0AAAAASUVORK5CYII=",
      "text/html": [
       "<div>                            <div id=\"6d9fb892-121d-4a26-95f8-8aaaa7103cf6\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"6d9fb892-121d-4a26-95f8-8aaaa7103cf6\")) {                    Plotly.newPlot(                        \"6d9fb892-121d-4a26-95f8-8aaaa7103cf6\",                        [{\"hovertemplate\":\"x=%{x}<br>y=%{y}<br>size=%{marker.size}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"size\":[0.0,76.52,24.46,35.96,7.95,25.17,43.45,20.78,15.31,3.22,22.39,14.15,19.42,37.75,20.08,26.74,18.2,26.23,2.13,17.25,16.04,20.31,8.54,38.75,44.89,36.01,69.32,34.63,6.75,108.29,76.77,6.27,32.34,6.59,39.88,10.31,12.5,13.91,49.12,23.87,48.75,41.85,1.81,48.69,7.82,31.46,18.34,7.35,39.87,36.65,16.63,9.17,115.28,31.53,41.46,37.86,23.83,27.1,22.35,17.86,31.84,15.34,11.27,34.52,17.18,8.97,19.88,35.85,2.02,20.87,20.07,7.91,11.67,15.77,12.6,12.38,6.83,23.32,11.82,18.91,64.29,15.1,31.16,24.19,30.15,40.73,24.47,31.14,28.5,20.46,41.94,29.68,18.22,36.13,11.01,24.3,13.23,15.55,41.03,15.24,41.23,12.73,13.6,5.96,14.25,9.39,22.55,0.89,35.56,18.6,7.45,56.04,16.19,33.76,51.43,11.47,21.96,84.92,75.38,63.63,49.24,35.68,23.71,9.43,25.84,88.95,26.47,32.93,19.72,30.84,33.44,2.59,4.65,10.42,17.5,22.33,16.19,16.81,51.02,22.46,88.26,23.61,1.5,8.93,10.01,3.01,29.81,23.25,76.88,175.6,16.67,329.41],\"sizemode\":\"area\",\"sizeref\":0.8235250000000001,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[\"2023-02-15T00:00:00\",\"2023-01-31T00:00:00\",\"2022-12-30T00:00:00\",\"2022-11-30T00:00:00\",\"2022-10-31T00:00:00\",\"2022-09-30T00:00:00\",\"2022-08-31T00:00:00\",\"2022-07-29T00:00:00\",\"2022-06-30T00:00:00\",\"2022-05-31T00:00:00\",\"2022-04-29T00:00:00\",\"2022-03-31T00:00:00\",\"2022-02-28T00:00:00\",\"2022-01-31T00:00:00\",\"2021-12-31T00:00:00\",\"2021-11-30T00:00:00\",\"2021-10-29T00:00:00\",\"2021-09-30T00:00:00\",\"2021-08-31T00:00:00\",\"2021-07-30T00:00:00\",\"2021-06-30T00:00:00\",\"2021-05-28T00:00:00\",\"2021-04-30T00:00:00\",\"2021-03-31T00:00:00\",\"2021-02-26T00:00:00\",\"2021-01-29T00:00:00\",\"2020-12-31T00:00:00\",\"2020-11-30T00:00:00\",\"2020-10-30T00:00:00\",\"2020-09-30T00:00:00\",\"2020-08-31T00:00:00\",\"2020-07-31T00:00:00\",\"2020-06-30T00:00:00\",\"2020-05-29T00:00:00\",\"2020-04-30T00:00:00\",\"2020-03-31T00:00:00\",\"2020-02-28T00:00:00\",\"2020-01-31T00:00:00\",\"2019-12-31T00:00:00\",\"2019-11-29T00:00:00\",\"2019-10-31T00:00:00\",\"2019-09-30T00:00:00\",\"2019-08-30T00:00:00\",\"2019-07-31T00:00:00\",\"2019-06-28T00:00:00\",\"2019-05-31T00:00:00\",\"2019-04-30T00:00:00\",\"2019-03-29T00:00:00\",\"2019-02-28T00:00:00\",\"2019-01-31T00:00:00\",\"2018-12-31T00:00:00\",\"2018-11-30T00:00:00\",\"2018-10-31T00:00:00\",\"2018-09-28T00:00:00\",\"2018-08-31T00:00:00\",\"2018-07-31T00:00:00\",\"2018-06-29T00:00:00\",\"2018-05-31T00:00:00\",\"2018-04-30T00:00:00\",\"2018-03-29T00:00:00\",\"2018-02-28T00:00:00\",\"2018-01-31T00:00:00\",\"2017-12-29T00:00:00\",\"2017-11-30T00:00:00\",\"2017-10-31T00:00:00\",\"2017-09-29T00:00:00\",\"2017-08-31T00:00:00\",\"2017-07-31T00:00:00\",\"2017-06-30T00:00:00\",\"2017-05-31T00:00:00\",\"2017-04-28T00:00:00\",\"2017-03-31T00:00:00\",\"2017-02-28T00:00:00\",\"2017-01-31T00:00:00\",\"2016-12-30T00:00:00\",\"2016-11-30T00:00:00\",\"2016-10-31T00:00:00\",\"2016-09-30T00:00:00\",\"2016-08-31T00:00:00\",\"2016-07-29T00:00:00\",\"2016-06-30T00:00:00\",\"2016-05-31T00:00:00\",\"2016-04-29T00:00:00\",\"2016-03-31T00:00:00\",\"2016-02-29T00:00:00\",\"2016-01-29T00:00:00\",\"2015-12-31T00:00:00\",\"2015-11-30T00:00:00\",\"2015-10-30T00:00:00\",\"2015-09-30T00:00:00\",\"2015-08-31T00:00:00\",\"2015-07-31T00:00:00\",\"2015-06-30T00:00:00\",\"2015-05-29T00:00:00\",\"2015-04-30T00:00:00\",\"2015-03-31T00:00:00\",\"2015-02-27T00:00:00\",\"2015-01-30T00:00:00\",\"2014-12-31T00:00:00\",\"2014-11-28T00:00:00\",\"2014-10-31T00:00:00\",\"2014-09-30T00:00:00\",\"2014-08-29T00:00:00\",\"2014-07-31T00:00:00\",\"2014-06-30T00:00:00\",\"2014-05-30T00:00:00\",\"2014-04-30T00:00:00\",\"2014-03-31T00:00:00\",\"2014-02-28T00:00:00\",\"2014-01-31T00:00:00\",\"2013-12-31T00:00:00\",\"2013-11-29T00:00:00\",\"2013-10-31T00:00:00\",\"2013-09-30T00:00:00\",\"2013-08-30T00:00:00\",\"2013-07-31T00:00:00\",\"2013-06-28T00:00:00\",\"2013-05-31T00:00:00\",\"2013-04-30T00:00:00\",\"2013-03-28T00:00:00\",\"2013-02-28T00:00:00\",\"2013-01-31T00:00:00\",\"2012-12-31T00:00:00\",\"2012-11-30T00:00:00\",\"2012-10-31T00:00:00\",\"2012-09-28T00:00:00\",\"2012-08-31T00:00:00\",\"2012-07-31T00:00:00\",\"2012-06-29T00:00:00\",\"2012-05-31T00:00:00\",\"2012-04-30T00:00:00\",\"2012-03-30T00:00:00\",\"2012-02-29T00:00:00\",\"2012-01-31T00:00:00\",\"2011-12-30T00:00:00\",\"2011-11-30T00:00:00\",\"2011-10-31T00:00:00\",\"2011-09-30T00:00:00\",\"2011-08-31T00:00:00\",\"2011-07-29T00:00:00\",\"2011-06-30T00:00:00\",\"2011-05-31T00:00:00\",\"2011-04-29T00:00:00\",\"2011-03-31T00:00:00\",\"2011-02-28T00:00:00\",\"2011-01-31T00:00:00\",\"2010-12-31T00:00:00\",\"2010-11-30T00:00:00\",\"2010-10-29T00:00:00\",\"2010-09-30T00:00:00\",\"2010-08-31T00:00:00\",\"2010-07-30T00:00:00\"],\"xaxis\":\"x\",\"y\":[0.0,76.52,-24.46,-35.96,-7.95,-25.17,-43.45,-20.78,15.31,-3.22,-22.39,14.15,-19.42,37.75,-20.08,26.74,-18.2,-26.23,-2.13,17.25,16.04,20.31,8.54,38.75,-44.89,36.01,69.32,-34.63,6.75,108.29,-76.77,-6.27,-32.34,6.59,39.88,10.31,12.5,-13.91,-49.12,-23.87,48.75,-41.85,-1.81,48.69,7.82,31.46,-18.34,-7.35,-39.87,36.65,-16.63,-9.17,115.28,-31.53,41.46,-37.86,23.83,-27.1,22.35,-17.86,-31.84,15.34,-11.27,34.52,-17.18,-8.97,19.88,35.85,2.02,-20.87,-20.07,-7.91,11.67,-15.77,-12.6,12.38,-6.83,-23.32,-11.82,18.91,64.29,-15.1,31.16,-24.19,30.15,-40.73,-24.47,31.14,28.5,-20.46,41.94,-29.68,-18.22,36.13,11.01,24.3,-13.23,-15.55,41.03,-15.24,41.23,-12.73,-13.6,-5.96,14.25,9.39,22.55,0.89,35.56,-18.6,7.45,56.04,-16.19,-33.76,51.43,-11.47,-21.96,84.92,-75.38,-63.63,49.24,-35.68,-23.71,9.43,-25.84,88.95,-26.47,32.93,-19.72,30.84,-33.44,-2.59,4.65,10.42,-17.5,22.33,-16.19,-16.81,51.02,-22.46,88.26,-23.61,-1.5,8.93,-10.01,-3.01,29.81,-23.25,-76.88,175.6,-16.67,329.41],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"x\"},\"showgrid\":false,\"gridcolor\":\"lightgray\"},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Percent Change\"},\"tickformat\":\".2%\",\"gridcolor\":\"lightgray\"},\"legend\":{\"tracegroupgap\":0,\"itemsizing\":\"constant\"},\"title\":{\"text\":\"Trade over time\"},\"plot_bgcolor\":\"rgb(255, 255, 255)\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('6d9fb892-121d-4a26-95f8-8aaaa7103cf6');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "stockViz(data_for_visualization)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6e2613a8-453f-4da5-a6af-0ff971dc3dc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dateString = data_for_visualization[0]\n",
    "date = data_for_visualization[1]\n",
    "stock_Price = data_for_visualization[2]\n",
    "stock_Volume = data_for_visualization[3]\n",
    "stock_Price_Change = data_for_visualization[4]\n",
    "stock_Volume_Change = data_for_visualization[5]\n",
    "\n",
    "stock_Price_Change_abs = [abs(change) for change in stock_Price_Change]\n",
    "stock_Volume_Change_abs = [abs(change) for change in stock_Volume_Change]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "76d41140-3360-43c2-b074-740c46a9d55d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# priceTracker = px.line(x = date, y = stock_Price, title = \"Stock Price over time\" )\n",
    "\n",
    "\n",
    "# priceTracker.update_layout(\n",
    "#     title='Stock Price',\n",
    "#     yaxis_tickformat='$',\n",
    "#     yaxis_title='Price',\n",
    "#     xaxis_showgrid=False,   # Set the x-axis grid lines to show\n",
    "#     # yaxis_showgrid=False,   # Set the y-axis grid lines to show\n",
    "#     xaxis_gridcolor='lightgray',  # Set the x-axis grid color\n",
    "#     yaxis_gridcolor='lightgray',  # Set the y-axis grid color\n",
    "#     plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white\n",
    "# )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ec361aae-986e-4d1b-881d-e2e380d0c3b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# changeTracker = px.scatter( x = date, y = stock_Volume_Change, title = 'Trade over time', size = stock_Volume_Change_abs)\n",
    "\n",
    "# changeTracker.update_layout(\n",
    "#     yaxis_tickformat = '.2%',\n",
    "#     yaxis_title = 'Percent Change',\n",
    "#     xaxis_showgrid=False,   # Set the x-axis grid lines to show\n",
    "#     # yaxis_showgrid=False,   # Set the y-axis grid lines to show\n",
    "#     xaxis_gridcolor='lightgray',  # Set the x-axis grid color\n",
    "#     yaxis_gridcolor='lightgray',  # Set the y-axis grid color\n",
    "#     plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white\n",
    "# )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
