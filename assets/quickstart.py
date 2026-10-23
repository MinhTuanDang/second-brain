from rich import print
from secondbrain import SecondBrainClient, ChatBlob

PROJECT_URL = "http://localhost:8019"
PROJECT_TOKEN = "secret"

client = SecondBrainClient(
    project_url=PROJECT_URL,
    api_key=PROJECT_TOKEN,
)

assert client.ping(), "Your Second Brain server is not running"

messages = [
    {
        "role": "user",
        "content": "Hello, I'm Gus",
        "created_at": "2025-01-14",
    },
    {
        "role": "assistant",
        "content": "Hi, nice to meet you, Gus!",
        "alias": "HerAI",
    },
]

blob = ChatBlob(messages=messages)


uid = client.add_user()
u = client.get_user(uid)

bid = u.insert(blob)
print("User ID is", uid)
print("Blob ID is", bid)

print("Start processing...")
u.flush(sync=True)


print("\n--------------\nBelow is your profile:")
print(u.profile(need_json=True))


print("\n--------------\nYou can use Second Brain Event to recent details of the user:")
for e in u.event():
    print("📅", e.created_at.astimezone().strftime("%Y-%m-%d %H:%M:%S"))
    for i in e.event_data.profile_delta:
        print(
            "-", i.attributes["topic"], i.attributes["sub_topic"], i.content, sep="::"
        )

print(
    "\n--------------\nYou can use Second Brain Context to get a memory prompt and insert it into your prompt:"
)
print(
    f"""```
{u.context()}
```
"""
)
