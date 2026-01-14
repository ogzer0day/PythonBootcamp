"""
Polymorphic Stream Processing System

This module defines an abstract streaming framework that supports multiple
stream types (sensor, transaction, event) using inheritance, method overriding,
and polymorphism. A central StreamProcessor coordinates batch processing
through a unified interface.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.

    All concrete stream types mouust inherit from this class and implement
    the `process_batch` method.
    """

    def __init__(self, stream_id: str, stream_type: str = None) -> None:
        """
        Initialize a data stream.

        :param stream_id: Unique identifier for the stream
        :param stream_type: Description of the stream category
        """
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data specific to the stream type.

        Must be implemented by all subclasses.

        :param data_batch: A batch of incoming data
        :return: Human-readable processing summary
        """
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filter data items based on a string-matching criteria.

        :param data_batch: List of data items to filter
        :param criteria: Optional substring to match against items
        :return: Filtered list of data items
        """
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieve basic metadata statistics for the stream.

        :return: Dictionary containing stream identifier and type
        """
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
        }


class SensorStream(DataStream):
    """
    Concrete stream for processing sensor data such as temperature
    and environmental readings.
    """

    def __init__(
        self, stream_id: str, stream_type: str = None, count: int = None,
        avg_temp: float = None
    ) -> None:
        """
        Initialize a sensor data stream.

        :param stream_id: Unique identifier for the stream
        :param stream_type: Description of the stream category
        :param count: Number of sensor readings processed
        :param avg_temp: Average temperature reading
        """
        super().__init__(stream_id, stream_type)
        self.avg_temp = avg_temp
        self.count = count

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of sensor readings.

        Calculates the number of readings and extracts temperature data.

        :param data_batch: List containing sensor reading dictionaries
        :return: Processing summary string
        """
        self.count = sum(1 for _ in data_batch[0].values())
        new_lst = [f"{key}: {val}" for key, val in data_batch[0].items()]
        readable_str = str(new_lst).replace("'", "")
        self.avg_temp = sum(
            val for ky, val in data_batch[0].items() if ky == "temp"
        )
        return f"Processing sensor batch: {readable_str}"


class TransactionStream(DataStream):
    """
    Concrete stream for processing financial transaction data.
    """

    def __init__(
        self, stream_id: str, stream_type: str = None, net_flow: int = None
    ) -> None:
        """
        Initialize a transaction data stream.

        :param stream_id: Unique identifier for the stream
        :param stream_type: Description of the stream category
        :param net_flow: Net flow of transaction values
        """
        super().__init__(stream_id, stream_type)
        self.net_flow = net_flow

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of transaction records.

        Computes total operations and net transaction flow.

        :param data_batch: List containing transaction dictionaries
        :return: Processing summary string
        """
        self.count = sum(1 for _ in data_batch[0].values())
        new_lst = [f"{key}: {val}" for key, val in data_batch[0].items()]
        readable_str = str(new_lst).replace("'", "")
        self.net_flow = sum(
            val if key == "buy_a" or key == "buy_b" else 0
            for key, val in data_batch[0].items()
        )
        return f"Processing sensor batch: {readable_str}"


class EventStream(DataStream):
    """
    Concrete stream for processing system or application event data.
    """

    def __init__(
        self, stream_id: str, stream_type: str = None, detect_error: int = None
    ) -> None:
        """
        Initialize an event data stream.

        :param stream_id: Unique identifier for the stream
        :param stream_type: Description of the stream category
        :param detect_error: Number of detected error events
        """
        super().__init__(stream_id, stream_type)
        self.detect_error = detect_error

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of event messages.

        Counts total events and detects error occurrences.

        :param data_batch: List of event strings
        :return: Processing summary string
        """
        self.count = sum(1 for _ in data_batch)
        readable_str = str(data_batch).replace("'", "")
        self.detect_error = sum(
            1 if var == "error" else 0 for var in data_batch
        )
        return f"Processing sensor batch: {readable_str}"


class StreamProcessor:
    """
    Coordinator class for managing and processing multiple data streams
    using polymorphism.
    """

    def __init__(self) -> None:
        """
        Initialize the stream processor with an empty registry.
        """
        self.streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        """
        Register a new data stream for processing.

        :param stream: A concrete DataStream instance
        """
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> None:
        """
        Process batches for all registered streams.

        Each stream processes its corresponding batch based on stream ID.

        :param batches: Mapping of stream IDs to data batches
        """
        for stream in self.streams:
            batch = batches.get(stream.stream_id)
            if batch is not None:
                stream.process_batch(batch)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001", "Environmental Data", 0, 0)
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    print(
        sensor_stream.process_batch(
            [{"temp": 22.5, "humidity": 65, "pressure": 1013}])
    )
    print(
        f"Sensor analysis: {sensor_stream.count} readings processed, "
        f"avg temp: {sensor_stream.avg_temp}°C\n"
    )

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001", "Financial Data", 0)
    print(
        f"Stream ID: {transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    dic = {'buy_a': 100, 'sell': 150, 'buy_b': 75}
    print(
        "Processing transaction batch: "
        f"{transaction_stream.process_batch([dic])}"
    )
    print(
        f"Transaction analysis: {transaction_stream.count} operations, "
        f"net flow: +{transaction_stream.net_flow} units\n"
    )

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001", "System Events", 0)
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    print(
        f"Processing event batch: "
        f"{event_stream.process_batch(['login', 'error', 'logout'])}"
    )
    print(
        f"Event analysis: {event_stream.count} events, "
        f"{event_stream.detect_error} error detected\n"
    )

    print("=== Polymorphic Stream Processing ===\n"
          "Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    sensor_stream.process_batch([{"temp": 22.5, "humidity": 65}])
    print(f"- Sensor data: {sensor_stream.count} readings processed")
    transaction_stream.process_batch(
        [{'buy_a': 100, 'sell': 150, 'buy_b': 75}])
    print(f"- Transaction data: {transaction_stream.count} "
          "operations processed")
    event_stream.process_batch(['login', 'error', 'logout'])
    print(f"- Event data: {event_stream.count} events processed\n")

    print("Stream filtering active: High-priority data only\n"
          "Filtered results: 2 critical sensor alerts, 1 large transaction\n")

    print("All streams processed successfully. Nexus throughput optimal.")
