from db.run_sql import run_sql

from models.task import Task #  ADDED

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"  # MODIFIED
    values = [task.description, task.assignee, task.duration, task.completed]
    results = run_sql(sql, values)  # MODIFIED
    id = results[0]['id']           # ADDED
    task.id = id                    # ADDED
    return task

def select_all():  
    tasks = []  # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['description'], row['assignee'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks

def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        task = Task(result['description'], result['assignee'], result['duration'], result['completed'], result['id'] )
    return task

def delete_all():
    sql = "DELETE  FROM tasks" 
    run_sql(sql)
    
def update(task):
    sql = "UPDATE tasks SET (description, assignee, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.assignee, task.duration, task.completed, task.id]
    run_sql(sql, values) 