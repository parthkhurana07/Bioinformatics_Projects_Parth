import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle


def desc_calc():
    bashCommand= "java -Xms1G -Xmx1G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process= subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error= process.communicate()
    os.remove('molecule.smi')


def filedownload(df):
    csv= df.to_csv(index=False)
    b64= base64.b64encode(csv.encode()).decode()
    href= f'<a href="data:file/csv;base64,{b64}" download='
    return href


def build_model(input_data):
    load_model= pickle.load(open('protease_hiv_model.pkl'))
    prediction= load_model.predict(input_data)
    st.header('**Prediction Output**')
    prediction_output= pd.Series(prediction, name='pIC50')
    molecule_name= pd.Series(load_data[1], name='molecule_name')
    df= pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)


image= Image.open('HIV_protease.png')

st.image(image, use_column_width=True)

st.markdown("""
#Bioactivity Prediction App (Protease)

This web application allows you to predict bioactivity data of Protease derived from Human Immundodeficientcy Virus 1

**Credits**
Parth Khurana
""")

with st.sidebar.header('1. Upload your CSV Data'):
    uploaded_file= st.sidebar.file_uploader("Upload your input file", type= ['txt'])


if st.sidebar.button('Predict'):
    load_data= pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep= '\t', header= False, index= False)

    st.header('**Original Input Data**')
    st.write(load_data)

    with st.spinner("Calculating descriptors..."):
        desc_calc()

    st.header('**Calculated Molecular Descriptors**')
    desc= pd.read_csv('descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    st.header('**Subset of Descriptors from Previously Built Models**')
    Xlist= list(pd.read_csv('descriptors_list.csv').columns)
    desc_subset= desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    build_model(desc_subset)
else:
    st.info('Upload input data in the sidebar to start!')

