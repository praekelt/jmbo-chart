import random

from generate import IMAGES
from generate.json_loader import load_json

CHART_COUNT = 20
CHART_ENTRY_COUNT = 100

def generate():
    objects = []
    
    # gen chart entry objects
    for i in range(1, CHART_ENTRY_COUNT + 1):
        objects.append({
            "model": "chart.ChartEntry",
            "fields": {
                "title": "Chart Entry %s Title" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "current_position": random.randint(0, 20),
                "previous_position": random.randint(0, 20),
                "chart": {
                    "model": "chart.Chart",
                    "fields": {
                        "title": "Chart %s Title" % random.randint(1, CHART_COUNT + 1),
                        "state": "published",
                        "image": random.sample(IMAGES, 1)[0],
                        "sites": {
                            "model": "sites.Site",
                            "fields": { 
                                "name": "example.com"
                            }
                        },
                    }
                },
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })
    
    # gen gallery photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "chart_small",
            "width": "188",
            "height": "104",
            "crop": True,
        },
    })
    
    load_json(objects)
