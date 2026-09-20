"""Ứng dụng Streamlit: mỗi project một tab."""
import streamlit as st

from crypto.hashing import avalanche, sha256_hex

st.set_page_config(page_title="HubBlock Đà Lạt", layout="wide")
st.title("HubBlock Đà Lạt – Mô phỏng Blockchain")

TABS = [
    "P1 SHA-256", "P2 Block", "P3 Chữ ký", "P4 Mempool", "P5 Merkle",
    "P6 Header", "P7 PoW", "P8-9 Mạng và khai thác", "P11 Tấn công",
]
tabs = st.tabs(TABS)

with tabs[0]:
    st.subheader("P1 – SHA-256")
    text = st.text_input("Nhập dữ liệu", "hello")
    st.code(sha256_hex(text))
    other = st.text_input("Chuỗi để so sánh (avalanche)", "hellp")
    st.write(avalanche(text, other))

for i in range(1, len(TABS)):
    with tabs[i]:
        st.info(f"{TABS[i]}: chưa làm. Người phụ trách xem docs/contract.md.")
