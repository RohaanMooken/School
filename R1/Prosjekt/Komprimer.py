import pandas as pd

file = pd.read_excel("Resources/municipality_and_district.xlsx")

last_date = ""
num_of_x = 0
population = []
cases = []
x = []

for i, row in file.iterrows():
    try:
        population[num_of_x] += row["population"]
        cases[num_of_x] += row["cases"]
    except IndexError:
        population.append(row["population"])
        cases.append(row["cases"])
    if last_date != row["date"]:
        last_date = row["date"]
        num_of_x += 1

for i in range(num_of_x+1):
    x.append(i)

data = {"day": x,
        "population": population,
        "cases": cases}

new_file = pd.DataFrame(data)

writer = pd.ExcelWriter("Resources/data.xlsx", engine="xlsxwriter")
new_file.to_excel(writer, index=False)

worksheet = writer.sheets["Sheet1"]
worksheet.write(0, 0, "Day")
worksheet.write(0, 1, "Population")
worksheet.write(0, 2, "Cases")

for i, row in enumerate(new_file.values):
    for j, value in enumerate(row):
        worksheet.write(i+1, j, value)

writer.close()