from fastapi import FastAPI
app = FastAPI()



# Get --> read Todo
@app.get('/todos', tags=['Todos'])
async def get_todos() -> dict:
    return {'data': todos}


# Post --> create Todo
@app.post('/todo', tags=['Todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {'data': 'You have add Todo successfully'}


# put --> update todo
@app.put(f'/todo/{id}', tags=['Todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['title'] = body['title']
            todo['description'] = body['description']
            return {'data': f"You have update Todo with id {id} successfully"}
    return{'data': f"Todo with id {id} does not exist"}


# delete --> delete todo
@app.delete(f'/todo/{id}', tags=['Todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {'data': f"You have delete Todo with id {id} successfully"}
    return{'data': f"Todo with id {id} does not exist"}



todos = [
    {"id": "1",
     "title": "Learn fastApi basic",
     "description": "start learning the basics of fastapi"},
    {"id": "2",
     "title": "Learn React basic",
     "description": "start learning the basics of React js"},
    {"id": "3",
     "title": "Become a professional developer",
     "description": "learn more stacks to become a professional fulstack developer"}
]
