import streamlit as st
import matplotlib.image as mpimg
import matplotlib.pyplot as plt # plt.figure を使う場合などに備えてインポート

# --- ページの基本設定 (任意) ---
st.set_page_config(
    page_title="画像表示アプリ (Matplotlib使用)",
    layout="centered"
)

# --- メインの処理 ---
st.title("StreamlitでMatplotlibを使って画像表示")

st.header("ren.jpg の表示 (Matplotlibで読み込み)")

# Matplotlib (mpimg) を使って画像を読み込む
try:
    img_array = mpimg.imread("ren.jpg")
    # mpimg.imread() は画像を NumPy 配列として読み込みます。

    # Streamlit の st.image() を使って NumPy 配列の画像を表示
    st.image(img_array, caption="レンちゃん (Matplotlibで読み込み)", use_column_width=True)
    # use_column_width: Trueにすると、列の幅に合わせて画像サイズを調整します。

    # (参考) 読み込んだ画像の情報を表示
    st.write("読み込んだ画像の形式:", type(img_array))
    st.write("画像の次元:", img_array.shape) # (高さ, 幅, 色チャネル数)

except FileNotFoundError:
    st.error("エラー: ren.jpg が見つかりません。ファイルが正しい場所にあるか確認してください。")
except Exception as e:
    st.error(f"画像の読み込みまたは表示中にエラーが発生しました: {e}")

st.divider()

# --- (補足) Matplotlib の図 (Figure) として画像を表示し、それを Streamlit で表示する場合 ---
st.header("Matplotlibの図として表示 (st.pyplot)")
st.write("この方法は、画像にMatplotlibの軸やタイトルなどを加えたい場合に有効です。")

try:
    img_for_plot = mpimg.imread("ren.jpg")

    # Matplotlib の Figure オブジェクトを作成
    fig, ax = plt.subplots()
    ax.imshow(img_for_plot)
    ax.axis('off')  # 軸を非表示にする
    # fig.suptitle("Matplotlib Figure内のレンちゃん", fontsize=12) # Figureにタイトルを付ける場合

    # Streamlit の st.pyplot() を使って Matplotlib の Figure を表示
    st.pyplot(fig)

except FileNotFoundError:
    st.info("Matplotlibの図としての表示は、ren.jpg が見つからないためスキップされました。")
except Exception as e:
    st.error(f"Matplotlibの図の作成または表示中にエラーが発生しました: {e}")


# --- アプリの実行方法についての補足 ---
st.sidebar.info(
    """
    このアプリを実行するには:
    1. このファイルを .py 形式 (例: app_mpl.py) で保存します。
    2. "ren.jpg" を同じディレクトリに置きます。
    3. ターミナルで `streamlit run app_mpl.py` を実行します。
    """
)
