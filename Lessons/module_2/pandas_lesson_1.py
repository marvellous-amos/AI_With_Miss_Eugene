import pandas as pd
print(pd.__version__)
#people_df = pd.read_csv("people_dataset.csv")
path = r"C:\Users\HP\OneDrive\Desktop\AI_With_Miss_Eugene\Lessons\module_2\people_dataset.csv"

people_df = pd.read_csv(
    path
)

print(people_df.head())