import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

########################
# Title page
########################

image = Image.open('DNA_Count_Web_App.png')
st.image(image, use_column_width=True)

st.write(""" #DNA Nucleotide Count Web App.
         This app counts the nucleotide composition of query DNA ***
         """)

#####################
#input textbox
#####################
#st.sidebar.header('Enter DNA Sequence')
st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nTTTGGGGGGGAATATACCCC\nTATAGCCCCTAGTAATGCTA\nGAGATCCATAGAGATAGACT\nTGTACCCATATAGCCGTATC"

#sequence = st.sidebar.text_area("Sequence_input", sequence_input, height =250)
sequence = st.text_area("Sequence_input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence

sequence = sequence[1:] # skip's the sequnece name (first line)
sequence

sequence = ''.join(sequence) # contenates list to string
sequence

st.write(""" 
         ***
         """)
#Prints the input DNA sequence
st.header('INPUT (DNA Query)')

#DNA Nucleotide Count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucletide_count(seq):
  # sourcery skip: inline-immediately-returned-variable
  d = dict ([
       ('A',seq.count('A')),
       ('T',seq.count('T')),
       ('G',seq.count('G')),
       ('C',seq.count('C'))
   ])
  return d

  
X = DNA_nucletide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())
X
###Print Text

st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' Cytosine (C)')

###Display Dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

### 4. Display Barchart
st.subheader('4. Display Barchart')
p = alt.Chart(df).mark_bar().encode(
  x = 'nucleotide',
  y = 'count'
)

p = p.properties(
    width=alt.Step(70) #controls width of bar
)
st.write(p)

