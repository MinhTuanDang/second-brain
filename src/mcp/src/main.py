from mcp.server.fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from dotenv import load_dotenv
from secondbrain import AsyncSecondBrainClient, ChatBlob
from secondbrain.utils import string_to_uuid
import asyncio
import json
import os

from utils import get_secondbrain_client

load_dotenv()

# Default user ID for memory operations
DEFAULT_USER_ID = string_to_uuid("user")


# Create a dataclass for our application context
@dataclass
class SecondBrainContext:
    """Context for the Second Brain MCP server."""

    secondbrain_client: AsyncSecondBrainClient


@asynccontextmanager
async def secondbrain_lifespan(server: FastMCP) -> AsyncIterator[SecondBrainContext]:
    """
    Manages the Second Brain client lifecycle.

    Args:
        server: The FastMCP server instance

    Yields:
        SecondBrainContext: The context containing the Second Brain client
    """
    # Create and return the Memory client with the helper function in utils.py
    secondbrain_client = get_secondbrain_client()
    assert await secondbrain_client.ping(), "Failed to connect to Second Brain"
    print("Second Brain client connected")
    try:
        yield SecondBrainContext(secondbrain_client=secondbrain_client)
    finally:
        # No explicit cleanup needed for the Second Brain client
        pass


# Initialize FastMCP server with the Second Brain client as context
mcp = FastMCP(
    "secondbrain-mcp",
    description="MCP server for long term memory storage and retrieval with Second Brain",
    lifespan=secondbrain_lifespan,
    host=os.getenv("HOST", "0.0.0.0"),
    port=os.getenv("PORT", 8050),
)


@mcp.tool()
async def save_memory(ctx: Context, text: str) -> str:
    """Save information to your long-term memory.

    This tool is designed to store any type of information that might be useful in the future.
    The content will be processed and indexed for later retrieval through semantic search.

    Args:
        ctx: The MCP server provided context which includes the Second Brain client
        text: The content to store in memory, including any relevant details and context
    """
    try:
        secondbrain_client: AsyncSecondBrainClient = (
            ctx.request_context.lifespan_context.secondbrain_client
        )
        messages = [{"role": "user", "content": text}]
        u = await secondbrain_client.get_or_create_user(DEFAULT_USER_ID)
        await u.insert(ChatBlob(messages=messages))
        await u.flush()
        return f"Successfully saved memory: {text[:100]}..."
    except Exception as e:
        return f"Error saving memory: {str(e)}"


@mcp.tool()
async def get_user_profiles(ctx: Context) -> str:
    """Get full user profiles.

    Call this tool when user asks for a summary of complete image of itself.

    Args:
        ctx: The MCP server provided context which includes the Second Brain client

    Returns:
        A list of user profiles with topic, subtopic and content.
    """
    try:
        secondbrain_client: AsyncSecondBrainClient = (
            ctx.request_context.lifespan_context.secondbrain_client
        )
        u = await secondbrain_client.get_or_create_user(DEFAULT_USER_ID)
        ps = await u.profile()
        return "\n".join([f"- {p.describe}" for p in ps])
    except Exception as e:
        return f"Error retrieving memories: {str(e)}"


@mcp.tool()
async def search_memories(ctx: Context, query: str, max_length: int = 1000) -> str:
    """Search user memories

    Call this tool when user ask for recall some personal information.

    Args:
        ctx: The MCP server provided context which includes the Second Brain client
        query: Search query string describing what you're looking for. Can be natural language.
        max_length: Maximum content length of the returned context.
    """
    try:
        secondbrain_client: AsyncSecondBrainClient = (
            ctx.request_context.lifespan_context.secondbrain_client
        )
        u = await secondbrain_client.get_or_create_user(DEFAULT_USER_ID)
        ps = await u.context(
            chats=[{"role": "user", "content": query}], max_token_size=max_length
        )
        return ps
    except Exception as e:
        return f"Error searching memories: {str(e)}"


async def main():
    transport = os.getenv("TRANSPORT", "sse")
    if transport == "sse":
        # Run the MCP server with sse transport
        await mcp.run_sse_async()
    else:
        # Run the MCP server with stdio transport
        await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
