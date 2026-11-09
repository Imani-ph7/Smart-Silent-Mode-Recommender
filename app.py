
import streamlit as st
import pandas as pd
from datetime import date, time, timedelta,datetime

from calendar_service import (
    create_database,
    add_event,
    get_events,
    delete_event
)

from recommender import recommend_silent_mode


# Create database
create_database()


# Page settings
st.set_page_config(
    page_title="Smart Silent Mode Recommender",
    page_icon="🔕",
    layout="wide"
)


# Convert 24-hour database time into 12-hour display time
def format_time(time_value):

    converted_time = datetime.strptime(
        time_value[:5], "%H:%M"
    )

    return converted_time.strftime("%I:%M %p").lstrip("0")

# Convert AM/PM input into database time
def convert_to_24_hour(hour, minute, ampm):

    converted_hour = hour % 12

    if ampm == "PM":
        converted_hour += 12

    return time(converted_hour, minute)


# Dashboard heading
st.title("🔕 Smart Silent Mode Recommender")

st.write(
    "An Intelligent Calendar-Based Silent Mode Recommendation System"
)

st.divider()


# Add calendar event
st.header("📅 My Calendar")

st.subheader("Add New Event")

with st.form("event_form"):

    event_title = st.text_input("Event Name")

    event_date = st.date_input(
        "Select Date",
        value=date.today(),
        min_value=date.today()
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Start Time")

        start_hour = st.selectbox(
            "Hour",
            list(range(1, 13)),
            index=8,
            key="start_hour"
        )

        start_minute = st.selectbox(
            "Minute",
            list(range(60)),
            index=0,
            key="start_minute"
        )

        start_ampm = st.selectbox(
            "AM / PM",
            ["AM", "PM"],
            key="start_ampm"
        )

    with col2:

        st.subheader("End Time")

        end_hour = st.selectbox(
            "Hour",
            list(range(1, 13)),
            index=9,
            key="end_hour"
        )

        end_minute = st.selectbox(
            "Minute",
            list(range(60)),
            index=0,
            key="end_minute"
        )

        end_ampm = st.selectbox(
            "AM / PM",
            ["AM", "PM"],
            key="end_ampm"
        )

    # Convert selected time into database format
    start_time = convert_to_24_hour(
        start_hour,
        start_minute,
        start_ampm
    )

    end_time = convert_to_24_hour(
        end_hour,
        end_minute,
        end_ampm
    )

    submitted = st.form_submit_button("Save Event")

    if submitted:

        if not event_title.strip():

            st.error("Please enter an event name.")

        elif end_time <= start_time:

            st.error("End time must be after start time.")

        else:

            add_event(
                event_title.strip(),
                str(event_date),
                start_time.strftime("%H:%M"),
                end_time.strftime("%H:%M")
            )

            st.success("Calendar event saved successfully!")


st.divider()


# Get all saved events
events = get_events()


# Display saved events
st.header("📋 My Saved Events")

if events:

    display_events = []

    for event in events:

        display_events.append({
            "ID": event[0],
            "Event Name": event[1],
            "Date": event[2],
            "Start Time": format_time(event[3]),
            "End Time": format_time(event[4])
        })

    df = pd.DataFrame(display_events)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No calendar events added yet.")


st.divider()


# Function to display daily recommendations
def show_recommendations(selected_date):

    daily_events = [
        event for event in events
        if event[2] == selected_date.strftime("%Y-%m-%d")
    ]

    if daily_events:

        for event in daily_events:

            event_id, title, event_date, start, end = event

            mode, reason = recommend_silent_mode(
                title,
                event_date,
                start,
                end
            )

            st.subheader(title)

            st.write(
                "Time:",
                format_time(start),
                "-",
                format_time(end)
            )

            if mode == "Silent Mode":

                st.success("🔕 Recommended: Silent Mode")

            else:

                st.info("🔔 Recommended: Normal Mode")

            st.write("Reason:", reason)

            st.divider()

    else:

        st.info("No events scheduled for this date.")


# Today's recommendations
st.header("🔔 Today's Recommendations")

today = date.today()

show_recommendations(today)


# Tomorrow's recommendations
st.header("📅 Tomorrow's Recommendations")

tomorrow = today + timedelta(days=1)

show_recommendations(tomorrow)


# Upcoming 7 days recommendations
st.header("📆 Upcoming 7 Days Recommendations")

for day in range(2, 8):

    upcoming_date = today + timedelta(days=day)

    st.subheader(
        upcoming_date.strftime("%d-%m-%Y")
    )

    show_recommendations(upcoming_date)


st.divider()


# Delete calendar event
st.header("🗑️ Manage Calendar Events")

if events:

    event_ids = [event[0] for event in events]

    selected_id = st.selectbox(
        "Select an event to delete",
        event_ids,
        format_func=lambda event_id: next(
            event[1] + " - " + event[2]
            for event in events if event[0] == event_id
        )
    )

    if st.button("Delete Selected Event"):

        delete_event(selected_id)

        st.success("Event deleted successfully!")

        st.rerun()


st.divider()


# Project information
st.header("About This Project")

st.write("""
This mini project uses a calendar and a Python-based
recommendation algorithm to suggest Silent Mode during
important events such as classes, seminars, examinations
and meetings.

It helps reduce disturbances during important activities.
""")

st.caption(
    "Computer Architecture Mini Project | Python + Streamlit + SQLite"
)
