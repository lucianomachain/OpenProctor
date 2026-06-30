from flask import Flask, request, jsonify

app = Flask(__name__)

# logs simples en memoria (solo demo)
logs = []
suspicion_score = {}

@app.route("/")
def home():
    return """
    <h2>OpenProctor ✔</h2>

    <p>Activá cámara y mantené la pestaña abierta</p>

    <video id="video" autoplay playsinline style="width:400px;"></video>

    <p id="status">Estado: iniciando...</p>

    <script>
        const video = document.getElementById("video");
        const status = document.getElementById("status");

        let frameCount = 0;

        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
        .then(stream => {
            video.srcObject = stream;
            status.innerText = "Cámara activa ✔";

            // Enviar "frames" simulados cada 3 segundos
            setInterval(() => {
                frameCount++;

                fetch("/frame", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({ frame: frameCount })
                });

            }, 3000);

        })
        .catch(err => {
            status.innerText = "❌ No se pudo acceder a la cámara";
            console.error(err);
        });

        // DETECCIÓN DE CAMBIO DE PESTAÑA
        document.addEventListener("visibilitychange", () => {
            if (document.hidden) {
                fetch("/tab", { method: "POST" });
            }
        });

    </script>

    <br><br>

    <a href="https://forms.gle/TU_EXAMEN_REAL" target="_blank">
        👉 Abrir examen
    </a>
    """


# =========================
# BACKEND DE EVENTOS
# =========================

@app.route("/frame", methods=["POST"])
def frame():
    data = request.get_json()

    suspicion_score["frames"] = suspicion_score.get("frames", 0) + 1
    logs.append("frame recibido")

    # alerta simple
    if suspicion_score["frames"] % 10 == 0:
        logs.append("⚠ actividad continua detectada")

    return jsonify({"ok": True})


@app.route("/tab", methods=["POST"])
def tab():
    suspicion_score["tab_switch"] = suspicion_score.get("tab_switch", 0) + 1
    logs.append("⚠ cambio de pestaña detectado")

    return jsonify({"ok": True})


@app.route("/logs")
def get_logs():
    return jsonify({
        "logs": logs,
        "suspicion_score": suspicion_score
    })


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
