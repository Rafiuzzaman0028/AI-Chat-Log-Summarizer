# chat_summarizer.py

def parse_chat_log(file_path):
    """
    Parse the chat log file and separate messages by speaker.
    Returns a dictionary with user and AI messages.
    """
    user_messages = []
    ai_messages = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line[len("User: "):])
            elif line.startswith("AI:"):
                ai_messages.append(line[len("AI: "):])

    return {
        "user": user_messages,
        "ai": ai_messages
    }


def calculate_statistics(messages):
    """
    Calculate basic statistics from the parsed messages.
    Returns a dictionary with counts.
    """
    return {
        "total_messages": len(messages["user"]) + len(messages["ai"]),
        "user_messages": len(messages["user"]),
        "ai_messages": len(messages["ai"])
    }


def main():
    file_path = "sample_chat.txt"
    messages = parse_chat_log(file_path)
    stats = calculate_statistics(messages)

    print("Chat Statistics:")
    print(f"- Total messages: {stats['total_messages']}")
    print(f"- User messages: {stats['user_messages']}")
    print(f"- AI messages: {stats['ai_messages']}")


if __name__ == "__main__":
    main()
