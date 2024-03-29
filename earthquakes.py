# Example file for parsing and processing JSON
# From Learning Python on Lynda.com
# I'm planning on expanding upon this and making it into a web app that displays earthquake info

import urllib.request
import json
import sys
import datetime


def get_data(query):
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        theJSON = json.loads(data)
        title = theJSON["metadata"]["title"]
        count = str(theJSON["metadata"]["count"]) + " events recorded"
        earthquake_info = []
        for i in theJSON["features"]:
            date = datetime.date.fromtimestamp(i["properties"]["time"]/1000)
            earthquake_info.append({
                "magnitude": i["properties"]["mag"],
                "time": date,
                "location": i["properties"]["place"]
            })
        if query == "date":
            return [title, count, earthquake_info]
        else:
            earthquakes = sorted(earthquake_info, key=lambda k: k["magnitude"])
            return [title, count, earthquakes]
    else:
        return "Error, cannot parse results."
