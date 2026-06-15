import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from detector import detect_objects
from face_detector import detect_faces
from utils import save_history



st.title("AI vision Image system")

menu=st.sidebar.selectbox(
    "Choose Module",
    [
        "Image Detection",
        "Face Detection",
        "Detection Dashboard"
    ]

)

#Image Detection
if menu == "Image Detection":
    file = st.file_uploader("Upload Image")
    if file:
        image=Image.open(file)
        st.image(image)
        img=np.array(image)
        detections,count,output=detect_objects(img)
        st.subheader("Detected Objects")
        objects=[]
        for obj,conf in detections:
            st.write(f"{obj} : {round(conf*100,2)}%")
            objects.append((obj, conf))
        save_history(objects)
        st.image(output)
        st.subheader("Object Counts")
        st.write(count)

#Face Detection
if menu == "Face Detection":
    file = st.file_uploader("Upload Face Image")
    if file:
        image=Image.open(file)
        img=np.array(image)
        result,count=detect_faces(img)
        st.image(result)
        st.write("Faces Detected:",count)


#Dashboard
if menu == "Detection Dashboard":
    df=pd.read_csv("history.csv")
    st.write(df)
    st.bar_chart(df["object"].value_counts())