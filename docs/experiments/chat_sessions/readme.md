# Running Results from multiple chat sessions
This tutorial contains a script to run Second Brain Server on mulitple chat sessions.

## Prepare Data

- You should store your chat data in`./chats/<USER>` folders
- Multiple conversation rounds from the same user are stored as separate json files in `./chats/<USER>/*.json`, with conversation rounds incrementing from 1
    - for example `1.json`, `2.json`, `3.json`..., indicating the 1st, 2nd, 3rd conversation sessions.
- Each json file should be a list of messages, each message is a dictionary with `role` and `content` keys
    - for example:
    ```json
    [
        {"role": "user", "content": "Hello, I'm Ming Ming."},
        {"role": "assistant", "content": "Hi Ming Ming, nice to meet you! Are you a boy or a girl? What are your hobbies?"},
        ...
    ]
    ```

We have a mock user data in `./chats/mock_user/`, you can use it as an example.



## Start Second Brain

- Make sure your [Second Brain Server](../../../src/server/readme.md) is running



## Run the Memory Extraction

```bash
# Python >= 3.11
pip install -r requirements.txt
python extract.py --user <USER>
```
The current profile will be automatically output after each conversation round.

For example, if you're using mock user data with `python extract.py --user mock_user`, the result is something like this:

```
User ID is b4a46c91-cb17-45d7-a7e4-7ed0a6b67925
File: ./chats/mock_user/1.json
Total chats: 6
Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Cost time(s) 2.3378407955169678
* basic_info: gender - girl
* basic_info: name - Ming Ming
* interest: activities - enjoys shopping with friends and buying pretty clothes
* interest: books - enjoys reading novels, especially "Journey to the West"
* interest: movies - likes Sun Wukong for his cleverness and intelligence
File: ./chats/mock_user/2.json
Total chats: 12
Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
Cost time(s) 4.208508014678955
* basic_info: gender - girl
* basic_info: name - Ming Ming
* education: school - user is currently attending school
* health: digestive_issues - user experiences diarrhea from eating watermelon starting in 2025
* interest: activities - enjoys shopping with friends and buying pretty clothes
* interest: books - enjoys reading novels, especially "Journey to the West"
* interest: foods - User does not like cilantro, loves rose pastries, has tried durian mille crepe, and loves watermelon, considering it the greatest of all time (GOAT).
* interest: movies - likes Sun Wukong for his cleverness and intelligence
```

