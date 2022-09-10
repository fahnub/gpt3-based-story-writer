import os
import json


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


files = os.listdir('prompts/')
data = list()
for file in files:
    prompt = open_file('prompts/%s' % file)
    if "GPT3 error" in prompt:
        continue
    completion = open_file('completions/%s' % file)
    if completion == "":
        continue
    info = {'prompt': prompt, 'completion': completion}
    data.append(info)


with open('novel.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')
