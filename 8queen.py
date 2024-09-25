from flask import Flask,render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/solve', methods=['GET'])
def solve_queens():
    """API route to solve the 8-Queens problem and return the solution."""
    solution = hill_climbing()
    return jsonify(solution)  


# Hill climbing solution for 8-Queens problem

def generate_initial_state():
    """Generate a random initial state where each queen is in a different column."""
    return [random.randint(0, 7) for _ in range(8)]

def evaluate_state(state):
    """Count the number of attacking pairs of queens."""
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    """Generate neighboring states by moving one queen to a different row in its column."""
    neighbors = []
    for i in range(8):
        for j in range(8):
            if state[i] != j:
                new_state = state[:]
                new_state[i] = j
                neighbors.append(new_state)
    return neighbors

def hill_climbing():
    """Find a solution to the 8-Queens problem using hill climbing."""
    current_state = generate_initial_state()
    current_score = evaluate_state(current_state)
    
    while current_score > 0:
        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=lambda state: evaluate_state(state))
        next_score = evaluate_state(next_state)
        
        if next_score >= current_score:
            return current_state  # No improvement, exit
        
        current_state = next_state
        current_score = next_score
    
    return current_state

'''# New root route for /
@app.route('/')
def index():
    return "Welcome to the 8-Queens Solver API! Visit /solve to get a solution."'''


if __name__ == "__main__":
    app.run(debug=True)
