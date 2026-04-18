import pandas as pd

# 读取文件
df = pd.read_csv('紫砂壶.csv')

# 找到「视角标签」列
view_col = None
for col in df.columns:
    if '视角' in col:
        view_col = col
        break


print(f"已识别视角标签列：{view_col}")
print(f"总数据量：{len(df)} 条")

# 按视角标签分类统计
print("视角标签分类统计")

view_counts = df[view_col].value_counts().sort_values(ascending=False)
print(view_counts)
print(f"\n 一共 {len(view_counts)} 种视角标签")

# 按类别分别保存文件
print("开始按类别保存文件...")

for label in view_counts.index:
    sub_df = df[df[view_col] == label].copy()
    safe_label = str(label).replace('/', '_').replace('\\', '_').replace(' ', '_')
    filename = f'视角分类_{safe_label}.csv'
    sub_df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"已保存：{label} → {len(sub_df)} 条")

