# 8-Queens-Hill-Climbing
This project provides a solution to the classic 8-Queen Problem using the Hill Climbing algorithm. The problem involves placing 8 queens on an 8x8 chessboard such that no two queens threaten each other, i.e., no two queens share the same row, column, or diagonal. The Hill Climbing algorithm is used to solve this problem by iteratively moving towards a solution with the least conflicts.

8-queen-hill-climbing/
│
├── app.py              # Flask application
├── hill_climbing.py    # Hill climbing algorithm logic
├── templates/
│   ├── index.html      # Web page for displaying results
│   └── result.html     # Page to show final result[optional]
├── static/
│   └── style.css       # CSS styles for the web app
├── README.md           # Project documentation
└── requirements.txt    # List of dependencies


NOTE:
app.py: This file contains the Flask application. It handles routing and logic for rendering the views.
hill_climbing.py: This file contains the core logic of the Hill Climbing algorithm for solving the 8-Queen problem.
