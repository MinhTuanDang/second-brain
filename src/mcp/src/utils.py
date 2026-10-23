from secondbrain import AsyncSecondBrainClient
import os


def get_secondbrain_client():
    client = AsyncSecondBrainClient(
        project_url=os.getenv("SECONDBRAIN_BASE_URL"),
        api_key=os.getenv("SECONDBRAIN_API_KEY"),
    )
    return client
