# AI-Powered Job Recommender System

## Overview

The AI-Powered Job Recommender System is an intelligent career recommendation platform that leverages Generative AI and Large Language Models (LLMs) to provide personalized job suggestions based on a user's resume and skill set.

The system analyzes uploaded resumes, extracts relevant information, identifies skill gaps, generates a professional profile summary, and recommends suitable job opportunities from multiple job platforms. It also provides a personalized roadmap to help users improve their skills and enhance their career prospects.

---

## Features

### Resume Analysis

* Extracts text from PDF resumes.
* Analyzes candidate qualifications and experience.
* Generates a concise professional profile summary.

### AI-Powered Recommendations

* Uses TinyLlama running locally through Ollama.
* Provides personalized job recommendations.
* Matches user skills with relevant job opportunities.

### Skill Gap Analysis

* Identifies missing skills required for desired roles.
* Highlights areas for improvement.

### Career Roadmap Generation

* Suggests learning paths and future career development plans.
* Provides actionable recommendations for skill enhancement.

### Real-Time Job Fetching

* Integrates with job platforms such as:

  * LinkedIn
  * Naukri
* Retrieves relevant job listings based on extracted resume keywords.

### User-Friendly Interface

* Built using Streamlit.
* Interactive and easy-to-use web interface.
* Displays recommendations, summaries, and career insights in real time.

---

## Technology Stack

### Artificial Intelligence

* TinyLlama
* Ollama

### Backend

* Python

### Frontend

* Streamlit

### APIs

* LinkedIn Job API
* Naukri Job API

### Data Processing

* PDF Text Extraction
* Natural Language Processing (NLP)

---

## System Workflow

1. User uploads a resume in PDF format.
2. The system extracts text from the resume.
3. TinyLlama analyzes the resume content.
4. The AI generates:

   * Profile Summary
   * Skill Gap Analysis
   * Career Improvement Roadmap
   * Resume Keywords
5. Extracted keywords are used to fetch relevant jobs from LinkedIn and Naukri.
6. Recommended jobs and career insights are displayed through the Streamlit interface.

---

## Project Architecture

```text
Resume PDF
     │
     ▼
Text Extraction
     │
     ▼
TinyLlama (Ollama)
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
Summary  Skill Gaps  Roadmap
     │
     ▼
Keyword Extraction
     │
 ┌───┴───────────────┐
 ▼                   ▼
LinkedIn API     Naukri API
     │
     ▼
Recommended Jobs
     │
     ▼
Streamlit Dashboard
```

---
## Screenshots

### 🔐 User Login

![Login Page](screenshots/Login%20Page.png)

### ⏳ Resume Processing

![Loading Stage](screenshots/Loading%20Stage.png)

### 📝 AI Generated Resume Summary

![Resume Summary](screenshots/Resume%20Summary.png)

### 🔑 Extracted Resume Keywords

![Extracted Keywords](screenshots/Extracted%20Keywords.png)

### 📊 Skill Gap Analysis

![Skill Gaps and Missing Areas](screenshots/Skill%20Gaps%20and%20Missing%20Area.png)

### 🚀 Personalized Career Roadmap

![Future Road Map](screenshots/Futrue%20Road%20Map.png)

### 💼 LinkedIn Job Recommendations

![LinkedIn Job Recommendations](screenshots/LinkedIn%20Job%20Recommendation.png)

### 🌐 Naukri Job Recommendations

![Naukri Job Recommendations](screenshots/Naukri%20Job%20Recommendation.png)
----
## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Job-Recommender.git
cd AI-Powered-Job-Recommender
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from:

https://ollama.com

### Run TinyLlama

```bash
ollama pull tinyllama
ollama run tinyllama
```

### Start Streamlit Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Advanced Resume Parsing
* Multiple LLM Support (Llama 3, Mistral, Gemma)
* Resume Scoring System
* ATS Compatibility Analysis
* Course Recommendations
* Interview Preparation Assistant
* Job Application Tracking Dashboard
* User Authentication and Profile Management

---

## Learning Outcomes

This project demonstrates:

* Generative AI Application Development
* Large Language Model Integration
* Prompt Engineering
* Resume Analysis using NLP
* API Integration
* Streamlit Web Development
* Local LLM Deployment using Ollama
* End-to-End AI Product Development

---

## License

This project is developed for academic and educational purposes.
