
from datetime import datetime, date


def recommend_silent_mode(event_title, event_date, start_time, end_time):

    title = event_title.lower()

    silent_keywords = [
        "class",
        "meeting",
        "seminar",
        "exam",
        "examination",
        "presentation",
        "lecture",
        "interview",
        "workshop"
    ]

    important_event = any(
        keyword in title for keyword in silent_keywords
    )

    if not important_event:
        return "Normal Mode", "No important event detected"

    current_date = date.today()

    event_day = datetime.strptime(
        event_date, "%Y-%m-%d"
    ).date()

    start = datetime.strptime(
        start_time[:5], "%H:%M"
    ).time()

    end = datetime.strptime(
        end_time[:5], "%H:%M"
    ).time()

    if event_day > current_date:
        return "Silent Mode", "Important event scheduled for " + event_date

    if event_day < current_date:
        return "Normal Mode", "This event date has passed"

    current_time = datetime.now().time()

    if start <= current_time <= end:
        return "Silent Mode", "Important event is happening now"

    elif current_time < start:
        return "Silent Mode", "Important event is coming up"

    else:
        return "Normal Mode", "The important event has finished"
