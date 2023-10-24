from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 업로드된 사진을 저장할 경로
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def show_frame():
    if request.method == "POST":  # 업로드된 파일을 받아옴
        uploaded_file = request.files["file"]

        if uploaded_file:  # 파일을 저장할 경로 설정
            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"], uploaded_file.filename
            )
            uploaded_file.save(file_path)

            # 업로드한 사진의 URL 생성
            photo_url = f"/{UPLOAD_FOLDER}/{uploaded_file.filename}"
            return render_template("index.html", photo_url=photo_url)

    return render_template("index.html", photo_url="")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
