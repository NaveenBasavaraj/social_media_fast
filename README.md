pip install fastapi uvicorn
uvicorn your_module_name:app --reload
uvicorn main:app --reload
uvicorn main_demo:app --reload

Fast API automatic documentations: http://127.0.0.1:8000/docs
uvicorn Product_API.main:app --reload
