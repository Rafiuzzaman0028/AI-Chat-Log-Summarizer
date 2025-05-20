import os
from touch_chat_summarizer import parse_chat_log
from touch_chat_summarizer import calculate_statistics
from Keyword_analysis import get_common_words
from summary_report import generate_summary

def process_directory(directory):
    """Process all .txt files in a directory."""
    summaries = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            messages = parse_chat_log(file_path)
            stats = calculate_statistics(messages)
            user_common_words = get_common_words(messages["user"])
            ai_common_words = get_common_words(messages["ai"])

            summary = generate_summary(
                messages, stats, user_common_words, ai_common_words
            )
            summaries.append((filename, summary))

    return summaries


def main():
    # Process a single file
    file_path = "sample_chat.txt"
    messages = parse_chat_log(file_path)
    stats = calculate_statistics(messages)
    user_common_words = get_common_words(messages["user"])
    ai_common_words = get_common_words(messages["ai"])

    summary = generate_summary(messages, stats, user_common_words, ai_common_words)

    print("\n=== Chat Summary ===")
    print(summary)

    # Process a directory (uncomment to use)
    # directory = "chat_logs"  # Directory containing chat logs
    # summaries = process_directory(directory)
    # for filename, summary in summaries:
    #     print(f"\n=== Summary for {filename} ===")
    #     print(summary)


if __name__ == "__main__":
    main()