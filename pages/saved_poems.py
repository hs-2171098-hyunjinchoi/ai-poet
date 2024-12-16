import streamlit as st
from sidebar import show_sidebar

st.set_page_config(page_title="Saved Poems", layout="wide")
show_sidebar()

# Load CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         .tag {
#             display: inline-block;
#             padding: 6px 12px;
#             margin: 4px 4px 0 0;
#             background-color: #6A5ACD; 
#             color: #FFFFFF;
#             font-weight: bold;
#             border-radius: 20px;
#             font-size: 0.85rem;
#             text-align: center;
#             box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
#         }
#     </style>
# """, unsafe_allow_html=True)

# Main Title
st.title("📚 Saved Poems")

# Add space below the main title
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Check if poems are saved
if 'saved_poems' not in st.session_state:
    st.session_state['saved_poems'] = []

# Display poems in card format
if st.session_state['saved_poems']:
    for i, poem in enumerate(st.session_state['saved_poems']):
        st.markdown(f"""
       <div class="card">
            <h3>{poem['title']}</h3>
            <p>{poem['content']}</p>
            <div>
                <span class="tag date">🗓 {poem['date']}</span>
                <span class="tag type">📝 {poem['type']}</span>
                <span class="tag language">🌐 {poem['language']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.info("No saved poems yet.")
