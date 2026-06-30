from flask import Flask

app = Flask(__name__)

GOOGLE_FORM_URL = "https://forms.gle/tu-examen"

@app.route("/")
def home():
    return f"""
    <h2>OpenProctor activo ✔</h2>
    <p>1. Permitir cámara</p>
    <p>2. Abrir examen:</p>
    <a href="{GOOGLE_FORM_URL}" target="_blank">Ir al examen</a>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
