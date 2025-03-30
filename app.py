import streamlit as st
import requests

# Django 백엔드 API에서 질문 목록 데이터를 가져오는 함수
def get_questions():
    url = "http://127.0.0.1:8000/api/qa/questions/"  # Django 백엔드 API URL
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        st.error("질문 목록을 불러오는 데 실패했습니다.")
        return []

# Django 백엔드 API에서 특정 질문의 상세 정보를 가져오는 함수
def get_question_detail(pk):
    url = f"http://127.0.0.1:8000/api/qa/questions/{pk}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        st.error("질문 상세 정보를 불러오는 데 실패했습니다.")
        return {}

# Streamlit UI 설정
st.title("질문 목록")

# 질문 데이터 가져오기
questions = get_questions()

if questions:
    for question in questions:
        st.subheader(question['content'])
        st.write(f"작성자: {question['author']}")
        
        # 각 질문에 대한 버튼을 생성
        if st.button(f"상세 보기 - {question['content']}", key=question['id']):
            # 버튼이 클릭되면 해당 질문의 상세 정보를 가져옵니다.
            question_detail = get_question_detail(question['id'])
            if question_detail:
                # 상세 정보 출력
                st.write("### 질문 상세 정보")
                st.write(f"**질문 내용**: {question_detail.get('content')}")
                st.write(f"**좋아요**: {question_detail.get('like')}")
                st.write(f"**싫어요**: {question_detail.get('unlike')}")
                st.write(f"**생성 일시**: {question_detail.get('create_date')}")
                st.markdown("---")
else:
    st.write("질문이 없습니다.")
