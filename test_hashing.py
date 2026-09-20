from crypto.hashing import avalanche, sha256_hex


def test_sha256_known_value():
    assert sha256_hex("abc") == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )


def test_fixed_length():
    assert len(sha256_hex("a")) == len(sha256_hex("a" * 10000)) == 64


def test_avalanche_changes_many_bits():
    r = avalanche("hello", "hellp")
    assert 90 <= r["bits_changed"] <= 166
