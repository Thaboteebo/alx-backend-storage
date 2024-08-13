#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
    """Provides statistics about Nginx logs stored in MongoDB."""
    client = MongoClient('')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DETELE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __namw__ == "__main__":
    log_stats()
