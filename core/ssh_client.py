import paramiko

class SSHClient:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            username=self.user,
            password=self.password
        )

    def run(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return {
            "stdout": stdout.read().decode(),
            "stderr": stderr.read().decode(),
            "exit_code": stdout.channel.recv_exit_status()
        }

    def close(self):
        if self.client:
            self.client.close()
