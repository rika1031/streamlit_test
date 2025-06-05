import streamlit as st
import matplotlib.image as mpimg
import matplotlib.pyplot as plt # plt.figure を使う場合などに備えてインポート

# --- ページの基本設定 (任意) ---
st.set_page_config(
    page_title="Nyan Page",
    layout="centered"
)

# --- メインの処理 ---
st.title("可愛い猫写真をアップロード！！！")


# Matplotlib (mpimg) を使って画像を読み込む
try:
    img_array = mpimg.imread("ren.jpg")
    # mpimg.imread() は画像を NumPy 配列として読み込みます。

    # Streamlit の st.image() を使って NumPy 配列の画像を表示
    st.image(img_array, caption="レンちゃん")
    # use_column_width: Trueにすると、列の幅に合わせて画像サイズを調整します。


except FileNotFoundError:
    st.error("エラー: ren.jpg が見つかりません。ファイルが正しい場所にあるか確認してください。")
except Exception as e:
    st.error(f"画像の読み込みまたは表示中にエラーが発生しました: {e}")

st.divider()
