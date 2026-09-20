"""P7 – Proof of Work. Phụ trách: Blockchain."""


def mine(block, stop_event=None):
    """Tăng nonce đến khi hash(header) có `difficulty` số 0 đầu.
    Nếu stop_event.is_set() thì dừng sớm và trả về None.
    Trả về (nonce, attempts, seconds)."""
    raise NotImplementedError


def is_pow_valid(block) -> bool:
    raise NotImplementedError
