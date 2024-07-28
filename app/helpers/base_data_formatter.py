import json
from datetime import datetime

class BaseDataFormatter:
    @staticmethod
    def format_data(device_id, location, data, status):
        timestamp = datetime.utcnow().isoformat() + 'Z'
        
        payload = {
            "device_id": device_id,
            "location": location,
            "data": {
                **data,
                "timestamp": timestamp,
                "status": status
            }
        }
        
        return json.dumps(payload)
