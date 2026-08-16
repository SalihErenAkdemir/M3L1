from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/bilgiler")
def bilgiler():
    bilgiler = ["Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.", "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.", "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."]
    return '<p>' + random.choice(bilgiler) + '<p>'

app.run(debug=True)