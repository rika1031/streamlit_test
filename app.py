from PIL import Image

try:
    # 画像ファイルを開く
    img = Image.open("ren.jpg")
    # 画像を表示する
    img.show()
except FileNotFoundError:
    print("エラー: ren.jpg が見つかりません。ファイルパスを確認してください。")
except Exception as e:
    print(f"エラーが発生しました: {e}")
