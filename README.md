# 🎥 YouTube Sentiment Analyzer

An AI-powered full-stack web application that analyzes the sentiments of comments on YouTube videos. Users can log in, submit a video link or ID, and receive a breakdown of sentiments (positive, negative, neutral) for each comment along with aggregate metrics. It also tracks sentiment analysis history per user.

---

## 🌟 Project Vision

In the era of digital opinion shaping, understanding public sentiment is crucial. This project aims to provide a simple and powerful tool to:

- Gauge the audience sentiment for any YouTube video.
- Enable content creators, brands, and researchers to analyze viewer reactions.
- Offer historical tracking and statistics for authenticated users.

---

## 🧩 Architecture Overview

    ┌────────────────────┐
    │    React Frontend  │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │    FastAPI Backend │
    │ (Python + JWT + AI)│
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │   PostgreSQL DB    │
    │  (Docker container)│
    └────────────────────┘

- Communication: RESTful APIs with JSON
- Authentication: JWT-based
- Deployment: Docker
- Sentiment Analysis: Pre-trained NLP model

---

## 🧠 Features Breakdown

| Category        | Feature                                                   |
|----------------|------------------------------------------------------------|
| 🧠 Sentiment AI | Classifies YouTube comments as **Positive**, **Neutral**, or **Negative** |
| 🔐 Auth         | JWT-based registration and login system                   |
| 🎬 Video Input  | Accepts public YouTube video IDs                          |
| 📊 Dashboard    | Real-time feedback with pie charts, comment lists, and overall video rating |
| 🕓 History      | Logged-in users can view past analyses                    |
| 🗃️ Persistence  | Stores user history, video IDs, timestamps, and results in PostgreSQL |
| 🌐 Responsive   | Mobile-friendly                    |

---

## 🔧 Technologies Used

### Frontend (React)
- React 18+
- Tailwind CSS + Heroicons
- Axios (API calls)
- JWT token handling
- React Router
- Chart libraries (Recharts, Chart.js, etc.)

### Backend (FastAPI)
- Python 3.11+
- FastAPI + Uvicorn
- SQLAlchemy (ORM)
- Pydantic (schema validation)
- PostgreSQL (via Docker)
- JWT Auth (PyJWT or fastapi-jwt-auth)
- dotenv for configuration
- Sentiment Analysis (VADER or Transformers)

### Infrastructure
- Docker + Docker Compose
- PostgreSQL (in container)
- .env configuration
- Deployment: Docker

---

## ⚙️ Setup Instructions

### 🔃 Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer
```

### 🔑 Create Environment Variables
#### Inside backend/.env:

```bash
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=database_name

DATABASE_URL=postgresql://postgres_user:postgres_password@postgres:5432/database_name

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

YOUTUBE_API_KEY=your_youtube_api
```

### 🐳 Dockerized Setup (Recommended)

```bash
docker-compose up --build
```

### 🧪 Local Development

#### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run start
```
---

### 📚 API Documentation


#### Key Endpoints

| Method |	Endpoint	 | Description                         |
|--------|-------------|----------------------------------|
| POST	 |     /signup |	Register a new user               |
| POST	 |    /login   |	Authenticate and return JWT token |
| GET	   | /analyze    |	Submit a YouTube video ID for analysis|
| GET	   | /history	   | Get the user’s sentiment history      |

---

### 🚀 Future Enhancements
🔎 Add keyword-based sentiment filtering

🌍 Support multi-language comments

🗣️ Voice-to-text comment ingestion

📊 Admin dashboard for global trends

🧠 Upgrade model to Transformer-based sentiment classifier

📲 Mobile App version (React Native)

---

### 🙋 Contact
#### Built with ❤️ by Harshit Saini
#### 📧 Email: sainiharshit322@gmail.com
