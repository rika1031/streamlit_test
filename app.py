import streamlit as st
import matplotlib.image as mpimg
# import matplotlib.pyplot as plt # plt.figure を使う場合などに備えてインポート (今回は未使用)

# --- ページの基本設定 ---
st.set_page_config(
    page_title="Nyan Page",
    layout="centered"  # これでページ全体のコンテナが中央寄せになります
)

# --- メインの処理 ---

# タイトルを中央寄せ
# st.title() の代わりに st.markdown() を使い、HTMLで中央揃えを指定します。
st.markdown("<h1 style='text-align: center;'>可愛い猫写真をアップロード！！！</h1>", unsafe_allow_html=True)


# Matplotlib (mpimg) を使って画像を読み込む
try:
    img_array = mpimg.imread("ren.jpg")
    # mpimg.imread() は画像を NumPy 配列として読み込みます。

    # 画像を中央の列に配置して表示
    # st.columnsを使用して3列レイアウトを作り、中央の列に画像を表示します。
    # 比率 [1, 2, 1] は、中央の列が左右の列の2倍の幅を持つことを意味し、
    # 画像を中央に配置するのに役立ちます。比率は適宜調整してください。
    col1, col2, col3 = st.columns([1, 2, 1]) 
    with col2:
        st.image(img_array, caption="レンちゃん", use_column_width='auto')
        # use_column_width:
        # 'auto' (デフォルト): 画像の自然な幅で表示し、列幅を超える場合は縮小します。
        # 'always': 列幅いっぱいに画像を広げます。
        # widthパラメータで画像の幅をピクセル指定することも可能です。

except FileNotFoundError:
    # エラーメッセージも中央の列に配置します。
    err_col1, err_col2, err_col3 = st.columns([0.5, 3, 0.5]) # 中央の列を広めに取ると見やすいです
    with err_col2:
        st.error("エラー: ren.jpg が見つかりません。ファイルが正しい場所にあるか確認してください。")
except Exception as e:
    # その他のエラーメッセージも中央の列に配置します。
    ex_col1, ex_col2, ex_col3 = st.columns([0.5, 3, 0.5])
    with ex_col2:
        st.error(f"画像の読み込みまたは表示中にエラーが発生しました: {e}")

st.divider()
# st.divider() は layout="centered" の設定の場合、中央に配置されたコンテナの幅いっぱいに表示されます。
# もし区切り線自体をさらに短くして中央に配置したい場合は、
# st.markdown("<hr style='width:50%; margin-left:auto; margin-right:auto;'>", unsafe_allow_html=True)
# のようなHTML/CSSのカスタマイズが必要になりますが、通常はデフォルトのままで中央にあるように見えます。
