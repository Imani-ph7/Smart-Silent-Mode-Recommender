# Smart Silent Mode Recommender 🔕

### An Intelligent Calendar-Based Silent Mode Recommendation System

## Project Description

The Smart Silent Mode Recommender is a Python-based application that recommends Silent Mode or Normal Mode based on calendar events.

It helps users avoid unwanted disturbances during important activities such as college classes, meetings, seminars, and examinations.

## Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Visual Studio Code

## Features

- Add and manage calendar events.
- Save events permanently using SQLite.
- Identify important events using predefined keywords.
- Recommend Silent Mode for important activities.
- Recommend Normal Mode for non-important activities.
- Display today's, tomorrow's, and upcoming seven days' recommendations.
- Delete unwanted events.

## Project Structure

```text
silentmode/
├── app.py
├── calendar_service.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
├── Project_Report.pdf
└── Screenshots/
```

## How to Run the Project

### 1. Install the required libraries

```bash
pip install streamlit pandas
```

### 2. Open the project folder in Visual Studio Code.

### 3. Run the application

```bash
streamlit run app.py
```

### 4. Open the local URL displayed in the terminal.

## Recommendation Logic

The system uses a rule-based algorithm to analyze event names, dates, and times.

| Event | Recommendation |
|---|---|
| College Class | Silent Mode |
| Seminar | Silent Mode |
| Examination | Silent Mode |
| Break | Normal Mode |

## Future Enhancements

- Calendar synchronization.
- Desktop notifications.
- Improved event identification using machine learning.
- Automatic sound-mode control with user permission.

## Conclusion

The project provides a simple calendar-based recommendation system to help users reduce disturbances during important activities.

**Developed as a Computer Architecture Mini Project.**