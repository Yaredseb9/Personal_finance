
# personal finance
### set up

1. go inside backend folder 
   ```cmd
    cd  backend\ 
    ```
1. create python enviromental virable 
    ```cmd
    python -m venv venv 
    ```
1. activate python enviroment 
   ```cmd
    venv\Scripts\activate
    ```
2. install django depencency
   ```cmd
   pip install
   ```
  
  ## steps
# 💰 Personal Finance App – Backend

This is the backend API for the Personal Finance App built using **Django + DRF**, connected to **Supabase PostgreSQL**, with **Token Authentication** for user login.

---

## 🔧 Backend Setup Checklist

- [x] Create Python virtual environment  
- [x] Install Django and dependencies  
- [x] Configure `.env` using `python-decouple`  
- [x] Connect to Supabase PostgreSQL  
- [x] Define models: Income, Expense  
- [x] Run migrations  
- [x] Create serializers and API views  
- [x] Set up DRF token authentication  
- [x] Create register and login views  
- [x] Secure endpoints with authentication  
- [x] Create `requirements.txt`  

---

## 📁 Folder Structure

- `backend/`: Django project root  
  - `api/`: App with models, views, serializers, and URLs  
  - `.env`: Environment variables  
  - `requirements.txt`: Python dependencies  

---

## 🔜 Next Steps

- Add pagination, filtering, and validation  
- Set up admin dashboards (optional)  
- Enable deployment configuration  
