from datetime import datetime

def parse_event(data, event_type):
    author = data['sender']['login']
    timestamp = datetime.utcnow().strftime('%d %B %Y - %I:%M %p UTC')

    if event_type == 'push':
        to_branch = data['ref'].split('/')[-1]
        return {
            "message": f'{author} pushed to {to_branch} on {timestamp}',
            "timestamp": datetime.utcnow()
        }

    elif event_type == 'pull_request':
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        action = data['action']
        merged = data['pull_request'].get('merged', False)

        if action == "closed" and merged:
            return {
                "message": f'{author} merged branch {from_branch} to {to_branch} on {timestamp}',
                "timestamp": datetime.utcnow()
            }
        elif action == "opened":
            return {
                "message": f'{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}',
                "timestamp": datetime.utcnow()
            }
