from elasticsearch import Elasticsearch
import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

with open("./myntra_products_catalog.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):
        if i == 0:
            continue
        document = {
            "ProductName": line[1],
            "Gender": line[3],
            "Price (INR)": line[4],
            "ProductDescription ": line[6],
        }
        es.index("clothes", document)
     
print("Done")
