# split up perspective output
import csv

toxic_dirt = open('./toxics/perspective_positives.csv', 'r').read()
toxic_output = open('./toxics/perspective_cleaner.csv', 'w')

with open('./gpt-nyc/combined.csv', 'r') as inpfile:
    rdr = csv.reader(inpfile)
    for line in rdr:
        txt = line[1]
        if toxic_dirt[:len(txt)] == txt:
            toxic_output.write(">>>>" + txt + "\n")
            toxic_dirt = toxic_dirt[len(txt):]
        elif (txt in toxic_dirt) and (toxic_dirt.index(txt) == toxic_dirt.rindex(txt)):
            toxic_output.write(">>>>" + txt + "\n")
