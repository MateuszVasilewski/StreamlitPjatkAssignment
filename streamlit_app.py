import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import pipeline

st.title('Various Transformers')

# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
# time.sleep(2)
# st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

"App for using transformers lib along with streamlit."
"Open one of the apps, write something, press enter+ctrl and wait for result."

st.header('Choose an  app')

option = st.selectbox(
    "Options",
    [
        "Sequence classification",
        "Translator",
    ],
)

if option == "Sequence classification":
    text = st.text_area(label="Input text")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

if option == "Translator":
    text = st.text_area(label="Input text")
    if text:
        with st.spinner():
            try:
                classifier = pipeline("translation_en_to_de")
                answer = classifier(text)
                st.success("Success")
                st.write(answer)
            except:
                st.error("Error")

"s18668"
