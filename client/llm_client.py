from openai import AsyncOpenAI

class LLMClient:
    def __init__(self) -> None: 
        self._client : AsyncOpenAI | None = None

    def get_client(self)->AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                apiKey="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", 
                base_url="https://openrouter.ai/api/v1"
            )
        return self._client
    
    async def close(self)->None:
        if self._client:
            await self._client.close()
            self._client = None