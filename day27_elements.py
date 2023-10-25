import streamlit as st
from pathlib import Path
import json
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# sidebar
with st.sidebar:
    st.title(':calendar: #30DaysOfStreamlit')
    st.header('Day 27 - Streamlit Elements')
    st.write('Build a draggable and resizable dashboard with Streamlit Elements.')
    st.write('---')
    media_url = st.text_input('Media URL', 'https://www.youtube.com/watch?v=vIQQR_yq-8I')

if 'data' not in st.session_state:
    st.session_state.data = Path('data.json').read_text()

layout = [
    #エディター項目は座標x=0、y=0に配置され、6/12列を取り、高さは3です。
    dashboard.Item("editor", 0, 0, 6, 3),
    #グラフ項目は座標x=6、y=0に配置され、6/12の列を取り、高さは3です。
    dashboard.Item("chart", 6, 0, 6, 3),
    #メディア項目は座標x=0、y=3に配置され、6/12列を取り、高さは4です。
    dashboard.Item("media", 0, 2, 12, 4),
]

#要素を表示するフレームを作成。
with elements("demo"):

    # レイアウトに沿ってダッシュボードを作成
    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # 1番目：コードエディター
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # header
            mui.CardHeader(title="Editor", className="draggable")
            
            # カードコンテンツを作成
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())
        
        # 2番目：Nivoバンプチャート
        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Chart", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # 3番目：メディアプレイヤー
        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url, width="100%", height="100%", controls=True)

        


