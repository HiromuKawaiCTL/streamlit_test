# app.py

import streamlit as st

# Title
st.title('こんにちは！Streamlit！')

# HTML+CSSだけ
st.markdown("""
<style>
/* メインコンテンツの背景を変更 */
div.block-container {
    background-color: #ffe4e1;
    padding: 2rem;
    border-radius: 1rem;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #f5deb3;
}
</style>
""", unsafe_allow_html=True)



# Markdown部分は別で書く（HTMLじゃないので unsafe_allow_html=False）
st.markdown("""
# プロフィール紹介

**名前**：山田 太郎  
*趣味*：プログラミング、読書、ランニング  

---

## 好きな果物ランキング🍎

1. りんご  
2. みかん  
3. バナナ  

---

## お問い合わせ

[こちらをクリックしてね](https://example.com)
""")



# Text
st.write('これはStreamlitの最初のアプリやで！')

# インタラクション（例：スライダー）
age = st.slider('年齢を選んでや', 0, 100, 25)
st.write(f'君の年齢は {age} やな！')

# ボタン
if st.button('挨拶して'):
    st.write('やっほー！Streamlitへようこそ！')

# 👇 サイドバーの中身
st.sidebar.title("メニュー")
option = st.sidebar.selectbox(
    "好きな果物は？",
    ("りんご", "バナナ", "みかん")
)

st.write(f"選んだ果物: {option}")



st.write(f"選んだ果物: {option}")