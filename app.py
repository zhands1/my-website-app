import streamlit as st
import base64
import os

# --- 1. ページの設定 (必ず最初に書く) ---
st.set_page_config(page_title="Artist Official Site", layout="centered")

# --- 2. 画像をBase64に変換する関数 ---
# Streamlit Cloudでローカルの背景画像を表示するために必要です
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# 画像の読み込み（パスが正しいか確認してください）
bg_base64 = get_base64_image("images/background.jpg")

# --- 3. 背景画像とデザインの設定（CSS） ---
if bg_base64:
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bg_base64}");
            background-attachment: fixed;
            background-size: cover;
        }}
        .profile-frame {{
            background-color: rgba(255, 255, 255, 0.8); /* 白背景を少し透過 */
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            margin-top: 50px;
        }}
        h1 {{
            color: #1DB954; /* アーティストっぽい色 */
        }}
        /* 右上のメニューや下のフッターを隠す設定（オプション） */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)
else:
    # 画像が見つからない場合の予備設定
    st.warning("背景画像（images/background.jpg）が見つかりません。パスを確認してください。")

# --- 4. メインコンテンツ ---
# 全体を枠（profile-frame）で囲む
st.markdown('<div class="profile-frame">', unsafe_allow_html=True)

# プロフィール写真
# st.imageはBase64変換しなくてもパス指定で表示可能です
try:
    st.image("images/profile.png", width=200)
except:
    st.write("（プロフィール画像が読み込めませんでした）")

# アーティスト名と紹介
st.title("アーティスト名 / Artist Name")
st.subheader("Vocalist / Songwriter")

st.write("""
ここにアーティストの経歴やメッセージを載せます。
30年前に作っていたMIDIカラオケの話から、今の音楽活動に繋がるストーリーなどを書くと素敵ですね。
""")

# リンクボタン
st.link_button("Latest Music (YouTube)", "https://youtube.com")
st.link_button("Official Instagram", "https://instagram.com")

st.markdown('</div>', unsafe_allow_html=True)
