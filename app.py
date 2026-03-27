from flask import Flask, request, jsonify, render_template
from scraper.lailai import get_price_lailai
from scraper.sanmiao import get_price_sanmiao

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compare")
def compare():
    keyword = request.args.get("item", "").strip()
    if not keyword:
        return jsonify({"error": "請提供 item 參數，例如：/compare?item=牛奶"}), 400

    results = []

    lailai = get_price_lailai(keyword)
    if lailai:
        results.append(lailai)

    sanmiao = get_price_sanmiao(keyword)
    if sanmiao:
        results.append(sanmiao)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
