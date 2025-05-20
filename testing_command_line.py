import argparse
import os
from touch_chat_summarizer import parse_chat_log
from touch_chat_summarizer import calculate_statistics
from compl
def main():
    parser = argparse.ArgumentParser(
        description="AI Chat Log Summarizer - Analyze and summarize chat logs."
    )
    parser.add_argument(
        "input",
        help="Path to a chat log file or directory containing chat logs"
    )
    parser.add_argument(
        "--tfidf",
        action="store_true",
        help="Use TF-IDF for keyword extraction"
    )

    args = parser.parse_args()

    if os.path.isfile(args.input):
        # Process single file
        messages = parse_chat_log(args.input)
        stats = calculate_statistics(messages)

        if args.tfidf:
            user_keywords = get_tfidf_keywords(messages["user"])
            ai_keywords = get_tfidf_keywords(messages["ai"])
        else:
            user_keywords = get_common_words(messages["user"])
            ai_keywords = get_common_words(messages["ai"])

        summary = generate_summary(messages, stats, user_keywords, ai_keywords)
        print("\n=== Chat Summary ===")
        print(summary)

    elif os.path.isdir(args.input):
        # Process directory
        summaries = process_directory(args.input)
        for filename, summary in summaries:
            print(f"\n=== Summary for {filename} ===")
            print(summary)
    else:
        print(f"Error: {args.input} is not a valid file or directory.")


if __name__ == "__main__":
    main()