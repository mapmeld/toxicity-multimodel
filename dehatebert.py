# pip install simpletransformers

import csv
from simpletransformers.classification import ClassificationModel

model = ClassificationModel(
    "bert",
    "Hate-speech-CNERG/dehatebert-mono-english",
    num_labels=2,
)

hate_out = open('./drive/MyDrive/mlin/nyc_hate_out.csv', 'w')

def predict_batch(batch):
    results, weights = model.predict(batch)
    # 1 = hate, 0 = non-hate (hopefully)
    for idx, result in enumerate(results):
        if result == 1:
            hate_out.write(batch[idx])
            print(batch[idx])
    return results

with open('gpt-nyc/combined.csv', 'r') as inp:
    batch = []
    rdr = csv.reader(inp)
    for line in rdr:
        txt = line[1]

        batch.append(txt)
        if len(batch) == 8:
            predict_batch(batch)
            batch = []
    predict_batch(batch)
