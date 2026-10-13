# Student Performance Tracker

This started with a simple question: if I had a class's marks saved in one place, what else could I find out besides each student's total?

I was learning Python at the time and wanted to try a slightly bigger program. I made a command-line tracker that can manage student records, compare results across sections, make charts, and export a leaderboard.

It's still a small project, but it was where I began getting interested in academic data beyond individual marks.

## See it working

![Demo of the command-line program](Demo/Demo_project.gif)

## What the program does

You can add, view, edit, or delete students. The records include an ID, name, section, and marks in the subjects listed in [`config.json`](config.json).

It can also calculate:
- Student rankings and the top N performers
- Class averages, section averages, and section toppers
- Subject toppers and overall topper
- Pass/fail results and filters by section or result

I used Matplotlib to draw some of these results instead of showing everything as text. There's also an option to export the leaderboard as CSV.

## Charts

| Top performers | Pass and fail counts |
| --- | --- |
| ![Top five students](Reports/top5_students.png) | ![Pass and fail](Reports/pass_fail_analysis.png) |

| Section comparison | Grade distribution |
| --- | --- |
| ![Section averages](Reports/section_wise_analysis.png) | ![Grade distribution](Reports/grade_distribution.png) |

These are example outputs included so you can see the kind of reports it produces.

## How to run it

You'll need Python 3 and Matplotlib.

```bash
git clone https://github.com/Rafidabd/student-performance-tracker.git
cd student-performance-tracker
python -m pip install -r requirements.txt
python main.py
```

The program has a numbered terminal menu. Choose an option to add records, see statistics, export a CSV, or generate a chart.

The configuration file controls the subjects, sections, mark limits, pass mark, and grade boundaries. Student records are saved locally in `data/students.json`; the file is created automatically and ignored by Git. Reports go into `Reports/`.

Please use fictional or appropriately authorized records if you try it with student data.

## Project files

```text
student-performance-tracker/
├── Demo/                   # Short GIF of the program
├── Reports/                # Sample charts and leaderboard
├── modules/
│   ├── analytics.py        # Rankings and calculations
│   ├── cli.py              # Menu and user input
│   ├── config_loader.py
│   ├── display.py
│   ├── export.py           # CSV output
│   ├── storage.py          # JSON data
│   ├── student.py          # Student records
│   ├── utils.py
│   └── visualize.py        # Matplotlib charts
├── tests/
│   └── test_storage.py
├── config.json
├── main.py
├── requirements.txt
└── README.MD
```

## Testing

Run the two basic storage tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

They check that an empty JSON store is created and that a sample student record can be saved and loaded. I haven't built a full set of tests for rankings, grading, charts, or the menu yet.

## Looking back

What I found interesting wasn't just calculating the average. It was seeing how one set of marks could be used to answer several questions about a class. I also learned that keeping student records, calculations, display code, and charts in separate modules makes it easier to find and change things later.

The program still uses local JSON and has no login or multi-user features. My ongoing [Bangladesh Academic Analytics System](https://github.com/Rafidabd/python-phase-1/tree/main/academics_analytics_system) is a separate, more ambitious project growing from some of these interests.

This tracker originally lived in [my Python practice repository](https://github.com/Rafidabd/python-phase-1/tree/main/day13_Mini_Projects/student-performance-tracker). I moved it to its own repository with its project-specific development history.
