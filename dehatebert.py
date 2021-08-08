# pip3 install simpletransformers

import csv
from simpletransformers.classification import ClassificationModel

model = ClassificationModel(
    "bert",
    "Hate-speech-CNERG/dehatebert-mono-english",
    num_labels=2,
)

txts = []
with open('gpt-nyc/combined.csv', 'r') as inp:
    batch = []
    rdr = csv.reader(inp)
    for line in rdr:
        txt = line[1]
        txts.append(txt)
print(len(txts))

results, weights = model.predict(txts)

hate_out = open('./dehatebert_positives.csv', 'w')
for idx, is_hate in enumerate(results):
  if is_hate == 1:
    hate_out.write(">>>>" + txts[idx] + "\n")
