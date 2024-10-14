from flask import Flask, request, render_template, redirect, url_for
import git
import os

app = Flask(__name__)

# Repository path - you can change this to any directory you want
REPO_PATH = 'C:\\Users\\premk\\Documents\\PythonAssignments\\notepad_tracker'

# Initialize or open the Git repository
if not os.path.exists(REPO_PATH):
    os.makedirs(REPO_PATH)
    repo = git.Repo.init(REPO_PATH)
else:
    repo = git.Repo(REPO_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    content = request.form.get('content', '')
    filename = request.form.get('filename', 'note.txt')
    
    file_path = os.path.join(REPO_PATH, filename)
    
    with open(file_path, 'w') as file:
        file.write(content)
    
    # Add, commit, and push changes
    repo.index.add([file_path])
    repo.index.commit("Updated note")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
