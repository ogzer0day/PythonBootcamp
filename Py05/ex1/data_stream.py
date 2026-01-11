from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str, count: int):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.count = count

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
 
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        pass

    def  get_stats(self) -> Dict[str, Union[str, int, float]]:
        return (
            {
                "stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "count": self.count
            }
            )



class SensorStream(DataStream):
    def __init__(self, stream_id, stream_type, count, avg_temp):
        super().__init__(stream_id, stream_type, count)
        self.avg_temp = avg_temp

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count = sum([1 for _ in data_batch[0].values()])
        new_lst = [f"{key}: {val}" for key, val in data_batch[0].items()]
        readable_str = str(new_lst).replace("'", "")
        self.avg_temp = sum([val for val in data_batch[0].values()]) / self.count

        return f"Processing sensor batch: {readable_str}"
 
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:


class TransactionStream(DataStream):
    def __init__(self, stream_id, stream_type, net_flow):
        super().__init__(stream_id, stream_type)
        self.net_flow = net_flow

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count = sum([1 for _ in data_batch[0].values()])
        new_lst = [f"{key}: {val}" for key, val in data_batch[0].items()]
        readable_str = str(new_lst).replace("'" ,"")
        self.net_flow = sum(-val if key == "buy" else val
                    for key, val in data_batch[0].items()
                    )
        return f"Processing sensor batch: {readable_str}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

class EventStream(DataStream):
    def __init__(self, stream_id, stream_type, ):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count = sum([1 for _ in data_batch[0].values()])
        readable_str = str(data_batch).replace("'" ,"")
        return f"Processing sensor batch: {readable_str}"
 
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        

class StreamProcessor():



if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")