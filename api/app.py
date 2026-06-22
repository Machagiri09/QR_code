from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link", "").strip()
        if link:
            # Redirect to the image route, passing the link as a query param
            from flask import redirect, url_for
            return redirect(url_for("index", link=link))

    link = request.args.get("link", "")
    return render_template("index.html", link=link)


@app.route("/qrcode")
def generate_qr():
    link = request.args.get("link", "")
    if not link:
        return "No link provided", 400

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
