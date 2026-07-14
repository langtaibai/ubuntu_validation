from dataclasses import dataclass

@dataclass
class TestResult:
    name: str
    status: str
    duration: float
    message: str