from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>OpenProctor ✔</h2>

    <p>Activá cámara para supervisión</p>

    <video id="video" autoplay playsinline style="width:400px;"></video>

    <p id="status">Estado: esperando cámara...</p>

    <br>
    <a href="https://forms.gle/tu-examen" target="_blank">
        👉 Abrir examen
    </a>

    <script>
        const video = document.getElementById("video");
        const status = document.getElementById("status");

        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
        .then(stream => {
            video.srcObject = stream;
            status.innerText = "Cámara activa ✔";
        })
        .catch(err => {
            status.innerText = "❌ No se pudo acceder a la cámara";
        });

        // "heartbeat" simple al backend
        setInterval(() => {
            fetch("/ping", {method: "POST"});
        }, 5000);
    </script>
    """

@app.route("/ping", methods=["POST"])
def ping():
    return jsonify({"ok": True})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
