import streamlit as st

# --- ページの設定 ---
st.set_page_config(page_title="Artist Official Site", layout="centered")

# --- 背景画像とデザインの設定（CSS） ---
# ここで背景画像や全体の雰囲気を変えられます
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("https://unsplash.com");
        background-attachment: fixed;
        background-size: cover;
    }}
    .profile-frame {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
    }}
    h1 {{
        color: #1DB954; /* アーティストっぽい色（Spotifyグリーンなど） */
    }}
    </style>
    """, unsafe_allow_stdio=True)

# --- メインコンテンツ ---
st.markdown('<div class="profile-frame">', unsafe_allow_html=True)

# 1. プロフィール写真（URLを写真のリンクに変えてください）
# st.image("アーティストの写真のパスまたはURL")
st.image("https://placeholder.com", width=200)

# 2. アーティスト名と紹介
st.title("アーティスト名 / Artist Name")
st.subheader("Vocalist / Songwriter")

st.write("""
ここにアーティストの経歴やメッセージを載せます。
30年前に作っていたMIDIカラオケの話から、今の音楽活動に繋がるストーリーなどを書くと素敵ですね。
""")

# 3. リンクボタン
st.link_button("Latest Music (YouTube)", "https://youtube.com")
st.link_button("Official Instagram", "https://instagram.com")

st.markdown('</div>', unsafe_allow_html=True)
