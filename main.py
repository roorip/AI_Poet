from langchain.chat_models import ChatOpenAI  
from langchain.schema import HumanMessage 
import streamlit as st


chat_model = ChatOpenAI(
    temperature=0.7,  
    model_name="gpt-4" 
)


st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제: " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중..."):
        user_message = HumanMessage(content=f"{subject}에 대한 시를 써줘")
        result = chat_model([user_message])  # 메시지를 리스트로 전달
        st.write(result.content)  # 응답 내용 출력
