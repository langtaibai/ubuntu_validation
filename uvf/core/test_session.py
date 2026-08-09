from dataclasses import dataclass, field
from typing import List
from .test_result import TestResult

@dataclass
class TestSession:
    start_time: float =0.0
    end_time: float =0.0
    duration: float =0.0
    total: int =0
    passed: int =0
    failed: int =0
    skipped: int =0
    results: List[TestResult] = field(default_factory=list)