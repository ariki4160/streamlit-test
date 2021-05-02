import streamlit as st

# タイトルの表示
st.title('My app')

# 文書の表示
st.write("Good morning")

# DataFrame の表示
import pandas as pd
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Markdown の表示
st.markdown('# Markdown documents')

# Plotly の表示
import plotly.graph_objs as go

animals = ['giraffes', 'orangutans', 'monkeys']
populations = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

st.plotly_chart(fig, use_container_width=True)

# Altair の表示
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

# ボタンの表示
answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')

# チェックボタンの表示
agree = st.checkbox('I agree')

if agree == True :
     st.write('Great!')

# ラジオボタンの表示
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

# ドロップダウンの表示
option = st.selectbox(
    'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

# ドロップダウンから2つ以上同時に選択
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.table(options)

# スライダーの表示
age = st.slider('How old are you?',  min_value=0, max_value=130, step=1, value=25)
st.write("I'm ", age, 'years old')

# 最小値0.0、最大値100.0、初期値(25.0,75.0)で動くスライダー
values = st.slider(
    'Select a range of values',
   0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
