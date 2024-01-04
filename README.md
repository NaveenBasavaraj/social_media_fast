pip install fastapi uvicorn
uvicorn your_module_name:app --reload
uvicorn main:app --reload
uvicorn movies_app:app --reload

Fast API automatic documentations: http://127.0.0.1:8000/docs