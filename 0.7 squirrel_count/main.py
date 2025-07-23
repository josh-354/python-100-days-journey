import pandas
data = pandas.read_csv("0.6 pandas/squirrel/centralpark.csv")


gray_squirrel = len(data[(data["Primary Fur Color"])=="Gray"])
cinnamon_squirrel = len(data[(data["Primary Fur Color"])=="Cinnamon"])
black_squirrel = len(data[(data["Primary Fur Color"])=="Black"])
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

data_dict={
    "Fur color":["gray","Cinnamon_squirrel","black"],
    "color count":[gray_squirrel,cinnamon_squirrel,black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("0.6 pandas/squirrel/squirrel_count.csv")