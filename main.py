import cv2

# カメラを初期化
cap = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)

if not cap.isOpened():
    print("カメラを開けませんでした。デバイスを確認してください。")
    exit()

# 平均フレーム（基準フレーム）を初期化
avg = None

while True:
    # フレームを取得
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした。")
        break

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 最初のフレームを基準フレームとして設定
    if avg is None:
        avg = gray.copy().astype("float")
        continue

    # 現在のフレームとの差分を計算
    cv2.accumulateWeighted(gray, avg, 0.6)  # 移動平均
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))  # 差分

    # 差分画像に閾値処理を適用
    thresh = cv2.threshold(frameDelta, 40, 255, cv2.THRESH_BINARY)[1]

    # 閾値処理後の画像を表示
    cv2.imshow("Threshold Frame", thresh)

    # ESCキーで終了
    if cv2.waitKey(1) & 0xFF == 27:
        break

# リソースを解放
cap.release()
cv2.destroyAllWindows()
