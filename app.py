import streamlit as st
import requests

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        url = "http://127.0.0.1:8000/api/auth/login/"
        response = requests.post(url, data={"username": username, "password": password})
        
        if response.status_code == 200:
            token = response.json()['access']
            st.session_state['token'] = token  # 세션에 토큰 저장
            st.session_state.login = True
            st.success("로그인 성공!")
        else:
            st.error("로그인 실패")

# Django 백엔드 API에서 질문 목록 데이터를 가져오는 함수
def get_questions(headers):
    url = "http://127.0.0.1:8000/api/qa/questions/"  # Django 백엔드 API URL
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        st.error("질문 목록을 불러오는 데 실패했습니다.")
        return []

# Django 백엔드 API에서 특정 질문의 상세 정보를 가져오는 함수
def get_question_detail(pk, headers):
    url = f"http://127.0.0.1:8000/api/qa/questions/{pk}/"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        st.error("질문 상세 정보를 불러오는 데 실패했습니다.")
        return {}

if "login" not in st.session_state:
    st.session_state["login"] = False
    st.session_state['token'] = None

if 'jwt_token' not in st.session_state:
    login()

if st.session_state['login']:
    st.title("질문 목록")
    headers = {
        "Authorization": f"Bearer {st.session_state['token']}"
    }
    
    questions = get_questions(headers=headers)

    if questions:
        for question in questions:
            st.subheader(question['content'])
            st.write(f"작성자: {question['author']}")
            
            # 각 질문에 대한 버튼을 생성
            if st.button(f"상세 보기 - {question['content']}", key=question['id']):
                # 버튼이 클릭되면 해당 질문의 상세 정보를 가져옵니다.
                question_detail = get_question_detail(question['id'], headers=headers)
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
