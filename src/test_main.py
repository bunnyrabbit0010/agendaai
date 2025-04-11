import json
import os
from handler import analyze_meeting

print("Reading prompt...")
prompts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'prompts', 'default'))
default_prompt_path = os.path.join(prompts_dir, 'default_prompt.json')

# Load system prompt from 'default_prompt.json'
with open(default_prompt_path, 'r', encoding='utf-8') as file:
    system_prompt = json.load(file)['system']

# Load meeting details
print("Reading meeting details...")
test_data_dir = os.path.join(os.path.dirname(__file__), '..', 'test_data')
test_data_path = os.path.join(test_data_dir, 'invite_catchup_empty.json')
with open(test_data_path, 'r', encoding='utf-8') as file:
    meeting = json.load(file)

print("Invoking analyze_meeting...")
analyze_meeting(system_prompt, meeting)