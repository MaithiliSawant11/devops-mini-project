from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>DevOps Mini Project</title>
        <style>
          body { font-family: Arial, sans-serif; max-width: 760px; margin: 60px auto;
                 padding: 0 20px; background: #f4f7fb; color: #172033; }
          main { background: white; padding: 32px; border-radius: 14px;
                 box-shadow: 0 8px 28px #17203318; }
          h1 { color: #175cd3; }
          .status { display: inline-block; padding: 8px 12px; border-radius: 20px;
                    background: #dcfae6; color: #067647; font-weight: bold; }
        </style>
      </head>
      <body>
        <main>
          <h1>DevOps Mini Project</h1>
          <p>Our DevOps pipeline is working successfully.</p>
          <p class="status">Application Status: OK</p>
          <p>Pipeline stages: Code → Test → Docker Build → Verify</p>
        </main>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
