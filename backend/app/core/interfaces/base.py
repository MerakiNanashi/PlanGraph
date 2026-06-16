from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.core.schema import GlobalState, Input, ExtractorOutput, CandidateOutput, Query, Constraint, ClusterOutput, Candidate


T = TypeVar("T")


class BaseStage(ABC):
    name: str

    @abstractmethod
    def run(
        self,
        state: GlobalState
    ) -> GlobalState:
        pass

class BaseWorkflow(ABC):
    domain: str
    stages: list[type[BaseStage]]

    def run(
        self,
        state: GlobalState
    ) -> GlobalState:

        for stage in self.stages:
            state = stage().run(state)

        return state
    

class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        constraints: list[Constraint],
        queries: list[Query]
    ) -> CandidateOutput:
        pass

class BaseAgent(ABC):
    agent_name: str

    @abstractmethod
    def execute(
        self,
        state: GlobalState
    ) -> GlobalState:
        pass

class BaseCluster(ABC):

    @abstractmethod
    def cluster(
            self,
            candidates: list[Candidate]
    ) -> ClusterOutput:
        pass