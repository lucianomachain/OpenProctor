from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>OpenProctor ✔</h2>

    <p>1. Activá la cámara</p>

    <video id="video" autoplay playsinline></video>

    <script>
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            document.getElementById('video').srcObject = stream;
        })
        .catch(err => {
            alert("No se pudo acceder a la cámara");
        });
    </script>

    <br><br>
    <a href='https://forms.gle/tu-examen' target='_blank'>
        Abrir examen
    </a>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
