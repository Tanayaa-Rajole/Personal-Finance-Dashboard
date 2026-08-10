from fastapi import FastAPI

app = FastAPI(
    title="Personal Finance Manager API",
    description="API for managing personal finances, expenses, budgets, and financial insights.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Personal Finance Manager API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
