from app.config.config import *
from app.core.schema import *
from app.core.interfaces.base import *
from app.core.utils import retry, measure_latency
from app.core.llm.endpoints import gemini_ep
from app.core.interfaces.base_extractor import *
import json

# Define domain specific schema
class Query(BaseModel):
    query: str
    constraints: list[Constraint] = Field(
        default_factory=list
    )

class TravelExtractorOp(BaseModel):
    dest: str
    stay: str | None = None
    days: int = Field(default=3)
    budget: float
    international: bool = Field(default=True)
    queries: list[Query] = Field(
        default_factory=list
    )

config = read_config(CONFIG_PATH)

# -------------------------------------
# Extractor
# -------------------------------------

class TravelExtractor(
    BaseExtractor[TravelExtractorOp]
):

    def __init__(self):

        super().__init__(
            d_schema=TravelExtractorOp,
            f_schema=ExtractorOutput
        )
    
    def build_prompt(self, user_input):
        prompt = f'''
        You're a extractor. Extract the fields for the following input:

        {user_input}
        '''
        return prompt

    @measure_latency()
    @retry()
    async def extract(
        self,
        user_input: Input,
    ) -> ExtractorOutput[
        TravelExtractorOp
    ]:
        try:
            gemini_response = await gemini_ep(
                api_key=GEMINI_API_KEY,
                prompt=user_input.input,
                config=config,
                response_schema=self.llm_schema,
            )

            # store parsed response
            self.response = gemini_response

            # runtime resolution
            return self.finalize(
                run_id=user_input.run_id
            )

        except Exception:
            raise

    async def main(
        self,
        user_input: Input,
    ) -> ExtractorOutput[
        TravelExtractorOp
    ]:

        return await self.extract(
            user_input
        )
    
class RetreivalFlow():
    pass
class ConstructorFlow():
    pass

TravelWorkFlow = [
    TravelExtractor,
    RetreivalFlow,
    ConstructorFlow
]