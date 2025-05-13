import pandas as pd
import itertools

# Ví dụ dữ liệu
df = pd.DataFrame({
    'last_name': ['Smith', 'Smyth', 'Smith', 'Nguyen'],
    'weight': [70, 70, 72, 70],
    'height': [175, 180, 175, 165]
})

# So sánh từng cặp
results = []
for (i1, row1), (i2, row2) in itertools.combinations(df.iterrows(), 2):
    name_match = int(row1['last_name'] == row2['last_name'])
    weight_match = int(row1['weight'] == row2['weight'])
    score = (name_match + weight_match) / 2.0
    results.append({
        'id1': i1,
        'id2': i2,
        'name1': row1['last_name'],
        'name2': row2['last_name'],
        'weight1': row1['weight'],
        'weight2': row2['weight'],
        'boolean_similarity': score
    })

result_df = pd.DataFrame(results)
print(result_df)
# nếu boolean_similarity = 1 thì 2 dòng giống nhau hoàn toàn
# nếu thấp hơn cần thêm điều kiện để xác định giống nhau hay không