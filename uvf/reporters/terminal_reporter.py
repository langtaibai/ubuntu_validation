from reporters.base_reporter import BaseReporter

class TerminalReporter(BaseReporter):
    def generate(self, session):
        print("=" * 50)
        print("UVF Test Report")
        print("=" * 50)
        for result in session.results:
            print(
                f"{result.status:6}"
                f"{result.name:25}"
                f"{result.duration:.2f}s"
            )
        print("----------------------")
        print(f"Total: {session.total}")
        print(f"PASS:  {session.passed}")
        print(f"FAIL: {session.failed}")
        print(f"SKIP: {session.skipped}")
        print(f"Duration: {session.duration: .2f}")


