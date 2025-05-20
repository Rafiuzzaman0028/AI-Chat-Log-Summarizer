import os
import re
from collections import Counter
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
import argparse

# Define stop words
STOP_WORDS = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
              'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
              'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their'}


def parse_chat_log(file_path):
    """Parse chat log file into user and AI messages"""
    user_msgs = []
    ai_msgs = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("User:"):
                user_msgs.append(line[6:])  # Remove "User: " prefix
            elif line.startswith("AI:"):
                ai_msgs.append(line[4:])  # Remove "AI: " prefix
    return {'user': user_msgs, 'ai': ai_msgs}


def process_chat_log(file_path, use_tfidf=False):
    """Process a single chat log file"""
    messages = parse_chat_log(file_path)

    # Get statistics
    stats = {
        'total': len(messages['user']) + len(messages['ai']),
        'user': len(messages['user']),
        'ai': len(messages['ai'])
    }

    # Get keywords
    if use_tfidf:
        def get_keywords(msgs):
            vectorizer = TfidfVectorizer(stop_words=list(STOP_WORDS))
            tfidf = vectorizer.fit_transform([' '.join(msgs)])
            return list(zip(vectorizer.get_feature_names_out(),
                            tfidf.toarray()[0]))

        user_kw = get_keywords(messages['user'])
        ai_kw = get_keywords(messages['ai'])
    else:
        def get_keywords(msgs):
            words = ' '.join(msgs).lower().split()
            words = [w.strip(punctuation) for w in words
                     if w not in STOP_WORDS and len(w) > 2]
            return Counter(words).most_common(5)

        user_kw = get_keywords(messages['user'])
        ai_kw = get_keywords(messages['ai'])

    # Generate summary
    summary = [
        f"Total messages: {stats['total']}",
        f"User messages: {stats['user']}",
        f"AI messages: {stats['ai']}",
        "Top user keywords: " + ', '.join([w[0] for w in user_kw]),
        "Top AI keywords: " + ', '.join([w[0] for w in ai_kw])
    ]

    return {
        'file': file_path,
        'stats': stats,
        'user_keywords': user_kw,
        'ai_keywords': ai_kw,
        'summary': '\n'.join(summary)
    }


def main():
    parser = argparse.ArgumentParser(description="AI Chat Log Summarizer")
    parser.add_argument('input', help="Path to chat log file or directory")
    parser.add_argument('--tfidf', action='store_true', help="Use TF-IDF analysis")
    args = parser.parse_args()

    if os.path.isfile(args.input):
        result = process_chat_log(args.input, args.tfidf)
        print("\n=== Analysis Results ===")
        print(result['summary'])
    elif os.path.isdir(args.input):
        print("Directory processing not implemented in this example")
    else:
        print(f"Error: {args.input} is not a valid file or directory")


if __name__ == "__main__":
    main()