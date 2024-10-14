import streamlit as st

precioPost = 102
precioReel = 12
precioStory = 8

st.title("Generado de Cotizaciones")

posts = st.number_input("Ingrese cantidad de publicaciones estáticas al mes: ", min_value=0, step=1)
reels = st.number_input("Ingrese la cantidad de reels al mes: ", min_value=0, step=1)
stories = st.number_input("Ingrese la cantidad de stories al mes: ", min_value=0, step=1)

if st.button("Calcular Cotización"):
    totalPosts = posts * precioPost
    totalReels = reels * precioReel
    totalStories = stories * precioStory
    totalDescripciones = posts * 1
    total = totalPosts + totalReels + totalStories + totalDescripciones

    st.write(f"Publicaciones estáticas: {posts} x ${precioPost} = ${totalPosts}")
    st.write(f"Reels: {reels} x ${precioReel} = ${totalReels}")
    st.write(f"Stories: {stories} x ${precioStory} = ${totalStories}")
    st.write(f"**Total: ${total}**")
