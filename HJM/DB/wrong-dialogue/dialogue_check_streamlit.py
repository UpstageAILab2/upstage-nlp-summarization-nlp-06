import os
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .main {
        max-width: 100%;
        margin-left: 0;
    }
    .text-container {
        white-space: pre-wrap; /* 텍스트 줄 바꿈 처리 */
        word-wrap: break-word; /* 길게 이어지는 단어 줄 바꿈 처리 */
        overflow: visible; /* 스크롤바 제거 */
        font-size: 20px; /* 글자 크기 설정 */
    }
    .stButton > button {
        width: 100%; /* 버튼 너비 설정 */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('데이터 확인')


train_df = pd.read_csv('../../data/train_regular-expression.csv')
valid_df = pd.read_csv('../../data/dev_regular-expression.csv')

def save_feedback(data_option, feedback_opt, feedback_text):
    feedback_df = pd.DataFrame([[feedback_opt, feedback_text]], columns=['Option', 'Feedback'])
    feedback_df.to_csv(f'{data_option}_GoodBad.csv', mode='a', header=not os.path.exists(f'{data_option}_GoodBad.csv'), index=False)

data_option = st.selectbox(
    label='데이터셋 선택',
    options=('train', 'valid'),
    index=None,
    label_visibility='collapsed',
    placeholder='데이터셋 선택'
)

if data_option:
    if data_option == 'train':
        data = train_df
    else:
        data = valid_df

    if 'idx' not in st.session_state:
        st.session_state.idx = 100 # 0
    if 'show_text_input' not in st.session_state:
        st.session_state.show_text_input = False

    idx = st.session_state.idx
    if idx < data.shape[0]:
        # st.text(f"[대화]\n{data.iloc[idx, 1]}\n\n[요약]\n{data.iloc[idx, 2]}")
        st.markdown(
            f"<div class='text-container'><pre>[{idx}/{data.shape[0]}]</pre><pre>[대화]\n{data.iloc[idx, 1]}</pre><pre>[요약]\n{data.iloc[idx, 2]}</pre></div>", 
            unsafe_allow_html=True
        ) 

        col1, col2 = st.columns(2)

        with col1:
            if st.button(label='Good'):
                good_feedback = '없음'
                data.at[idx, 'Feedback'] = good_feedback
                save_feedback(data_option, 'Good', good_feedback)
                st.session_state.idx += 1
                st.rerun()
            
        with col2:       
            if st.button(label='Bad'):
                st.session_state.show_text_input = True
            if st.session_state.show_text_input:
                bad_feedback = st.text_input(label='피드백')
                if st.button(label='저장'):
                    data.at[idx, 'Feedback'] = bad_feedback
                    save_feedback(data_option, 'Bad', bad_feedback)
                    st.session_state.show_text_input = False
                    st.session_state.idx += 1
                    st.rerun()

        col3, col4, _, _ = st.columns(4)

        with col3:
            if st.button(label='이전'):
                st.session_state.idx -= 1
                st.rerun()
        
        with col4:
            if st.button(label='다음'):
                st.session_state.idx += 1
                st.rerun()

    else:
        data.to_csv(f'./{data_option}_GoodBad_ALL.csv', index=False)
        st.write('Saved.')