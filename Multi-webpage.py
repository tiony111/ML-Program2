# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
from distutils.command import clean
import streamlit as st
import numpy as np 
# import joblib
import base64
import time


def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{page_name}"><img src="data:image/jpg;base64,{data_url}" style="width:300px"></a>'

data_url = get_image_html("分類(0~9辨識)", "./Arabic numerals.jpg")
data_url_2 = get_image_html("分類[A(a)~Z(z)辨識]", "./English Alphabet.jpg")
data_url_3 = get_image_html("解聯立方程式", "./Solve equations.jpg")

st.set_page_config(
    page_title="個人作業演練",
    page_icon=":footprints:",
)


progress_text = "Operation in progress. Please wait.:mantelpiece_clock:"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

my_bar.empty()

st.title('Machine Learning 學習展示')  

tab1, tab2, tab3 = st.tabs([":blue[手寫數字(0~9)]", ":green[手寫英文字母(A~Z)]", ":orange[解聯立方程式]"])

# with tab1:
#    st.header("手寫數字(0~9)")
#    st.image("./Arabic numerals.jpg", width=200)

# with tab2:
#    st.header("手寫英文字母(A~Z)")
#    st.image("./English Alphabet.jpg", width=200)

# with tab3:
#    st.header("解聯立方程式")
#    st.image("./Solve equations.jpg", width=200)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)

with tab1:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [(0~9辨識)手寫數字](分類(0~9辨識))')
    st.markdown(data_url, unsafe_allow_html=True)
    st.markdown('''
    ##### 特徵(X):
        - 請手寫阿拉伯數字0~9
    ##### 預測類別(Class):
        - 數字0~9
        ''')
    # st.image('iris.png')
    # st.markdown(data_url, unsafe_allow_html=True)

with tab2:
    st.markdown('### [(A(a)~Z(z)辨識)手寫英文字母](分類[A(a)~Z(z)辨識])')
    st.markdown(data_url_2, unsafe_allow_html=True)
    st.markdown('''
    ##### 特徵(X):
        - 請手寫大或小寫英文字母A(a)~Z(z)
    ##### 預測類別(Class):
        - 英文字母A~Z
        ''')

with tab3:
    st.markdown('### [(解聯立方程式)輸入方程式](解聯立方程式)')
    st.markdown(data_url_3, unsafe_allow_html=True)
    st.markdown('''
    ##### 使用方法:
        - 請輸入聯立方程式
    ##### 求解:
        - 變數x, y
        ''')

# with col1:
#     # url must be external url instead of local file
#     # st.markdown(f"### [![分類]({url})](分類)")
#     st.markdown('### [(分類(0~9辨識))手寫數字](分類(0~9辨識))')
#     st.markdown('''
#     ##### 特徵(X):
#         - 島嶼
#         - 嘴巴長度
#         - 嘴巴寬度
#         - 翅膀長度
#         - 體重
#         - 性別
#     ##### 預測類別(Class):
#         - Adelie
#         - Chinstrap
#         - Gentoo
#         ''')
#     # st.image('iris.png')
#     st.markdown(data_url, unsafe_allow_html=True)
# with col2:
#     st.markdown('### [(迴歸)計程車小費預測](迴歸)')
#     st.markdown('''
#     ##### 特徵(X):
#         - 車費
#         - 性別
#         - 吸菸
#         - 星期
#         - 時間
#         - 同行人數
#     ##### 目標：預測小費金額
#         ''')
#     # st.image('taxi.png')
#     st.markdown(data_url_2, unsafe_allow_html=True)
