from flask import Flask, render_template, redirect, session, request, url_for

app = Flask(__name__)
app.secret_key = "notsosure"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# ===================== FINAL BATTLE LOGIC =====================

def final_battle(with_eleven):
    health = session["health"]
    allies = session["allies"]

    if with_eleven and allies.get("Eleven") and health > 30:
        session["ending"] = "best"

    elif health > 20:
        session["health"] -= 30
        if session["health"] < 0:
            session["health"] = 0
        session["ending"] = "neutral"

    else:
        session["health"] -= 50
        if session["health"] < 0:
            session["health"] = 0
        session["ending"] = "bad"


# ===================== GAME START =====================

@app.route("/", methods=["GET", "POST"])
def home():
    if "health" not in session:
        session["health"] = 100
        session["allies"] = {
            "Friends": False,
            "Eleven": False
        }
        print(f"DEBUG: Session initialized, health={session['health']}")

    if request.method == "POST":
        choice = request.form.get("choice")
        print(f"DEBUG: Before choice, health={session['health']}")

        if choice == "one":
            session["health"] -= 20
            if session["health"] < 0:
                session["health"] = 0
            print(f"DEBUG: After 'ignore it', health={session['health']}")
            return redirect("/room_encounter")

        elif choice == "two":
            session["health"] -= 30
            if session["health"] < 0:
                session["health"] = 0
            print(f"DEBUG: After 'go outside', health={session['health']}")
            return redirect("/demo_encounter")

        else:
            session["allies"]["Friends"] = True
            print(f"DEBUG: After 'call friends', health={session['health']}")
            return redirect("/call_friends")

    return render_template(
        "home.html",
        health=session["health"],
        bg_image=url_for("static", filename="images/d&d.jpg")
    )


# ===================== STORY ROUTES =====================

@app.route("/room_encounter", methods=["GET", "POST"])
def room_encounter():
    if request.method == "POST":
        return redirect("/scene2")
    return render_template("room_encounter.html", health=session["health"])


@app.route("/demo_encounter", methods=["GET", "POST"])
def demo_encounter():
    if request.method == "POST":
        return redirect("/scene2")
    return render_template("demo_encounter.html", health=session["health"])


@app.route("/call_friends", methods=["GET", "POST"])
def call_friends():
    if request.method == "POST":
        return redirect("/room_encounter")
    return render_template("call_friends.html", health=session["health"])


@app.route("/scene2", methods=["GET", "POST"])
def scene2():
    if request.method == "POST":
        return redirect("/scene_dustin_place")
    return render_template("scene2.html", health=session["health"])


@app.route("/scene_dustin_place", methods=["GET", "POST"])
def scene_dustin_place():
    if request.method == "POST":
        return redirect("/scene3")
    return render_template("scene_dustin_place.html", health=session["health"])


@app.route("/scene3", methods=["GET", "POST"])
def scene3():
    if request.method == "POST":
        return redirect("/meetstrange")
    return render_template("scene3.html", health=session["health"])


@app.route("/meetstrange", methods=["GET", "POST"])
def meetstrange():
    if request.method == "POST":
        choice = request.form.get("choice")
        print(f"DEBUG: meetstrange choice={choice}")
        if choice == "one":
            session["allies"]["Eleven"] = True
            session.modified = True
            print("DEBUG: Eleven added to allies!")
        else:
            print("DEBUG: Eleven NOT added.")
        return redirect("/scene4")

    return render_template("meetstrange.html", health=session["health"])


# ===================== FINAL CHOICE =====================

@app.route("/scene4", methods=["GET", "POST"])
def scene4():


    if request.method == "POST":
        choice = request.form.get("choice")
        print(f"DEBUG: choice={choice}, Eleven={session['allies']['Eleven']}, health={session['health']}")
        print(f"DEBUG: session={dict(session)}")

        if choice == "one":
            if session["allies"]["Eleven"]:
                print("DEBUG: Going to final_battle with_eleven=True")
                final_battle(with_eleven=True)
            else:
                print("DEBUG: Going to final_battle with_eleven=False (no Eleven)")
                final_battle(with_eleven=False)
        else:
            print("DEBUG: Going to final_battle with_eleven=False (let Eleven fight alone)")
            final_battle(with_eleven=False)

        print(f"DEBUG: ending={session.get('ending')}")
        return redirect("/ending")

    return render_template(
        "scene4.html",
        health=session["health"],
        allies=session["allies"]
    )


# ===================== ENDING =====================

@app.route("/ending")
def ending():
    return render_template(
        "ending.html",
        ending=session.get("ending", "bad"),
        health=session["health"],
        allies=session["allies"]
    )


@app.route("/restart")
def restart():
    session.clear()
    session["health"] = 100
    session["allies"] = {
        "Friends": False,
        "Eleven": False
    }
    return redirect("/")


# ===================== RUN =====================

if __name__ == "__main__":
    app.run(debug=True)
