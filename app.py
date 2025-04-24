from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample task data stored in a list of dictionaries
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'This is task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'This is task 2',
        'done': False
    }
]

# Home route
@app.route('/')
def home():
    return "Hello, World!"

# GET all tasks
@app.route('/get-all-tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# GET a specific task by ID
@app.route('/get-task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    return jsonify({'message': 'Task not found'}), 404

# POST to create a new task
@app.route('/create-task', methods=['POST'])
def create_task():
    data = request.json
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully', 'task': new_task}), 201

# PUT to update an existing task
@app.route('/update-task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.json
        task.update(data)
        return jsonify({'message': 'Task updated successfully', 'task': task})
    return jsonify({'message': 'Task not found'}), 404

# DELETE a task
@app.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
