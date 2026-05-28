import re
import sys
from collections import Counter
from pathlib import Path


FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)


def analyze_log(log_path):
    failed_ips = Counter()
    failed_users = Counter()

    with open(log_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                failed_ips[match.group("ip")] += 1
                failed_users[match.group("user")] += 1

    return failed_ips, failed_users


def print_summary(failed_ips, failed_users):
    total_failures = sum(failed_ips.values())

    print("Security Log Analysis")
    print("=====================")
    print(f"Total failed logins: {total_failures}")

    print("\nFailed logins by IP:")
    for ip, count in failed_ips.most_common():
        marker = " <- review" if count >= 3 else ""
        print(f"- {ip}: {count}{marker}")

    print("\nMost targeted usernames:")
    for user, count in failed_users.most_common():
        print(f"- {user}: {count}")

    if not total_failures:
        print("\nNo failed login activity found.")


def main():
    default_log = Path(__file__).with_name("sample_auth.log")
    log_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_log

    if not log_path.exists():
        print(f"Log file not found: {log_path}")
        sys.exit(1)

    failed_ips, failed_users = analyze_log(log_path)
    print_summary(failed_ips, failed_users)


if __name__ == "__main__":
    main()
