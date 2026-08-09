import json

from rich.diagnose import report

from reporters.base_reporter import BaseReporter

class JsonReporter(BaseReporter):
    def generate(self, session):
        report ={
            "summary": {
                "total": session.total,
                "passed": session.passed,
                "failed": session.failed,
                "skipped": session.skipped,
                "duration": session.duration,
            },
            "result": []
        }
        for r in session.results:
            report["result"].append({
                "name": r.name,
                "status": r.status.value,
                "duration": r.duration,
                "message": r.message
            })
        with open(
            "report.json",
            "w"
        ) as f:
            json.dump(
                report,
                f,
                indent=4,
            )
