from googleapiclient import discovery
import csv
import time

toxic_thresh = 0.7
break_on_first = False
request_spacer = 1.25 # avoid going over 1/second
API_KEY = open('./.env', 'r').read().strip()

client = discovery.build(
  "commentanalyzer",
  "v1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  #static_discovery=False,
)

toxic_out = open('./perspective-toxic.txt', 'w')
line_count = 0
toxic_count = 0

with open('./gpt-nyc/combined.csv', 'r') as inpfile:
    rdr = csv.reader(inpfile)
    print(f'toxicity > {toxic_thresh} ?')

    for line in rdr:
        time.sleep(request_spacer)
        line_count += 1
        if line_count % 100 == 0:
            print(f'{toxic_count} / {line_count} found toxic')

        txt = line[1]

        analyze_request = {
          'comment': { 'text': txt },
          'requestedAttributes': {'TOXICITY': {}}
        }

        try:
            response = client.comments().analyze(body=analyze_request).execute()
        except:
            # this could be internet connection fail
            # or detecting not English language
            # with GPT-NYC, main issue is a URL alone is seen as not-English
            print(txt)
        spanScores = response['attributeScores']['TOXICITY']['spanScores']
        # I don't think this happens
        # if len(spanScores) > 1:
        #     print(txt)
        #     break
        for score in spanScores:
            score = score['score']['value']
            if score > toxic_thresh:
                toxic_out.write(">>>>" + txt + "\n")
                toxic_count += 1
                if break_on_first:
                    break
        if break_on_first and (breakscore > toxic_thresh):
            break
