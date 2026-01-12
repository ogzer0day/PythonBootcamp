from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        


class InputStage:
    def process(self, data: Any) -> Dict:
        

class TransformStage:
    def process(self, data: Dict) -> Dict:
        


class OutputStage:
    def process(self, data: Dict) -> str:
       


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
       

    def process(self, data: Any) -> Any:
       


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id



class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_all(self, data: Any) -> List[Any]:
        