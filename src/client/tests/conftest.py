import pytest
from secondbrain import SecondBrainClient, AsyncSecondBrainClient
from secondbrain.error import ServerError


@pytest.fixture(scope="session")
def api_client():
    client = SecondBrainClient(
        project_url="http://localhost:8019/",
        api_key="secret",
    )
    if not client.ping():
        return pytest.skip("API not available")
    return client


@pytest.fixture(scope="session")
def api_async_client():
    client = AsyncSecondBrainClient(
        project_url="http://localhost:8019/",
        api_key="secret",
    )
    # if not await client.ping():
    #     return pytest.skip("API not available")
    return client
