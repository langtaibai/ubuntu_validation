from unittest import result

from uvf.tests.boot_test import BootTest
#from tests.test_system import TestSystem
from uvf.core.ssh_client import SSHClient
from uvf.config.config import load_config
from uvf.core.test_runner import TestRunner
# config = load_config()
# ssh = SSHClient(
#     host=config["host"],
#     user=config["user"],
#     password=config["password"]
# )
# ssh.connect()
# boot = BootTest(ssh)
# result = boot.run()
# print(result)
# ssh.close()

# def main():
#     # tester = TestSystem()
#     # tester.connect()
#     # tester.check_system_status()
#     # tester.collect_journal()
#     # tester.disconnect
#     boot = BootTest()
#     boot.connect()
#     result= boot.run()
#     boot.disconnect()
#     print(result)
# if __name__ == "__main__":
#     main()

def main():
    config = load_config()
    ssh = SSHClient(
        host=config["host"],
        user=config["user"],
        password=config["password"]
    )
    ssh.connect()

    #create runner
    runner = TestRunner(ssh)
    #add test
    #runner.add_test(BootTest(ssh))
    #discovery test case
    runner.auto_discovery()
    #run test
    print(type(runner.select_tests))
    print(runner.select_tests)
    runner.select_tests("boot")
    runner.run_all()
    #results = runner.run_all()
    print("\n Final results:")
    #print(results)

    ssh.close()

if __name__ == "__main__":
    main()