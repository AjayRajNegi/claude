from typing import Any
from openai import AsyncOpenAI

class LLMClient:
    def __init__(self) -> None: 
        self._client : AsyncOpenAI | None = None

    def get_client(self)->AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                api_key="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", 
                base_url="https://openrouter.ai/api/v1"
            )
        return self._client
    
    async def close(self)->None:
        if self._client:
            await self._client.close()
            self._client = None

    async def chat_completion(self, messages: list[dict[str, Any]], stream:bool=True):

        client = self.get_client()
        kwargs={
            "model":"nvidia/nemotron-3-nano-30b-a3b:free",
            "messages":messages,
            "stream":stream
        }
        if stream:
            await self._stream_response(client, kwargs)
        else:
            await self._non_stream_response(client, kwargs)

    async def _stream_response(self):
        pass

    async def _non_stream_response(self, client:AsyncOpenAI, kwargs: dict[str, Any]):
        response = await client.chat.completions.create(**kwargs)
        print(response)