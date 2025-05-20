from collections import Counter
import re
from string import punctuation
from touch_chat_summarizer import parse_chat_log
from touch_chat_summarizer import calculate_statistics
# Common English stop words
STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
    'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
    'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
    'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
    'will', 'just', 'don', 'should', 'now'
}


def preprocess_text(text):
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(f'[{punctuation}]', '', text)
    return text


def get_common_words(messages, top_n=5):
    """Extract the most common words from all messages."""
    all_text = ' '.join(messages)
    words = preprocess_text(all_text).split()

    # Filter out stop words and short words
    filtered_words = [
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_n)


def main():
    file_path = "sample_chat.txt"
    messages = parse_chat_log(file_path)
    stats = calculate_statistics(messages)

    # Get common words from user messages
    user_common_words = get_common_words(messages["user"])
    ai_common_words = get_common_words(messages["ai"])

    print("\nChat Statistics:")
    print(f"- Total messages: {stats['total_messages']}")
    print(f"- User messages: {stats['user_messages']}")
    print(f"- AI messages: {stats['ai_messages']}")

    print("\nMost Common User Words:")
    for word, count in user_common_words:
        print(f"- {word}: {count}")

    print("\nMost Common AI Words:")
    for word, count in ai_common_words:
        print(f"- {word}: {count}")


if __name__ == "__main__":
    main()