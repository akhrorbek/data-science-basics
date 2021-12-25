import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jpg')

st.image(image, use_column_width=True)
st.write("""
## Simple DNA App

This app counts the composition of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa"

sequence = st.text_area("sequence input", sequence_input, height=250)
sequence= sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Count)')

st.subheader('1. Print Dictionary')
def DNA_count(seq):
    d = dict([
    ('A', seq.count('A')),
    ('B', seq.count('B')),
    ('C', seq.count('C')),
    ('F', seq.count('F')),
    ('X', seq.count('X'))
    ])

    return d

x = DNA_count(sequence)
x_label = list(x)
x_values = list(x.values())

x

st.subheader('2. print text')
st.write('There are ' + str(x['A']) + ' adenine (A)')
st.write('There are ' + str(x['X']) + ' adenine (X)')
st.write('There are ' + str(x['F']) + ' adenine (F)')


st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
#df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar line_chart')
p = alt.Chart(df).mark_bar().encode(
    x='index',
    y='count'
)

p = p.properties(
    width=alt.Step(75)
)
st.write(p)
