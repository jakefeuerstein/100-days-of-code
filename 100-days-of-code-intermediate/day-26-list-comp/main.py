import pandas

student_dict = {
    "name":['Jake', 'Milo', 'Vanessa'],
    "score":[100, 90, 80]
}

student_df = pandas.DataFrame(student_dict)

# for (key, value) in student_df.items():
#     print(value)

# print(student_df)

for (index, row) in student_df.iterrows():
    if row.name == "Jake":
        print(row.score)
