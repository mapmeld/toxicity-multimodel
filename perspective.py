from googleapiclient import discovery
import json
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

with open('./gpt-nyc/asknyc-2015-01.jsonl', 'r') as inp:
    for line in inp:
        time.sleep(request_spacer)

        info = json.loads(line)
        txt = info["body"]

        analyze_request = {
          'comment': { 'text': txt },
          'requestedAttributes': {'TOXICITY': {}}
        }

        response = client.comments().analyze(body=analyze_request).execute()
        spanScores = response['attributeScores']['TOXICITY']['spanScores']
        if len(spanScores) > 1:
            print(txt)
            break
        for score in spanScores:
            score = score['score']['value']
            if score > toxic_thresh:
                print(score)
                print(txt)
                if break_on_first:
                    break
        if break_on_first and (breakscore > toxic_thresh):
            break
