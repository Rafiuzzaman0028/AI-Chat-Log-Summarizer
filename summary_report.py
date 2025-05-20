from touch_chat_summarizer import parse_chat_log
from touch_chat_summarizer import calculate_statistics
from Keyword_analysis import get_common_words
from collections import Counter
def generate_summary(messages, stats, user_common_words, ai_common_words):
    """Generate a formatted summary of the chat."""
    summary = []
    summary.append(f"- The conversation had {stats['total_messages']} exchanges.")

    # Determine nature of conversation based on keywords
    topics = set(word for word, count in user_common_words[:3])
    summary.append(f"- The user asked mainly about {', '.join(topics)}.")

    # Combine all common words
    all_common_words = user_common_words + ai_common_words
    combined_words = Counter()
    for word, count in all_common_words:
        combined_words[word] += count

    top_keywords = [word for word, count in combined_words.most_common(5)]
    summary.append(f"- Most common keywords: {', '.join(top_keywords)}.")

    return "\n".join(summary)


def main():
    file_path = "sample_chat.txt"
    messages = parse_chat_log(file_path)
    stats = calculate_statistics(messages)
    user_common_words = get_common_words(messages["user"])
    ai_common_words = get_common_words(messages["ai"])

    summary = generate_summary(messages, stats, user_common_words, ai_common_words)

    print("\n=== Chat Summary ===")
    print(summary)


if __name__ == "__main__":
    main()