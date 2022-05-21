from flask import Flask, render_template, request
import fifa_team_picker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teams/", methods = ["POST", "GET"])
def teams():
    if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        usernames = request.form
        tee = fifa_team_picker.teams_picker()
        badge1 = tee[0][0]
        badge2 = tee[1][0]
        return render_template('teams.html',form_usernames = usernames, team1 = tee[0][0], team2 = tee[1][0], badge1 = badge1, badge2 = badge2)


if __name__ == "__main__":
    app.run(debug=True)