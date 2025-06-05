import streamlit as st
from PIL import Image # 画像のサイズ調整などを行いたい場合に備えてインポート

# --- ページの基本設定 (任意) ---
st.set_page_config(
    page_title="画像表示アプリ",
    layout="centered" # "wide" も選択可能
)

# --- メインの処理 ---
st.title("Streamlitで画像表示")

st.header("ren.jpg の表示")

# 方法1: ファイルパスを直接指定 (推奨されるシンプルな方法)
try:
    st.image("ren.jpg", caption="可愛いレンちゃん", use_column_width=True)
    # caption: 画像の下に表示されるテキスト
    # use_column_width: Trueにすると、列の幅に合わせて画像サイズを調整します。'auto'や整数ピクセル値も指定可能。
except FileNotFoundError:
    st.error("エラー: ren.jpg が見つかりません。ファイルが正しい場所にあるか確認してください。")
except Exception as e:
    st.error(f"画像の読み込み中にエラーが発生しました: {e}")

st.divider() # 区切り線

# 方法2: Pillowを使って画像を読み込んでから表示 (事前に画像処理をしたい場合など)
st.header("Pillow経由での表示 (例)")
try:
    img = Image.open("ren.jpg")
    st.image(img, caption="Pillow経由のレンちゃん", width=300) # widthでピクセル指定も可能
except FileNotFoundError:
    st.info("Pillow経由の表示は、ren.jpg が見つからないためスキップされました。")
except Exception as e:
    st.error(f"Pillow経由での画像の読み込み中にエラーが発生しました: {e}")

# --- アプリの実行方法についての補足 ---
st.sidebar.info(
    """
    このアプリを実行するには:
    1. このファイルを .py 形式 (例: app.py) で保存します。
    2. "ren.jpg" を同じディレクトリに置きます。
    3. ターミナルで `streamlit run app.py` を実行します。
    """
)
