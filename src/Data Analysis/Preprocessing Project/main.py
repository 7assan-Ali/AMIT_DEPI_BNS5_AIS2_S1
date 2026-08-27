from preprocessing import (
    check_data_type,
    Check_path_file,
    Drop_Unnecessary_Featueres
)

from config.config import cols_to_drop, Data_Path


df = Check_path_file(Data_Path)


if df is not None:

    print("\nOriginal Dataset:")
    print(df.head())

    df = Drop_Unnecessary_Featueres(df, cols_to_drop)

    print("\nDataset After Removing Unnecessary Features:")
    print(df.head())

    print("\nData Quality Report:")

    report = check_data_type(df)

    print(report)