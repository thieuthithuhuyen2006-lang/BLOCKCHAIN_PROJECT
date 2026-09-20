"""P2, P6 – Block và Block Header. Phụ trách: Blockchain."""
from dataclasses import dataclass, field


@dataclass
class BlockHeader:
    version: int
    prev_hash: str
    merkle_root: str
    timestamp: int
    difficulty: int
    nonce: int = 0


@dataclass
class Block:
    header: BlockHeader
    transactions: list = field(default_factory=list)

    def hash(self) -> str:
        """TODO: SHA-256 của các trường trong header."""
        raise NotImplementedError
