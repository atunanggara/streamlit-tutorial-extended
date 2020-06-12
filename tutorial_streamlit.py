import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time


st.title('Streamlit Tutorial')

st.write('')
st.write('I am following along the \
    [documentation](https://docs.streamlit.io/en/latest/getting_started.html), \
    but will modify in several areas to explore the streamlit functionality.')

st.header('Interactive DataFrame')

st.write('Using random data, I am creating an interactive dataframe `df` \
          with highlights on the highest value on each row.')
with st.echo():
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 40, 30]
        })
    st.dataframe(df.style.highlight_max(axis=0))

st.info('The \
        [API](https://docs.streamlit.io/en/latest/api.html#streamlit.dataframe) \
        provide more details on the highlighting of the dataframe.')

st.header('Drawing Charts and Maps')

st.subheader('Line chart  ')

st.write('First I created a random chart data:')
with st.echo():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

st.write('With just a line of code, I can create a line chart: ')
with st.echo():
    st.line_chart(chart_data)

st.info('This line chart is created using \
         [altair](https://altair-viz.github.io/index.html). \
         Feel free to take a look at the \
[API](https://docs.streamlit.io/en/latest/getting_started.html#draw-charts-and-maps) \
for more information.')

st.subheader('Area chart  ')

st.write('Using the same data, I created an area chart \
          using `st.area_chart` \
[API](https://docs.streamlit.io/en/latest/api.html#streamlit.area_chart) ')

with st.echo():
    st.area_chart(chart_data)


st.subheader('Bar chart')

with  st.echo():
    st.bar_chart(chart_data)

st.info('I used `st.bar_chart` \
[API](https://docs.streamlit.io/en/latest/api.html#streamlit.bar_chart) \
to create this graph.')

st.subheader('Altair Chart')

st.write('We can also explicitly create an altair chart:')

with st.echo():
    c = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)

st.subheader('Map of Saint Paul, MN')

st.write('First, let\'s start by creating 1000 random spots \
         around the Saint Paul, MN latitude, longitude area (44.96, -93.09) \
         and enclose them in `map_data` Pandas data frame. ')

with st.echo():
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [44.96, -93.09],
        columns=['lat', 'lon'])
    st.dataframe(map_data)

st.write('To evoke the map, we just write one line of code:')

with st.echo():
    st.map(map_data)

st.info('The map is fueled by [mapbox](https://mapbox.com).')

st.header('Add Interactivity with Widgets')

st.subheader('Use checkboxes to show/hide data')

st.write('We start by creating another random data called `chart_data2`: ')

with st.echo():
    chart_data2 = pd.DataFrame(
                  np.random.randn(20, 3),
                  columns=['a', 'b', 'c'])

st.write('Then create an `if` conditional for `st.checkbox()`: ')

with st.echo():
    if st.checkbox('Show line chart'):
        st.line_chart(chart_data2)

st.subheader('Use a selectbox for options')

st.write('Use `st.selectbox` to choose from a series. I am using the `df` \
          data frame to show the selectbox column: ')

st.dataframe(df)

with st.echo():
    option = st.selectbox('Which number do you like best?',
                           df['first column'])

st.write('To show the interactive output, we write: ')

with st.echo():
    'You selected: ', option

st.write('We can use the `option` variable to filter the `df` dataframe: ')

with st.echo():
    df.loc[df['first column']==option]


st.subheader('Use a radio button as an alternative to selectbox')

st.write('If we want to see all the options, we can use `radio` \
          to show a radio button widget, instead: ')

with st.echo():
    option2 = st.radio('Which number do you like best?',
                        df['first column'])

st.write('we can show the output by writing: ')

with st.echo():
    'You selected: ', option2

st.subheader('Use button widget to reveal a value')

st.write('We can use button widget to show the value of the second column \
          chosen in the earlier selectbox:')

with st.echo():
    if st.button('Would you like to see the second column value?'):
        second_value = df.loc[df['first column']==option2, 'second column']
        'the second column value is', second_value

st.subheader('Put widgets in a sidebar')

st.write('I can move a similar widget like the one created above \
          to a sidebar using `st.sidebar.selectbox`.')

with st.echo():
    option3 = st.sidebar.selectbox('Which number do you like best?',
                                    df['second column'])

'You selected: ', option3



st.warning("I got an error when I used the same `option` variable as \
         `st.selectbox` \
         :`DuplicateWidgetID: There are multiple identical st.selectbox \
         widgets with the same generated key.` So instead of following \
         the documentation, I selected `df['second column']` for my sidebar \
         widget example")

st.info('Other than `st.sidebar.selectbox`, most of the elements \
          can be put in a sidebar using the syntax: \
          `st.sidebar.[element_name]`. A few examples are: \
          `st.sidebar.markdown()`, `st.sidebar.slider()`, \
          `st.sidebar.line_chart`. ')

st.warning("I have difficulty in showing `'You selected: ', option2` in the \
          sidebar, so I moved it into the main web page. ")

st.header("Show Progress")

st.write('When adding long running computations to an app, \
          you can use `st.progress()` to display status in real time.')

st.write('First, `import time`, then create a progress bar:')

with st.echo():
    create_progress = st.button('Starting a long computation...')

    if create_progress:
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            time.sleep(0.1)
            bar.progress(i + 1)

        st.success('...and now we\'re done!')

st.header("Record a Screencast")

st.write('To start a screencast, locate the menu in the upper right hand \
          corner of your app, select **Record a screencast**, and follow the \
          prompts.')

st.write('Please refer to \
          [the original documentation] \
(https://docs.streamlit.io/en/latest/getting_started.html#record-a-screencast), \
          for more details on this animation:')

st.image("https://docs.streamlit.io/en/latest/_images/screenshare.gif",
         use_column_width = True)

st.header('Summary')

st.write('Using streamlit, we show a simple way to visualize \
          pandas DataFrame, charts, and maps. We can create various widgets \
          with minimal lines of code. We can record a screencast and \
          show an animated progress bar.')

st.write('To end, let\'s celebrate with flowing balloons and emojis: ')
with st.echo():
    if st.button('Let\'s celebrate with balloons and emoji!'):
        st.balloons()

