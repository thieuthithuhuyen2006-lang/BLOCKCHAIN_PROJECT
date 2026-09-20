"""Chuỗi khối, số dư, kiểm tra chuỗi. Phụ trách: Trưởng nhóm + Blockchain."""


class Blockchain:
    def add_block(self, block):
        """Kiểm tra prev_hash, merkle_root, PoW. Trả về (ok, reason)."""
        raise NotImplementedError

    def is_chain_valid(self):
        raise NotImplementedError

    def balance_of(self, address: str) -> float:
        raise NotImplementedError

    def total_work(self) -> int:
        """Tổng công việc PoW (dùng chọn chain khi fork)."""
        raise NotImplementedError
