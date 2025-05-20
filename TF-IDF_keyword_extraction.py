from sklearn.feature_extraction.text import TfidfVectorizer
from touch_chat_summarizer import calculate_statistics
from Keyword_analysis import get_common_words
from touch_chat_summarizer import parse_chat_log

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

def get_tfidf_keywords(messages, top_n=5):
    """Extract keywords using TF-IDF."""
    # Combine all messages into a single string per speaker
    combined_text = [' '.join(messages)]

    vectorizer = TfidfVectorizer(stop_words=list(STOP_WORDS), max_features=100)
    tfidf_matrix = vectorizer.fit_transform(combined_text)

    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]

    # Pair feature names with their TF-IDF scores
    word_scores = list(zip(feature_names, tfidf_scores))

    # Sort by score in descending order
    word_scores.sort(key=lambda x: x[1], reverse=True)

    return word_scores[:top_n]


def main():
    file_path = "sample_chat.txt"
    messages = parse_chat_log(file_path)
    stats = calculate_statistics(messages)

    # Get common words using both methods
    user_common_words = get_common_words(messages["user"])
    user_tfidf_words = get_tfidf_keywords(messages["user"])

    print("\nUser Message Analysis:")
    print("Most frequent words:")
    for word, count in user_common_words:
        print(f"- {word}: {count}")

    print("\nTF-IDF keywords:")
    for word, score in user_tfidf_words:
        print(f"- {word}: {score:.2f}")


if __name__ == "__main__":
    main()