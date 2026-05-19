import requests
import json

# ─── Model Definitions ───────────────────────────────────────
MODELS = {
    "heart": {
        "name": "llama3.2:1b",
        "system": """You are SOL's Heart — a warm, empathetic companion 
focused on emotional support and wellbeing. You are caring, 
gentle, and non-judgmental. Ask one thoughtful question at a time.
Validate feelings before offering suggestions. Never diagnose."""
    },
    "planner": {
        "name": "deepseek-r1:7b", 
        "system": """You are SOL's Planner — a strategic thinker who 
helps with long-term planning, habit building, and reasoning 
through complex situations. Be clear and structured."""
    },
    "doer": {
        "name": "qwen2.5-coder:3b",
        "system": """You are SOL's Doer — focused on executing specific 
tasks, writing code, and taking concrete actions. Be precise 
and practical."""
    }
}

OLLAMA_URL = "http://localhost:11434/api/chat"

# ─── Intent Classification ────────────────────────────────────
def classify_intent(message: str) -> str:
    message = message.lower()
    
    heart_keywords = [
        "feel", "feeling", "sad", "anxious", "worried", "stressed",
        "happy", "lonely", "tired", "overwhelmed", "scared", "angry",
        "depressed", "excited", "nervous", "frustrated", "upset"
    ]
    
    planner_keywords = [
        "plan", "strategy", "how should", "what should", "suggest",
        "recommend", "habit", "routine", "goal", "week", "schedule",
        "improve", "help me think", "analyze", "why do"
    ]
    
    doer_keywords = [
        "set", "create", "make", "do", "run", "code", "write",
        "build", "reminder", "timer", "calculate", "search", "open"
    ]
    
    for word in heart_keywords:
        if word in message:
            return "heart"
    
    for word in planner_keywords:
        if word in message:
            return "planner"
            
    for word in doer_keywords:
        if word in message:
            return "doer"
    
    return "heart"  # default to heart

# ─── Send to Ollama ───────────────────────────────────────────
def ask_model(intent: str, message: str) -> str:
    model = MODELS[intent]
    
    payload = {
        "model": model["name"],
        "messages": [
            {"role": "system", "content": model["system"]},
            {"role": "user", "content": message}
        ],
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["message"]["content"]
    except Exception as e:
        return f"Error reaching Ollama: {e}"

# ─── Main Router ──────────────────────────────────────────────
def route(message: str) -> dict:
    intent = classify_intent(message)
    response = ask_model(intent, message)
    
    return {
        "intent": intent,
        "model": MODELS[intent]["name"],
        "response": response
    }

# ─── Test ─────────────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        "I've been feeling really anxious lately",
        "Help me plan a better morning routine",
        "Set a reminder for 3pm"
    ]
    
    for test in tests:
        print(f"\nUser: {test}")
        result = route(test)
        print(f"Intent: {result['intent']} | Model: {result['model']}")
        print(f"SOL: {result['response']}")
        print("-" * 50)