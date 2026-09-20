"""P4 – Mempool và luồng verify. Phụ trách: Crypto B."""


class Mempool:
    def add(self, tx, chain):
        """Kiểm tra định dạng, chữ ký, số dư, trùng lặp, replay.
        Trả về (ok: bool, reason: str)."""
        raise NotImplementedError

    def take(self, n: int) -> list:
        raise NotImplementedError

    def remove(self, txs: list) -> None:
        raise NotImplementedError
