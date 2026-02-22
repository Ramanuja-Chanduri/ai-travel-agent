# AI Travel Agent

A Streamlit web app that generates personalized day-trip itineraries using LangChain and a Groq-hosted LLM.

## Features

- Enter a destination city and your interests (e.g. art, food, history)
- Receive a concise, AI-generated bulleted itinerary tailored to your preferences
- Powered by LangChain and Groq

## Requirements

- Python 3.11+
- A [Groq API key](https://console.groq.com/)

## Setup

1. **Clone the repository and install dependencies:**
   ```bash
   pip install -e .
   ```

2. **Create a `.env` file in the project root:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   LLM_MODEL=openai/gpt-oss-20b   # optional, this is the default
   ```

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

## Docker

```bash
docker build -t ai-travel-agent .
docker run -p 8501:8501 --env-file .env ai-travel-agent
```

## Kubernetes

```bash
kubectl apply -f k8s-deploy.yaml
kubectl apply -f k8s-service.yaml
```

## Project Structure

```
main.py                  # Streamlit entry point
src/
  core/planner.py        # TravelPlanner orchestrator
  chains/iternary_chain.py  # LangChain + Groq LLM chain
  config/config.py       # Environment-based configuration
  utils/                 # Logger and custom exceptions
```
