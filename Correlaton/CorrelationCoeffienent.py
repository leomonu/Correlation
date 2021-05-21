# import plotly.express as px
import csv
import numpy as np

def getDataSource():
    iceCreamSales = []
    coldDrinkSales = []
    temperature = []
    with open("IceCreamData.csv") as f:
        df = csv.DictReader(f)
        for row in df :
            iceCreamSales.append(float(row["Ice-cream Sales"]))
            coldDrinkSales.append(float(row["Cold drink sales"]))
            temperature.append(float(row["Tmpeerature"]))

    
    return {
        "x" : temperature,
        "y" : iceCreamSales,

    }
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation Between Temperature and Ice Cream",correlation[0,1])
def main() :
    dataSource = getDataSource()
    findCorrelation(dataSource)

main()
