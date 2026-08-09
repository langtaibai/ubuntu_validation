import json

from rich.diagnose import report

from reporters.base_reporter import BaseReporter

class JsonReporter(BaseReporter):
    def generate(self, results):
        report = []
        for result in results:
            report.append({
                "name": result.name,
                "status": result.status,
                "duration": result.duration,
                "message": result.message,
            })
        with open("report.json", "w") as f:
            json.dump(
                report,
                f,
                indent=4
            )
