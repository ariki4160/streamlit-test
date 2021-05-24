import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# タイトルの表示
st.title('Streamlitで作成したサンプルアプリ')

# 文書の表示
# st.write("Good morning")

# DataFrame の表示
st.markdown('## DataFrame での表示')
st.markdown('- 各列でのソートが可能')
st.dataframe(pd.DataFrame({
    'date': ["2020/3/22","2020/3/23","2020/3/24","2020/3/25","2020/3/26","2020/3/27","2020/3/28"],
    'day of week': ["日","月","火","水","木","金","土"],
    'Number of infected people': ["1","0","0","0","0","1","1"]
}))


# table の表示
st.markdown('## table での表示')
st.markdown('- 各列でのソートは出来ない')
st.table(pd.DataFrame({
    'date': ["2020/3/22","2020/3/23","2020/3/24","2020/3/25","2020/3/26","2020/3/27","2020/3/28"],
    'day of week': ["日","月","火","水","木","金","土"],
    'Number of infected people': ["1","0","0","0","0","1","1"]
}))

# DataFrame の表示
st.markdown('## DataFrame での20列、50行の数値のランダム生成表示')
st.markdown('- 読み込むごとに数値をランダムに生成')
st.markdown('- 各列でのソートが可能')
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)


# Markdown の表示
# st.markdown('# Markdown documents')

# Plotly の表示
st.markdown('## Plotly を使ったグラフ表示')
import plotly.graph_objs as go

animals = ['鳥取県', '島根県', '岡山県', '広島県', '山口県']
populations = [4, 9, 83, 160, 55]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "都道府県",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "感染者数",
        title_standoff = 25),
    title ='2021/05/24　中国5県の感染者数')

st.plotly_chart(fig, use_container_width=True)

# Altair の表示
st.markdown('## Altair を使ったグラフ表示')
import altair as alt
from vega_datasets import data

source = data.cars()

fig = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).properties(
    width=500,
    height=500
).interactive()

st.write(fig)


# Altair の表示
st.markdown('## Altair を使ったインタラクティブなグラフ表示')
cars = data.cars()

brush = alt.selection_interval()

points = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(cars).mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

points & bars



# ボタンの表示
# answer = st.button('Say hello')
#
# if answer == True:
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

# チェックボタンの表示
# agree = st.checkbox('I agree')
#
# if agree == True :
#      st.write('Great!')

# ラジオボタンの表示
st.markdown('## ラジオボタンでの選択表示')
genre = st.radio(
     "中国5県より県名を選択ください。",
     ('鳥取県', '島根県', '岡山県', '広島県', '山口県'))

if genre == '岡山県':
     st.write('岡山県が選択されました。')
else:
     st.write("岡山県以外が選択されました。")

# ドロップダウンの表示
st.markdown('## ドロップダウンでの選択表示')
option = st.selectbox(
    '中国5県より県名を選択ください。',
     ('鳥取県', '島根県', '岡山県', '広島県', '山口県'))
st.write('あなたが選択した県：', option)

# ドロップダウンから2つ以上同時に選択
st.markdown('## ドロップダウンから2つ以上同時に選択')
options = st.multiselect(
    '中国5県より県名を選択ください。',
    ['鳥取県', '島根県', '岡山県', '広島県', '山口県'],
    ['岡山県', '広島県'])

st.table(options)

# スライダーの表示
st.markdown('## スライダーでの選択')
age = st.slider('あなたの年齢は?',  min_value=0, max_value=120, step=1, value=25)
st.write("私は", age, '歳です。')

# 最小値0.0、最大値100.0、初期値(25.0,75.0)で動くスライダー
st.markdown('## 範囲スライダーでの選択')
values = st.slider(
    '範囲を選択してください。',
   0.0, 100.0, (25.0, 75.0))
st.write('選択した範囲は', values, 'です。')
