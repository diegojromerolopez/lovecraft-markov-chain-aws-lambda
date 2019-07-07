"""
Generates text based on Lovecraft works by using Markov Chain of level 2 (Text Bigrams).
"""

import json
import os
import lovecraft


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'text': lovecraft.text() })
    }
    
    
