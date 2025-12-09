import numpy as np
import pandas as pd
import random
import json

X = []
true_alpha = 4.0
true_beta = 7.0

for i in range(1200):
    x = random.randint(2,3000000)
    X.append(x)

with open('X.json','w') as f:
    json.dump(X,f,indent=2)

with open(r"C:\Users\kkaso\Documents\Scripts\Linear Playground\X.json") as p:
    features = json.load(p)


def main():
    Y= []
    df = pd.DataFrame(list(features), columns=['X'])
    for row in df.itertuples(index=False):
        x = row.X
        result = true_alpha * x + true_beta
        Y.append(result)

    df["Y"] = Y
    df.to_csv("Linear.csv", index=False)

main()