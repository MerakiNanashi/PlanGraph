from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.core.schema import GlobalState, Input, ExtractorOutput, CandidateOutput, Query, Constraint, ClusterOutput, Candidate


T = TypeVar("T")


class BaseExtractor(
    ABC,
    Generic[T]
):

    def __init__(
        self,
        d_schema: type[T],
        f_schema: type[ExtractorOutput[T]] = ExtractorOutput,
    ):
        self.d_schema = d_schema
        self.f_schema = f_schema

        # schema sent to Gemini
        self.llm_schema = self.build_schema()

        # raw parsed Gemini response
        self.response: dict | None = None

    # --------------------------------------------------
    # Schema Construction
    # --------------------------------------------------

    def build_schema(self) -> dict:
        schema = self.get_base_schema()
        schema = self.remove_runtime_fields(schema)
        schema = self.apply_custom_schema_rules(schema)

        return schema

    def get_base_schema(self) -> dict:

        return self.f_schema[
            self.d_schema
        ].model_json_schema()

    def remove_runtime_fields(
        self,
        schema: dict,
    ) -> dict:

        runtime_fields = ["run_id",]

        for field in runtime_fields:
            schema.get("properties", {}, ) \
            .pop(
                field,
                None,
            )

            required = schema.get("required",[],)

            if field in required:
                required.remove(
                    field
                )

        return schema

    def apply_custom_schema_rules(
        self,
        schema: dict,
    ) -> dict:
        return schema

    # --------------------------------------------------
    # LLM
    # --------------------------------------------------

    @abstractmethod
    async def call_llm(
        self,
        prompt: str,
    ) -> dict:
        pass

    @abstractmethod
    def build_prompt(
        self,
        user_input: Input,
    ) -> str:
        pass

    # --------------------------------------------------
    # Parsing
    # --------------------------------------------------

    def parse_response(
        self,
        response: dict,
    ) -> dict:
        self.response = response
        return response

    # --------------------------------------------------
    # Runtime Resolution
    # --------------------------------------------------

    def finalize(
        self,
        run_id: str,
    ) -> ExtractorOutput[T]:

        if self.response is None:
            raise ValueError(
                "No response available"
            )

        return self.f_schema[
            self.d_schema
        ](
            run_id=run_id,
            **self.response,
        )

    # --------------------------------------------------
    # Main Flow
    # --------------------------------------------------

    async def main(
        self,
        user_input: Input,
    ) -> ExtractorOutput[T]:

        prompt = self.build_prompt(
            user_input
        )

        raw_response = (
            await self.call_llm(
                prompt
            )
        )

        self.parse_response(
            raw_response
        )

        return self.finalize(
            user_input.run_id
        )

    # --------------------------------------------------
    # External API
    # --------------------------------------------------

    @abstractmethod
    async def extract(
        self,
        user_input: Input,
    ) -> ExtractorOutput[T]:
        pass

