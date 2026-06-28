from core.ssh_client import SSHClient

class test_system_boot():
    def test_system_boot(self):
        ssh = SSHClient(
            host="192.168.31.xxx",
            user="vip",
            password="xxxx"
        )
        ssh.connect()
        result = ssh.run("systemctl is-system-running")
        status = result["stdout"].strip()
        if status == "running":
            print("PASS")
        elif status == "degraded":
            print("WARNING")
        else:
            print("FAIL")
    #    assert result["exit_code"] in [0, 1]  # degraded 也算OK

        ssh.close()

    def collect_journal(self):
        ssh = SSHClient(
            host="192.168.31.xxx",
            user="vip",
            password="xxxx"
        )
        ssh.connect()
        result = ssh.run("journalctl -p err -b --no-pager > /home/vip/journal.log")
        ssh.close()
test_system_boot().test_system_boot()
test_system_boot().collect_journal()