from flask import Flask, render_template

app = Flask(__name__)


@app.route('/DjXazuk')
def home_gen():
    return render_template('Home.html')


@app.route('/SocialNetwork')
def social_gen():
    return render_template('SocialNetwork.html')


@app.route('/Team')
def team_gen():
    return render_template('XBandaTeam.html')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
