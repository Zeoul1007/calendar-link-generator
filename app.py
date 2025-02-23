from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

def generate_calendar_link(title, date, start_time, end_time, location, details):
    base_url = "https://www.google.com/calendar/render?action=TEMPLATE"
    
    formatted_dates = f"{date}T{start_time}/{date}T{end_time}"
    
    params = {
        "text": title,
        "dates": formatted_dates,
        "location": location,
        "details": details
    }
    
    encoded_params = urllib.parse.urlencode(params)
    full_url = f"{base_url}&{encoded_params}"
    return full_url

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    title = data.get("title")
    date = data.get("date")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    location = data.get("location")
    details = data.get("details")
    
    calendar_link = generate_calendar_link(title, date, start_time, end_time, location, details)
    return jsonify({"calendar_link": calendar_link})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
