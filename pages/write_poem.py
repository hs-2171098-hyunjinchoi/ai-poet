from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Error: OPENAI_API_KEY is not set in the .env file")


from langchain_openai import ChatOpenAI

# Configure ChatOpenAI model
# chat_model = ChatOpenAI()
chat_model = ChatOpenAI(openai_api_key=api_key)

## test
# try:
#     result = chat_model.invoke("hello")
#     print(result.content)
# except Exception as e:
#     print("Error:", e)


import streamlit as st
from sidebar import show_sidebar
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="AI Poet", layout="wide", initial_sidebar_state="expanded")
show_sidebar()

# Load CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Custom Style for Dark Mode UI
st.markdown("""
    <style>
        /* Main background and font settings */
        .main {
            background-color: #181818;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
        }
        .block-container {
            padding: 2rem;
        }
        /* Card style */
        .card {
            background: #232836;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin-bottom: 1rem;
        }
        .card h3 {
            margin: 0;
            color: #FFFFFF;
        }
        .card p {
            color: #DDDDDD;
        }
        /* Tag style */
        .tag {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            margin: 0.2rem;
            background-color: #3D3D3D;
            border-radius: 5px;
            color: #E0E0E0;
            font-size: 0.9rem;
        }
        /* Column spacing */
        .st-emotion-cache-1kyxreq {
            margin-right: 1rem;
        }
        /* Center alignment for cards */
        .centered-card {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 style='text-align: center;'>AI Poem Creation Board</h1>", unsafe_allow_html=True)

# Add space below the main title
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Two-column layout
col1, col2 = st.columns(2)

# Left Column - User Input and Topic Selection
with col1:
    st.markdown("### Select Topic and Format")
    subject = st.text_input("Enter the poem's topic", placeholder="e.g., Winter, Cat")
    poem_type = st.selectbox("Choose the poem's format", ["Free Verse", "Structured", "Prose", "Lyric", "Epic", "Dramatic"])
    language = st.selectbox("Select the language", ["English", "한국어", "Français", "日本語"])

    # Recommend topic button
    if st.button("🔍 Recommend Topic"):
        with st.spinner("AI is recommending a topic..."):
            recommended = chat_model.invoke("Recommend an interesting and creative topic for a poem.")
            st.success(f"Recommended Topic: {recommended.content}")

    # Start poem creation button
    if st.button("🚀 Start Poem Creation"):
        if subject and poem_type and language:
            with st.spinner("AI is generating the poem..."):
                prompt = f"Write a poem about {subject} in the style of {poem_type} in {language}."
                result = chat_model.invoke(prompt) 
                st.session_state['completed'] = result.content  
                st.session_state['subject'] = subject 
                st.success("Poem generation complete!")
        else:
            st.warning("Please fill in all fields before generating the poem.")



# Right Column - Poem Display
with col2:
    st.markdown("### Your Poem")

    if 'completed' in st.session_state:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")  # Current date and time
        st.markdown(f"""
        <div class='card centered-card'>
            <div>
                <h3 style="color:#FFFFFF; margin-bottom:0.5rem;">{st.session_state.get('subject', 'Untitled')}</h3>
                <p style="color:#DDDDDD; margin-bottom:1rem;">{st.session_state['completed']}</p>
                <div>
                    <span class="tag date">{current_datetime}</span>
                    <span class="tag type">{poem_type}</span>
                    <span class="tag language">{language}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Save poem button
        if st.button("💾 Save Poem"):
            poem_data = {
                "title": st.session_state.get('subject', 'Untitled'), 
                "content": st.session_state['completed'], 
                "type": poem_type,
                "language": language,
                "date": current_datetime
            }
            st.session_state.setdefault('saved_poems', []).append(poem_data)
            st.success("Poem has been saved!")
