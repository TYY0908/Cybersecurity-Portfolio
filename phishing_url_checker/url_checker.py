import re
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = {
    "account",
    "bank",
    "confirm",
    "free",
    "gift",
    "login",
    "password",
    "secure",
    "update",
    "verify",
}


def check_url(url):
    parsed = urlparse(url if "://" in url else f"http://{url}")
    hostname = parsed.hostname or ""
    findings = []

    if parsed.scheme != "https":
        findings.append("URL does not use HTTPS.")

    if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", hostname):
        findings.append("URL uses an IP address instead of a domain name.")

    keyword_hits = [keyword for keyword in SUSPICIOUS_KEYWORDS if keyword in url.lower()]
    if keyword_hits:
        findings.append(f"Suspicious keyword found: {', '.join(sorted(keyword_hits))}.")

    if len(url) > 90:
        findings.append("URL is unusually long.")

    if hostname.count("-") >= 2:
        findings.append("Domain contains multiple hyphens.")

    if url.count("@") > 0:
        findings.append("URL contains @, which can hide the real destination.")

    if len(findings) >= 4:
        risk = "High"
    elif len(findings) >= 2:
        risk = "Medium"
    else:
        risk = "Low"

    return risk, findings


def main():
    url = input("Enter URL to check: ").strip()
    risk, findings = check_url(url)

    print(f"\nRisk rating: {risk}")

    if findings:
        print("\nFindings:")
        for finding in findings:
            print(f"- {finding}")
    else:
        print("No obvious phishing indicators found.")


if __name__ == "__main__":
    main()
