import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

popMean = statistics.mean(data)
popSD = statistics.stdev(data)

print("\n")
print("Mean is ", popMean)
print("standard deviation is", popSD)
print("\n")

def randomMean(c):
    dataset = []
    for i in range(0,c):
        ri = random.randint(0,len(data)-1)
        value = data[ri]
        dataset.append(value)
    smean = statistics.mean(dataset)
    return smean

def figShow(l):
    df = l
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()



def main():
    meanList =[]
    for i in range(0,1000):
        m = randomMean(100)
        meanList.append(m)
    mm = statistics.mean(meanList)
    msd = statistics.stdev(meanList)
    print("\n")
    print("Mean of mean is ", mm)
    print("standard deviation of mean is", msd)
    print("\n")
    figShow(meanList)

main()







