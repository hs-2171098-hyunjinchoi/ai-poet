# pip install python-dotenv
# pip install langchain-openai
# pip install streamlit

# from dotenv import load_dotenv
# import os

# .env 파일 로드
# load_dotenv()

# 환경 변수에서 API 키 가져오기
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise ValueError("Error: OPENAI_API_KEY is not set in the .env file")

from langchain_openai import ChatOpenAI

# ChatOpenAI 모델 설정
chat_model = ChatOpenAI()
# chat_model = ChatOpenAI(openai_api_key=api_key)

# 모델 호출 테스트
# try:
#     result = chat_model.invoke("hello")
#     print(result.content)
# except Exception as e:
#     print("Error:", e)
    
import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요!")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
