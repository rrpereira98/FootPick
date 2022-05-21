from flask import Flask, render_template
import fifa_team_picker

app = Flask(__name__)

@app.route("/")
def index():
    tee = fifa_team_picker.teams_picker()
    badge1 = tee[0][0]
    badge2 = tee[1][0]
    return render_template("index.html", team1 = tee[0][0], team2 = tee[1][0], badge1 = badge1, badge2 = badge2)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")