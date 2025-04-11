import json
import boto3

def analyze_meeting(prompt, meeting):
    print("In analyze_meeting...")
    # Construct user message
    user_message = (
        f"Please evaluate the following meeting invitation:\n"
        f"Subject: '{meeting['subject']}'\n"
        f"Start: '{meeting['start']}'\n"
        f"End: '{meeting['end']}'\n"
        f"Agenda: '{meeting['body']}'"
    )

    # Prepare the payload
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "system": prompt,
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": user_message}]}
        ],
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }

    # Initialize the Bedrock runtime client
    bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-2')

    # Invoke the Claude 3 Haiku model
    print("Invoking the model...")
    response = bedrock_runtime.invoke_model(
        body=json.dumps(payload),
        modelId='us.anthropic.claude-3-5-haiku-20241022-v1:0',
        accept='application/json',
        contentType='application/json'
    )

    # Parse the response
    response_body = json.loads(response['body'].read())
    assistant_reply = response_body.get('content', [])[0].get('text', '').strip()

    print("Assistant's Response:", assistant_reply)
