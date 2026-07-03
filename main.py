from tests.boot_test import BootTest
#from tests.test_system import TestSystem

def main():
    # tester = TestSystem()
    # tester.connect()
    # tester.check_system_status()
    # tester.collect_journal()
    # tester.disconnect
    boot = BootTest()
    boot.connect()
    result= boot.run()
    boot.disconnect()
    print(result)
if __name__ == "__main__":
    main()
