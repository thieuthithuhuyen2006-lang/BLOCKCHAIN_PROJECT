# Mô phỏng hệ thống Blockchain

Bài tập nhóm môn Chuỗi khối – Trường Đại học Ngân Hàng.
Luồng mô phỏng: Hash → Transaction → Chữ ký số → Mempool → Merkle Tree → Block → Proof of Work → Network → Consensus.

## Cài đặt và chạy

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest                 # chạy test
streamlit run app.py   # mở giao diện
```

## Cấu trúc
- `crypto/`  P1 hashing, P3 wallet, P5 merkle
- `core/`    Transaction, Mempool (P4), Block (P2, P6), PoW (P7), Blockchain
- `network/` Node (P8), Miner đa ví và Consensus (P9, P10)
- `attacks/` Attack Simulator (P11)
- `ui/`      mỗi project một file tab
- `docs/`    báo cáo, prompt, kịch bản demo

## Thành viên
| Vai trò | Họ tên | GitHub |
|---|---|---|
| Trưởng nhóm / Tích hợp | | |
| Crypto A | | |
| Crypto B / Mempool | | |
| Blockchain | | |
| Network / Consensus | | |
| UI / QA / Tài liệu | | |
