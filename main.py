from tests.test_system import TestSystem

def main():
    tester = TestSystem()
    tester.connect()
    tester.check_system_status()
    tester.collect_journal()
    tester.disconnect()
if __name__ == "__main__":
    main()
