import argparse
import os
import json
from rich.progress import track
from time import time
from secondbrain import SecondBrainClient, ChatBlob
from httpx import Client
from rich import print as pprint

USER = "user1"
parser = argparse.ArgumentParser()
parser.add_argument("--user", type=str, default=USER)
parser.add_argument("-u", "--project_url", type=str, default="http://localhost:8019")
parser.add_argument("-t", "--project_token", type=str, default="secret")

args = parser.parse_args()
USER = args.user
PROJECT_URL = args.project_url
PROJECT_TOKEN = args.project_token

client = SecondBrainClient(
    project_url=PROJECT_URL,
    api_key=PROJECT_TOKEN,
)
hclient = Client(
    base_url=PROJECT_URL, headers={"Authorization": f"Bearer {PROJECT_TOKEN}"}
)

total_files = sorted(os.listdir(f"./chats/{USER}"))
total_files = [t for t in total_files if t.endswith(".json")]
sessions = []
for i in total_files:
    with open(f"./chats/{USER}/{i}") as f:
        messages = json.load(f)
    sessions.append({"file": f"./chats/{USER}/{i}", "messages": messages})
uid = client.add_user()
print("User ID is", uid)
u = client.get_user(uid)

for session in sessions:
    messages = session["messages"]
    blobs = [
        ChatBlob(
            messages=messages[i : i + 2],
        )
        for i in range(0, len(messages), 2)
    ]

    print("File:", session["file"])
    print("Total chats:", len(blobs))

    start = time()
    for index, blob in track(enumerate(blobs), total=len(blobs)):
        u.insert(blob, sync=True)
    u.flush(sync=True)
    print("Cost time(s)", time() - start)

    prompts = [m.describe for m in u.profile()]
    print("* " + "\n* ".join(sorted(prompts)))
    # pprint(hclient.get(f"/api/v1/users/event/{uid}").json()["data"]["events"])
