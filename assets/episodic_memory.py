from secondbrain import SecondBrainClient, ChatBlob

PROJECT_URL = "http://localhost:8019"
PROJECT_TOKEN = "secret"

client = SecondBrainClient(
    project_url=PROJECT_URL,
    api_key=PROJECT_TOKEN,
)

assert client.ping(), "Your Second Brain server is not running"
uid = client.add_user()
u = client.get_user(uid)
print("User ID is", uid)

print("Start processing...")
messages1 = [
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

blob = ChatBlob(messages=messages1)
bid = u.insert(blob)
u.flush(sync=True)

messages2 = [
    {
        "role": "user",
        "content": "My name is Tom now.",
    },
]

blob = ChatBlob(messages=messages2)
bid = u.insert(blob)
u.flush(sync=True)


events = u.event()

print("Below is recent memories:")
for e in events:
    print("-----------------")
    print("📅", e.created_at.astimezone().strftime("%Y-%m-%d %H:%M:%S"))
    for i in e.event_data.profile_delta:
        print("-", i.attributes["topic"], i.attributes["sub_topic"], i.content)
    print("-----------------")
