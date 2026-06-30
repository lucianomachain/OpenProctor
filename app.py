from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>OpenProctor ✔</h2>
    <p>Sistema activo</p>
    <a href='https://forms.gle/tu-examen' target='_blank'>
        Abrir examen
    </a>
    """

@app.route("/status")
def status():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
