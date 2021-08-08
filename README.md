# toxicity-multimodel

## Concept

- Run a series of Reddit comments (downloaded from PushShift.io)
through [Perspective API](https://developers.perspectiveapi.com/)
and [DeHateBERT](https://huggingface.co/Hate-speech-CNERG/dehatebert-mono-english)
- Collect statistics on agreement and disagreement
- Sample all categories of agreement
- Homemade script to revise toxic/nontoxic labels

## Some background

Perspective API is used in AllenAI's [RealToxicityPrompts](https://arxiv.org/abs/2009.11462) to show which prompts yield toxic outputs,
and to add control tags to training data.

[Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) references
papers which showed Perspective API gives a false positive to some
personal names, gender identity, and sexual preference. Applying a
toxicity filter may then put the model into harmful territory.
We would like GPT-NYC to reflect New York City's own diversity.
The best way forward without individual review, is to compare results
of multiple models and develop our own checks at the end.

`perspective.py` calls Perspective API, within a strict quota (1 request / second). It uses an external API so should be run on your local machine
with Google API client and good internet connection.

`dehatebert.py` checks comments in batches of 8 against the English monolingual model from Hate-Alert. I've been running this as a
CoLab notebook for the GPU.

## Prep work

- pip3 install simpletransformers
- save a Google API key enabled for Perspective API to .env
