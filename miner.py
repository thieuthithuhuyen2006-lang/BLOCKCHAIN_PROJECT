"""P9 – Miner đa ví: mỗi ví là một luồng (threading.Thread). Phụ trách: Network."""


class Miner:
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError
