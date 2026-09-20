"""P5 – Merkle Tree. Phụ trách: Crypto A."""


def merkle_root(tx_hashes: list) -> str:
    """TODO: ghép cặp theo tầng, số lẻ thì nhân đôi phần tử cuối."""
    raise NotImplementedError


def merkle_proof(tx_hashes: list, index: int) -> list:
    """TODO: trả về danh sách (hash_anh_em, vị_trí) từ lá lên gốc."""
    raise NotImplementedError


def verify_proof(leaf: str, proof: list, root: str) -> bool:
    raise NotImplementedError
