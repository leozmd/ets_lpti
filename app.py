from flask import Flask, render_template, session, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        res = "hola"
    else:
        if 'user' in session:
            res = redirect(url_for('zonas'))

        else:
            res = render_template("index.html")
    return res


@app.route('/zonas')
def zonas():
    if 'user' in session:
        res = render_template("zonas.html")
    else:
        res = redirect(url_for('index'))
    return res


@app.route('/autos')
def autos():
    if 'user' in session:
        res = render_template("pedir_autos.html")
    else:
        res = redirect(url_for('index'))
    return res

@app.route('/personal')
def personal():
    if 'user' in session:
        res = render_template("nvo_personal.html")
    else:
        res = redirect(url_for('index'))
    return res

@app.route('/sucursal')
def sucursal():
    if 'user' in session:
        res = render_template("nva_sucursal.html")
    else:
        res = redirect(url_for('index'))
    return res

@app.route('/factura')
def factura():
    if 'user' in session:
        res = render_template("nva_factura.html")
    else:
        res = redirect(url_for('index'))
    return res

if __name__ == '__main__':
    app.run()
