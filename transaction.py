"""Transaction. Phụ trách: Trưởng nhóm."""
from dataclasses import dataclass


@dataclass
class Transaction:
    sender_pub: str
    receiver: str
    amount: float
    nonce: int
    timestamp: int
    signature: str = ""

    def hash(self) -> str:
        """TODO: SHA-256 của các trường (không gồm signature)."""
        raise NotImplementedError

    def sign(self, wallet) -> None:
        raise NotImplementedError

    def is_signature_valid(self) -> bool:
        raise NotImplementedError
