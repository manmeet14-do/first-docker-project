from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 DevOps CI/CD Pipeline</h1>
    <p>Application deployed successfully!</p>

    <h3>Project Details</h3>
    <ul>
        <li>✅ GitHub Actions CI/CD</li>
        <li>✅ Docker</li>
        <li>✅ Docker Hub</li>
        <li>✅ AWS EC2</li>
        <li>✅ Flask Application</li>
    </ul>

    <p><b>Author:</b> Manmeet Kaur</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
