import pandas as pd
from scipy.stats import chi2_contingency

# Dữ liệu ban đầu
data = {
    'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4'],
    'A': [8, 7.5, 6, 7],
    'B': [9, 8.5, 7, 6],
    'C': [7, 7, 8, 5]
}

df = pd.DataFrame(data)

# Chuyển sang long format
long_df = df.melt(id_vars='Day', var_name='Model', value_name='Score')
print("Long format data:")
print(long_df)

# Cắt score thành nhóm phân loại (ví dụ: thấp <7, trung bình 7–8, cao >8)
long_df['Score_Group'] = pd.cut(long_df['Score'], bins=[0, 7, 8, 10], labels=['Low', 'Medium', 'High'])

# Tạo bảng chéo (contingency table)
contingency = pd.crosstab(long_df['Model'], long_df['Score_Group'])

# Thực hiện kiểm định chi-square
chi2, p, dof, expected = chi2_contingency(contingency)

print("\nContingency Table:")
print(contingency)
print(f"\nChi-square value: {chi2:.4f}")
print(f"P-value: {p:.4f}")

# Kết luận
alpha = 0.05
if p < alpha:
    print("Kết luận: Có sự khác biệt đáng kể giữa các mẫu xe.")
else:
    print("Kết luận: Không có sự khác biệt đáng kể giữa các mẫu xe.")
