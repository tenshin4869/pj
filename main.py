import cv2

# カメラを初期化
cap = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)

if not cap.isOpened():
    print("カメラを開けませんでした。デバイスを確認してください。")
    exit()



while True:
    # フレームを取得
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした。")
        break

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # グレースケール画像を表示
    cv2.imshow("Gray Frame", gray)

    # ESCキーで終了
    if cv2.waitKey(1) & 0xFF == 27:
        break

# リソースを解放
cap.release()
cv2.destroyAllWindows()
