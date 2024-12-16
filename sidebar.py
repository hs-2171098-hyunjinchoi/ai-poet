import streamlit as st

def show_sidebar():
    st.sidebar.title("📋 About AI Poet")
    st.sidebar.markdown("### Features")
    st.sidebar.write("📌 **Write a Poem**")
    st.sidebar.write("📗 **Suggest a Topic**")
    st.sidebar.write("📙 **Saved Poems**")
    st.sidebar.write("📕 **Share Your Poem**")
    st.sidebar.markdown("---")
    st.sidebar.write("⚙️ **Settings**")
