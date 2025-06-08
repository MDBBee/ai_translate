from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import schemas


app = FastAPI()

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

templates = Jinja2Templates(directory="templates")

 
@app.get("/index", response_class=HTMLResponse)
async def read_index(request: Request):
    """Read Index"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):

    task = crud.create_translation_task(x,y)
    background_tasks.add_task(perform_translation, task.id, request.text, request.languages, db)

    return {"task_id": {task.id}}