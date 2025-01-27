# logs_processor.py
def detect_intrusions(logs: list) -> int:
    """
    Recibe una lista de 'logs' (strings) y retorna la
    cantidad de líneas que podrían ser sospechosas.
    """
    suspicious_keywords = ["intrusion", "attack", "malware"]
    count_suspicious = 0
    for line in logs:
        for keyword in suspicious_keywords:
            if keyword in line.lower():
                count_suspicious += 1
                break
    return count_suspicious

if __name__ == "__main__":
    sample_logs = [
        "User admin logged in",
        "Possible intrusion detected from IP 192.168.1.10",
        "Network scanner found suspicious traffic",
        "System normal",
        "Malware signature matched"
    ]
    suspicious_count = detect_intrusions(sample_logs)
    print(f"Suspicious logs found: {suspicious_count}")
