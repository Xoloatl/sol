conversation_memory = []

def remember(user_message, sol_response):
    conversation_memory.append({
        "user": user_message,
        "sol": sol_response
    })

    # Keep memory short for now
    if len(conversation_memory) > 10:
        conversation_memory.pop(0)

def get_recent_memory():
    return conversation_memory