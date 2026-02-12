from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    t_score = sum(combined.count(char) for char in "true")
    l_score = sum(combined.count(char) for char in "love")
    
    # Simple logic to cap score at 100 or keep it as 2 digits
    score_str = f"{t_score}{l_score}"
    return int(score_str) if int(score_str) <= 100 else 99

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name1 = request.form.get("boy", "")
        name2 = request.form.get("girl", "")
        score = calculate_love_score(name1, name2)
        # Return JSON instead of HTML
        return jsonify(score=score)
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)