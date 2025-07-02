import csv
from datetime import datetime
import os

CSV_FILE = "generated_replies.csv"

async def save_to_csv(platform: str, post_text: str, reply: str):
    # If file doesn't exist, write header
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "platform", "post_text", "generated_reply"])
        writer.writerow([
            datetime.utcnow().isoformat(),
            platform,
            post_text,
            reply
        ])
