>  Use ~900 turns of chats from the ShareGPT dataset to evaluate Second Brain

## Setup

- Selected the longest chats from the [ShareGPT dataset](https://huggingface.co/datasets/RyokoAI/ShareGPT52K/tree/main/old) (`sg_90k_part1.json`)
  - ID "7uOhOjo". The chats can be found in: `./sharegpt_test_7uOhOjo.json`
- Ensure you have [set up the Second Brain Backend](../../../src/server/readme.md)
- Run `pip install secondbrain rich`
- We use OpenAI **gpt-4o-mini** as the default model. Make sure you have an OpenAI key and add it to `config.yaml`
- Run `python run.py` (this will take some time) based on the [Quickstart - Second Brain](https://docs.secondbrain.io/quickstart).
- For comparison, we also tested against [mem0](https://github.com/mem0ai/mem0) (version 0.1.2), another great memory layer solution. The code is in `./run_mem0.py`, also using gpt-4o-mini as the default model.
  - Feel free to raise issues about `run_mem0.py`. We wrote this script based on the [quickstart](https://docs.mem0.ai/open-source/quickstart) and it may not follow best practices. However, we kept the Second Brain process as basic as possible for fair comparison.
- To simulate real-world usage, we combine each user+assistant exchange as a single turn when inserting into both Second Brain and Mem0.

## Cost Analysis

- Using `tiktoken` to count tokens (model `gpt-4o`)
- Total tokens in Raw Messages: 63,736 

#### Second Brain

- Estimated costs:
  - Input tokens: ~220,000
  - Output tokens: ~15,000
- Based on OpenAI's Dashboard, 900 turns of chat will cost approximately **$0.042** (LLM costs)
- Complete insertion takes **270-300 seconds** (averaged over 3 tests)

#### Mem0

- Based on OpenAI's Dashboard, 900 turns of chat will cost approximately **$0.24** (LLM) + **<$0.01** (embedding)
- Complete insertion takes **1,683 seconds** (single test)

### Why the Difference?

- Mem0 uses hot-path updates, meaning each update triggers a memory flush. When using Mem0's `Memory.add`, you need to manually manage data insertion to avoid frequent memory flushes. Second Brain includes a buffer zone to handle this automatically.
  - This results in Mem0 making more LLM calls than Second Brain, leading to higher costs and longer processing times.
- Additionally, Mem0 computes embeddings for each memory and retrieves them on every insertion, while Second Brain doesn't use embeddings for user memory. Instead, we use dynamic profiling to generate primary and secondary indices for users, retrieving memories using SQL queries only.

## What will you get?

#### Second Brain

User profile is below (mask sensitive information as **):

```python
* basic_info: language_spoken - User uses both English and Korean.
* basic_info: name - 오*영
* contact_info: email - s****2@cafe24corp.com
* demographics: marital_status - user is married
* education:  - User had an English teacher who emphasized capitalization...
```

You can view the full profile in [here](./full_secondbrain.txt)

Take a look at a more structured profiles:

```python
[
  UserProfile(
      topic='demographics',
      sub_topic='marital_status',
      content='user is married'
      ...
  )
  ...
]
```

#### Mem0

We list some of the memories below(`Memory.get_all`):

```python
- The restaurant is awesome
- User is interested in the lyrics of 'Home Sweet Home' by Motley Crue
- In Korea, people use '^^' to express smile
- Reservation for a birthday party on March 22
- Did not decide the menu...
```

The full results is in [here](./full_mem0.txt).