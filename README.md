# 🚀 Docker CI/CD Pipeline with GitHub Actions & AWS EC2

## 📌 Project Overview

This project demonstrates a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, **Docker Hub**, and **AWS EC2**.

Whenever code is pushed to the GitHub repository, GitHub Actions automatically:

* Builds a Docker image
* Pushes the image to Docker Hub
* Connects to an AWS EC2 instance using SSH
* Pulls the latest Docker image
* Replaces the existing container with the new version

The application is built using **Python Flask** and runs inside a Docker container.

---

# 🛠️ Technologies Used

* Git
* GitHub
* GitHub Actions
* Docker
* Docker Hub
* Python
* Flask
* AWS EC2
* Linux (Amazon Linux 2023)

---

# 📂 Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── docker-push.yml
├── templates/
│   └── index.html
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🔄 CI/CD Workflow

```text
Developer
      │
      ▼
Git Push
      │
      ▼
GitHub Actions
      │
      ▼
Checkout Repository
      │
      ▼
Build Docker Image
      │
      ▼
Docker Hub Login
      │
      ▼
Push Image to Docker Hub
      │
      ▼
SSH into AWS EC2
      │
      ▼
Docker Pull Latest Image
      │
      ▼
Stop Existing Container
      │
      ▼
Remove Existing Container
      │
      ▼
Run New Docker Container
```

---

# ⚙️ GitHub Actions Features Used

* Workflow Dispatch
* Jobs
* Steps
* GitHub Secrets
* GitHub Variables
* Docker Login Action
* Appleboy SSH Action
* Docker Build
* Docker Push
* Docker Pull
* Automated Deployment

---

# 🔐 GitHub Secrets

The following secrets are configured:

| Secret       | Purpose                 |
| ------------ | ----------------------- |
| DOCKER_TOKEN | Docker Hub Access Token |
| HOST         | AWS EC2 Public IP/DNS   |
| EC2_SSH_KEY  | Private SSH Key         |

---

# 🌐 GitHub Variables

| Variable        | Purpose             |
| --------------- | ------------------- |
| DOCKER_USERNAME | Docker Hub Username |

---

# ▶️ Run the Project Locally

### Clone Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Build Docker Image

```bash
docker build -t my-python-app .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 my-python-app
```

Open your browser:

http://localhost:5000
🚀 Deployment

Deployment is fully automated using GitHub Actions.

Every successful workflow execution:

Builds a new Docker image
Pushes it to Docker Hub
Deploys the latest image to AWS EC2

No manual deployment is required.

📸 Application

The Flask application displays a simple web page showing:

DevOps CI/CD Pipeline
Deployment Successful
Technologies Used
CI/CD Workflow
📚 Skills Demonstrated
CI/CD Pipeline
GitHub Actions
Docker Containerization
Docker Hub Image Registry
AWS EC2 Deployment
SSH Automation
Linux Administration
Flask Web Application
👩‍💻 Author

Manmeet Kaur

DevOps Engineer | RHCSA Certified

⭐ Future Improvements
Add Docker Compose
Configure Nginx Reverse Proxy
Add HTTPS with SSL
Deploy using Kubernetes
Build Infrastructure with Terraform
Add Monitoring using Prometheus & Grafana
