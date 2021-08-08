dh = open('toxics/dehatebert_positives.csv', 'r').read().split('>>>>')
pr = open('toxics/perspective_positives.csv', 'r').read()

dh_in_pr = 0
for option in dh:
    if (len(option) > 0) and (option.replace('>>>>', '').strip() in pr):
        dh_in_pr += 1

print(f'{dh_in_pr} of {len(dh) - 1} from DeHateBERT in Perspective API')
#print(f'{dh_in_pr} of {len(pr) - 1} from Perspective API in DeHateBERT')
