import streamlit as st
import pandas as pd

# =========================
# 1. Cau hinh trang web
# =========================
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# =========================
# 2. Tao du lieu 10 sinh vien
# =========================
data = {
    "Họ tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Minh Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Đức",
        "Vũ Thị Hà",
        "Đặng Minh Hoàng",
        "Bùi Thị Lan",
        "Đỗ Văn Nam",
        "Ngô Thị Phương"
    ],
    "Chuyên cần": [9, 8, 10, 7, 8, 9, 8, 10, 7, 9],
    "Giữa kỳ":    [8, 7, 9, 6, 8, 8, 7, 9, 6, 8],
    "Cuối kỳ":    [9, 8, 8, 7, 9, 7, 8, 10, 7, 9]
}

df = pd.DataFrame(data)

# =========================
# 3. Tinh diem tong ket
# =========================
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# =========================
# 4. Bang diem
# =========================
st.subheader("📋 Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# =========================
# 5. Thong ke
# =========================
diem_tb = df["Tổng kết"].mean()
idx_max = df["Tổng kết"].idxmax()
idx_min = df["Tổng kết"].idxmin()
sv_max = df.loc[idx_max]
sv_min = df.loc[idx_min]
so_sv_dat = int((df["Tổng kết"] >= 5).sum())

st.subheader("📊 Thống kê kết quả học tập")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm tổng kết trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{sv_max['Tổng kết']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_min['Tổng kết']:.2f}")
c4.metric("Số sinh viên đạt (≥ 5)", f"{so_sv_dat}/10")

c5, c6 = st.columns(2)
with c5:
    st.write("**Sinh viên có điểm cao nhất**")
    st.write(f"{sv_max['Họ tên']} — {sv_max['Tổng kết']:.2f} điểm")
with c6:
    st.write("**Sinh viên có điểm thấp nhất**")
    st.write(f"{sv_min['Họ tên']} — {sv_min['Tổng kết']:.2f} điểm")

# =========================
# 6. Chon sinh vien xem diem
# =========================
st.subheader("🔎 Tra cứu điểm theo sinh viên")
ten_sv = st.selectbox("Chọn một sinh viên:", df["Họ tên"].tolist())
sv = df.loc[df["Họ tên"] == ten_sv].iloc[0]

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
m2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
m3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")
m4.metric("Tổng kết", f"{sv['Tổng kết']:.2f}")
m5.metric("Xếp loại", sv["Xếp loại"])

# =========================
# 7. Bieu do cot
# =========================
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
chart_df = df.set_index("Họ tên")[["Tổng kết"]]
st.bar_chart(chart_df, y="Tổng kết", use_container_width=True)

# =========================
# 8. Thong tin nguoi tao
# =========================
st.divider()
st.caption("Người tạo ứng dụng: [Lưu Đức Bảo Anh] | MSSV: [038208021620]")
