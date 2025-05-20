import argparse
import os
from multiple_file_optional import process_directory
from comple_version import process_chat_log

def main():
    parser = argparse.ArgumentParser(description="AI Chat Log Summarizer")
    parser.add_argument('input', type=str, help="Path to chat log file or directory containing chat logs")
    parser.add_argument('--tfidf', action='store_true', help="Use TF-IDF for keyword extraction")

    args = parser.parse_args()

    if os.path.isfile(args.input):
        # Process single file
        result = process_chat_log(args.input, args.tfidf)
        print("\n=== Chat Summary ===")
        print(result['summary'])
    elif os.path.isdir(args.input):
        # Process directory
        results = process_directory(args.input, args.tfidf)
        display_results(results)
    else:
        print(f"Error: {args.input} is not a valid file or directory.")


if __name__ == "__main__":
    main()