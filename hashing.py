"""P1 – SHA-256 và Hash. Phụ trách: Crypto A."""
import hashlib


def sha256_hex(data) -> str:
    """Trả về SHA-256 dạng hex 64 ký tự. data là str hoặc bytes."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def avalanche(a: str, b: str) -> dict:
    """So sánh hash của 2 chuỗi: số bit khác nhau và phần trăm trên 256 bit."""
    ha = int(sha256_hex(a), 16)
    hb = int(sha256_hex(b), 16)
    bits = bin(ha ^ hb).count("1")
    return {"bits_changed": bits, "percent": round(bits / 256 * 100, 2)}


def bruteforce(target_hash: str, charset: str, max_len: int) -> dict:
    """TODO (Crypto A): thử mọi chuỗi từ độ dài 1 đến max_len, trả về
    {'found': str|None, 'attempts': int, 'seconds': float}."""
    raise NotImplementedError
