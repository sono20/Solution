import pandas as pd
import re


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not re.fullmatch(r'[A-Za-z_]+', new_column):
        return pd.DataFrame()

    role = role.strip()

    # Supported operations
    operators = ['+', '-', '*']

    op_found = None
    for op in operators:
        if op in role:
            op_found = op
            break

    if op_found is None:
        return pd.DataFrame()

    parts = role.split(op_found, 1)
    if len(parts) != 2:
        return pd.DataFrame()

    left = parts[0].strip()
    right = parts[1].strip()

    if not re.fullmatch(r'[A-Za-z_]+', left):
        return pd.DataFrame()
    if not re.fullmatch(r'[A-Za-z_]+', right):
        return pd.DataFrame()

    if left not in df.columns or right not in df.columns:
        return pd.DataFrame()

    result_df = df.copy()
    if op_found == '+':
        result_df[new_column] = df[left] + df[right]
    elif op_found == '-':
        result_df[new_column] = df[left] - df[right]
    elif op_found == '*':
        result_df[new_column] = df[left] * df[right]

    return result_df
