from flask import Flask, render_template

app = Flask(__name__)

# Accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page Histoire
@app.route('/histoire')
def histoire():
    return render_template('histoire.html')

# Galerie d’images
@app.route('/galerie')
def galerie():
    return render_template('galerie.html')



@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route("/sport")
def sport():
    return render_template("sport.html")

@app.route("/mosque-mahadhra")
def mosque_mahadhra():
    return render_template("mosque_mahadhra.html")


@app.route('/ecole')
def ecole():
    return render_template('ecole.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route("/chieftain")
def chieftain():
    return render_template("chieftain.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
