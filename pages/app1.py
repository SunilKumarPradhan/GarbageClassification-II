import streamlit as st
import os

def app():
    st.title("GreenGuardian: Garbage Classification")

    st.subheader("Objective :")
    st.markdown("The main Objective of this project is to use `Machine Learning` and `Deep learning` to categorize the garbage image into 6 different classes namely :", True)
    
    st.subheader("Motivation :")
    st.markdown("This Project has been created as part of the <b>Trithon Hackathon </b> presented by <b>Team Hacktivist</b>", True)
    st.markdown("The main motivation behind this project is to create a solution to the problem of garbage classification and recycling.", True)
    st.markdown("<hr/>", True)

    st.subheader("Description :")
    st.markdown("This Project uses `Fine Tuned InceptionV3 Model` which is a <b> Pre-Trained CNN Model</b> from Keras.", True)
   

    st.markdown("<hr/>", True)

    st.subheader("Tribute:")
    st.markdown("Thanks for giving us this Opportunity , our team remains thankful to you ! ", True)
    