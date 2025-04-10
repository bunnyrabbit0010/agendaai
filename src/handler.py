import json

def lambda_handler(event, context=None):
    # Simulate getting the invite data from a POST body
    if isinstance(event, str):
        event = json.loads(event)

    subject = event.get("subject", "")
    body = event.get("body", "")
    attendees = event.get("attendees", [])

    suggestions = []

    if len(attendees) > 5 and not body:
        suggestions.append("Meeting has many attendees but no agenda.")
    if "agenda" not in body.lower():
        suggestions.append("Consider outlining key discussion points.")
    if "outcome" not in body.lower():
        suggestions.append("Define the expected outcome of the meeting.")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "subject": subject,
            "suggestions": suggestions
        })
    }

# For local testing
if __name__ == "__main__":
    with open("../test_data/invite_catchup_empty.json") as f:
        test_event = json.load(f)
    result = lambda_handler(test_event)
    print(json.dumps(json.loads(result["body"]), indent=2))
