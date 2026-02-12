from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
def calculate_love_score(name1, name2):
    # 1. Clean the names
    n1 = name1.lower().replace(" ", "")
    n2 = name2.lower().replace(" ", "")
    
    # 2. Find common and unique characters using Sets
    set1 = set(n1)
    set2 = set(n2)
    
    common = set1.intersection(set2)
    all_unique = set1.union(set2)
    
    # 3. Calculate a ratio (Jaccard Similarity concept)
    # How many letters they share vs the total variety of letters they have
    if not all_unique:
        return 0
        
    ratio = len(common) / len(all_unique)
    
    # 4. Use a "Salt" to make it less predictable
    # We use the length of the names to influence the base score
    length_factor = (len(n1) + len(n2)) % 10
    
    # Generate a score out of 100
    # We use a base of 50 and move up or down based on the ratio
    score = int((ratio * 60) + 30 + length_factor)
    
    # Cap it logically
    return min(max(score, 0), 100)

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