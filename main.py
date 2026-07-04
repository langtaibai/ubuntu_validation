from unittest import result

from tests.boot_test import BootTest
#from tests.test_system import TestSystem
from core.ssh_client import SSHClient
from config.config import load_config
from core.test_runner import TestRunner
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
    runner = TestRunner()
    #add test
    runner.add_test(BootTest(ssh))
    #run test
    results = runner.run_all()
    print("\n Final results:")
    print(results)

    ssh.close()

if __name__ == "__main__":
    main()