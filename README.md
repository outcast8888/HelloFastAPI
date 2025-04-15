# 🚀 HelloFastAPI

A simple, production-ready FastAPI app with CI/CD, code coverage, and EC2 deployment.

![Python](https://img.shields.io/badge/python-3.10-blue)
![CI](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/ci.yml?label=CI)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📡 Live Demo & Source

- 🌐 App: [http://52.205.110.60](http://52.205.110.60/)
- 🗂️ GitHub: [HelloFastAPI](https://github.com/outcast8888/HelloFastAPI)

---


## ✅ Features

- FastAPI application with `/` and `/ping` routes
- Containerized using Docker
- CI/CD pipelines with GitHub Actions:
  - Runs tests on every push/PR
  - Enforces code coverage
  - Auto-deploys to EC2 when main branch passes CI
- Deployed on: `http://<your-ec2-public-ip>`

---

## 📁 Project Structure

```
HelloFastAPI/
├── app/                # FastAPI app
├── tests/              # Unit tests
├── Dockerfile          # Docker build file
├── .github/workflows/  # CI/CD pipeline
├── requirements.txt    # Python dependencies
├── pytest.ini          # Pytest config
└── README.md
```

---

## 🧪 Run Tests

```bash
pytest --cov=app --cov-report=term --cov-report=html tests/
```

---

## 🐳 Docker

```bash
docker build -t hello-fastapi .
docker run -d -p 80:8000 hello-fastapi
```

---

## 🔁 CI/CD Automation

- ✅ On **push to `main`**:
  - CI runs tests and code coverage
  - CD uploads app to EC2 via SSH
  - Rebuilds Docker image
  - Restarts FastAPI container

---

## ⚙️ Run Locally

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🛡️ Security & Delivery

- `.pem` keys and secrets are **not stored** in repo
- `.gitignore` includes:
  - `venv/`
  - `.pytest_cache/`
  - `ec2-user@*`
- GitHub Actions securely connects using encrypted secrets

---

## 📦 Final Checklist

- ✅ CI/CD works on `main`
- ✅ Coverage enforced
- ✅ Deployment tested on EC2
- ✅ Repo ready for public delivery
- ✅ Other repos set to private

---

## 📄 License

MIT © 2024

