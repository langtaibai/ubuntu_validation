from dataclasses import dataclass
from uvf.core.status import Teststatus

@dataclass
class TestResult:
    name: str
    status: Teststatus
    duration: float
    message: str=""