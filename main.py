import streamlit as st
from sidebar import show_sidebar

show_sidebar()

# Title
st.markdown("<h1 style='text-align: center;'>📖 What is AI Poet?</h1>", unsafe_allow_html=True)

# Add space below the main title
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Animated Description with Purple Keywords
st.markdown("""
<div style="
    font-size: 20px; 
    line-height: 1.8; 
    text-align: center; 
    animation: fadeMove 3s infinite;">
    <b class="purple-keyword">AI Poet</b> is a creative project that uses 
    <b class="purple-keyword">artificial intelligence</b> to generate poems <br>
    based on <b class="purple-keyword">user input</b>. You can 
    <b class="purple-keyword">write poems</b>, explore <b class="purple-keyword">topics</b>, and read 
    <b class="purple-keyword">inspiring articles</b>.
</div>

<style>
/* Animation for the fadeMove effect */
@keyframes fadeMove {
    0% { opacity: 1; transform: translateY(0px); }
    50% { opacity: 0.5; transform: translateY(-5px); }
    100% { opacity: 1; transform: translateY(0px); }
}


</style>
""", unsafe_allow_html=True)
