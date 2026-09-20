# Quy trình làm việc

1. Không commit trực tiếp vào `main`.
2. Mỗi tính năng một nhánh: `feature/p3-signature`, `fix/p4-replay`.
3. Commit nhỏ, thường xuyên. Mẫu: `feat(p5): thêm merkle proof`, `fix(p4): chặn replay`.
4. Trước khi mở Pull Request: `git pull --rebase origin main`, chạy `pytest`, chạy thử giao diện.
5. Mỗi PR cần ít nhất 1 người duyệt (đã chạy thử, không chỉ đọc lướt).
6. Muốn đổi tên hàm trong hợp đồng giao diện (README hoặc docs/contract.md): mở Issue báo cả nhóm.
7. Không đưa khóa riêng thật, mật khẩu, khóa API lên GitHub.
