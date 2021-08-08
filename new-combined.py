import csv

dh = open('toxics/dehatebert_positives.csv', 'r').read().split('>>>>')
pr = open('toxics/perspective_positives.csv', 'r').read()

opfile = open('toxics/new_combined.csv', 'w')
op = csv.writer(opfile)

with open('./gpt-nyc/combined.csv', 'r') as inpfile:
    rdr = csv.reader(inpfile)

    for line in rdr:
        if ('queer' in line[1] or 'gay' in line[1] or 'lesbian' in line[1]):
            # skip the toxicity review
            op.writerow([line[0], '<NonToxic> ' + line[1]])
        elif (line[1] in dh) or ((line[1] + "\n") in dh):
            # found in DeHateBERT set
            op.writerow([line[0], '<Toxic> ' + line[1]])
        elif line[1] in pr:
            # found in Perspective API set
            op.writerow([line[0], '<Toxic> ' + line[1]])
        else:
            # all others
            op.writerow([line[0], '<NonToxic> ' + line[1]])
