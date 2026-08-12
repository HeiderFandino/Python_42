import sys


def score_analytics() -> None:
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    for argv in sys.argv[1:]:
        try:
            score = int(argv)
            scores += [score]
        except ValueError:
            print(f"Invalid parameter: '{argv}'")
    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total_player = len(scores)
    total_score = sum(scores)
    average_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_player}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    score_analytics()
