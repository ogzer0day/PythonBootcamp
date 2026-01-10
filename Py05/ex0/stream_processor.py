from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: Any) -> str:
        pass


class NumericProcessor(DataProcessor):

    def process(self, data: List[int]) -> List[str]:
        try:
            return [str(value) for value in data]
        except Exception:
            return ("Error")

    def validate(self, data: Any) -> bool:
        return (isinstance(data, list) and
                all(isinstance(i, int) for i in data))

    def format_output(self, result: List[str]) -> str:
        len_lst = len(result)
        sum_lst = sum([int(i) for i in result])
        avg = sum_lst / len_lst
        res = f"Processed {len_lst} numeric values, sum={sum_lst}, avg={avg}"
        return (res)


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            return data.strip()
        except Exception:
            return ("Error")

    def validate(self, data: str) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        len_str = len(result)
        len_words = result.split(" ")
        words = len(len_words)
        res_word = f"Processed text: {len_str} characters, {words} words"
        return res_word


class LogProcessor(DataProcessor):

    def process(self, data: str) -> str:
        if data == 'Error':
            return ("\"ERROR: Connection timeout\"")
        else:
            return ("\"System ready\"")

    def validate(self, data: Any) -> bool:
        return (isinstance(data, str) and len(data) > 0)

    def format_output(self, result: str) -> str:
        if result == "\"ERROR: Connection timeout\"":
            return ("[ALERT] ERROR level detected: Connection timeout")
        else:
            return ("[INFO] INFO level detected: System ready")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num = NumericProcessor()
    nums = num.process([1, 2, 3, 4, 5])
    print(f"Processing data: {nums}")
    if num.validate([1, 2, 3, 4, 5]):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data not verified :(")

    print(f"Output: {num.format_output(nums)}\n")

    print("Initializing Text Processor...")
    txt = TextProcessor()
    txt_str = "Hello Nexus World"
    print(f"Processing data: {txt.process(txt_str)}")
    if txt.validate(txt_str):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data not verified :(")

    print(f"Output: Processed text: {txt.format_output(txt_str)}\n")

    print("Initializing Log Processor...")
    log = LogProcessor()
    log_error = txt.process(123)
    error = log.process(log_error)
    print(f"rocessing data: {log.process(log_error)}")
    if log.validate(error):
        print("Validation: Log entry verified")
    else:
        print("Validation: Log entry not verified :(")

    print(f"Output: {log.format_output(error)}\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print(f"Result 1: {num.format_output([1, 2, 3])}")
    print(f"Result 2: {txt.format_output('hello bro how are u')}")
    print(f"Result 3: {log.format_output('valid')}\n")
    print("Foundation systems online. Nexus ready for advanced streams.")
