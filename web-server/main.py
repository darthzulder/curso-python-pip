import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return {'name': 'Platzi'}

@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Wololooo Mundo</h1>
        <p>Soy un parrafofo</p>
    """


def run():
    store.get_categories()

if __name__=='__main__':
    run()