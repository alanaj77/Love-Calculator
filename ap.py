from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_love_score(name1, name2):
    name = name1.lower() + name2.lower()

    t = [0,0,0,0]
    l = [0,0,0,0]

    true = "true"
    love = "love"

    for match in true:
        count = 0
        for letter in name:
            if letter == match:
                count += 1
        t[true.index(match)] = count

    for match in love:
        count = 0
        for letter in name:
            if letter == match:
                count += 1
        l[love.index(match)] = count

    score = int(str(sum(t)) + str(sum(l)))
    return score


@app.route("/", methods=["GET","POST"])
def home():
    score = None
    if request.method == "POST":
        name1 = request.form["boy"]
        name2 = request.form["girl"]
        score = calculate_love_score(name1, name2)

    return render_template("index.html", score=score)


if __name__ == "__main__":
    app.run()

