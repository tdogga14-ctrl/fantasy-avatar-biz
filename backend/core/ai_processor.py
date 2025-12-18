import replicate
from backend.app.config import settings

class TieredModelRouter:
    def __init__(self):
        self.replicate = replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

    async def run_ai_task(self, image_url, style):
        output = await self.replicate.run(
            "black-forest-labs/flux-2-pro",
            input={
                "image": image_url,
                "prompt": f"professional headshot, {style}, high quality",
            }
        )
        return output