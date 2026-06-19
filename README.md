# 🚀 Docker CI/CD Pipeline using GitHub Actions & AWS EC2

This project demonstrates a complete CI/CD pipeline that automatically builds a Docker image, pushes it to Docker Hub, and deploys the latest version to an AWS EC2 instance using GitHub Actions.

---

## 📌 Project Overview

The pipeline performs the following tasks automatically:

1. Checkout the source code from GitHub.
2. Build a Docker image using the Dockerfile.
3. Login to Docker Hub.
4. Tag and push the Docker image to Docker Hub.
5. Connect to an AWS EC2 instance using SSH.
6. Pull the latest Docker image from Docker Hub.
7. Stop and remove the previous running container.
8. Deploy a new container with the latest image.

---

## 🛠️ Technologies Used

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- AWS EC2 (Amazon Linux 2023)
- SSH

---

## 📂 Project Structure

```
.
├── .github
│   └── workflows
│       └── docker-push.yml
├── Dockerfile
├── app.py
└── README.md
```

---

## ⚙️ CI/CD Workflow

```
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
Login to Docker Hub
    │
    ▼
Push Docker Image
    │
    ▼
SSH into AWS EC2
    │
    ▼
Pull Latest Docker Image
    │
    ▼
Stop Previous Container
    │
    ▼
Remove Previous Container
    │
    ▼
Run New Docker Container
```

---

## 🔐 GitHub Secrets & Variables

### Repository Secrets

| Secret | Description |
|---------|-------------|
| DOCKER_TOKEN | Docker Hub Access Token |
| EC2_SSH_KEY | AWS EC2 Private Key (.pem) |
| HOST | EC2 Public IP or DNS |

### Repository Variables

| Variable | Description |
|----------|-------------|
| DOCKER_USERNAME | Docker Hub Username |

---

## 🚀 Docker Commands Used

Build Image

```bash
docker build -t my-python-app .
```

Tag Image

```bash
docker tag my-python-app <dockerhub-username>/my-python-app:latest
```

Push Image

```bash
docker push <dockerhub-username>/my-python-app:latest
```

Pull Image

```bash
docker pull <dockerhub-username>/my-python-app:latest
```

Run Container

```bash
docker run -d --name my-python-app -p 5000:5000 <dockerhub-username>/my-python-app:latest
```

---

## 📖 What I Learned

- GitHub Actions workflow syntax
- GitHub Secrets & Variables
- Docker image creation
- Docker Hub authentication
- Docker image tagging and pushing
- SSH deployment using GitHub Actions
- AWS EC2 deployment
- Docker container lifecycle management
- Building a basic CI/CD pipeline

---

## 🎯 Future Improvements

- Convert the application into a Flask web application
- Use Docker Compose
- Deploy with Nginx
- Implement Kubernetes deployment
- Provision infrastructure using Terraform
- Add automated testing before deployment

---

## 👨‍💻 Author

**Manmeet Kaur**

Infrastructure & DevOps Engineer

GitHub: https://github.com/manmeet14-do
