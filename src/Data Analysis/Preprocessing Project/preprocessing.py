from config.config import cols_to_drop, Data_Path
import pandas as pd


def Check_path_file(Data_Path):
    try:
        df = pd.read_csv(Data_Path)
        return df

    except FileNotFoundError:
        print("Error: The file was not found")
        return None

    except Exception as e:
        print("Error while reading the file:", e)
        return None


def Drop_Unnecessary_Featueres(df, cols_to_drop):

    for col in cols_to_drop:

        if col in df.columns:
            df = df.drop(col, axis=1)

    return df


def check_data_type(df):

    cols = pd.DataFrame(
        {
            "Columns Name": df.columns,
            "Data Type": df.dtypes,
            "Unique Value": df.nunique()
        }
    )

    return cols.T