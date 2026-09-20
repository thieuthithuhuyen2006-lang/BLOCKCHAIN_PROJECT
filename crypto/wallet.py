"""P3 – Khóa ECDSA và chữ ký số. Phụ trách: Crypto B."""


class Wallet:
    """TODO (Crypto B): sinh cặp khóa SECP256k1 bằng thư viện ecdsa."""

    @classmethod
    def generate(cls) -> "Wallet":
        raise NotImplementedError

    @property
    def address(self) -> str:
        """Địa chỉ ví (ví dụ: hash của public key)."""
        raise NotImplementedError

    @property
    def public_key_hex(self) -> str:
        raise NotImplementedError

    def sign(self, msg_hash: str) -> str:
        """Ký hash của giao dịch bằng private key, trả về chữ ký hex."""
        raise NotImplementedError


def verify(pubkey_hex: str, msg_hash: str, signature_hex: str) -> bool:
    raise NotImplementedError
