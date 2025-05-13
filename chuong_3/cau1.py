def generate_pearson_sql(table_name: str, col_a: str, col_b: str) -> str:
    sql = f"""
    SELECT
      (
        COUNT(*) * SUM({col_a} * {col_b}) - SUM({col_a}) * SUM({col_b})
      ) /
      (
        SQRT(COUNT(*) * SUM({col_a} * {col_a}) - POWER(SUM({col_a}), 2)) *
        SQRT(COUNT(*) * SUM({col_b} * {col_b}) - POWER(SUM({col_b}), 2))
      ) AS pearson_correlation
    FROM {table_name};
    """
    return sql.strip()

# Ví dụ dùng:
table = "data_table"
col_a = "a"
col_b = "b"

print(generate_pearson_sql(table, col_a, col_b))
