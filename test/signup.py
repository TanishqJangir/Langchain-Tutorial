from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="User Authentication API",
    description="A simple FastAPI service for user signup",
    version="1.0.0"
)

# Pydantic model for request validation
class UserSignupRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: str = Field(..., min_length=5, description="Valid email address")
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

# Pydantic model for response serialization
class UserSignupResponse(BaseModel):
    message: str
    username: str
    email: str

# In-memory database mock (dict key: username, value: dict representation of user)
fake_db = {}

@app.post("/signup", response_model=UserSignupResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserSignupRequest):
    # Simple email format validation (check for @ and .)
    if "@" not in user_data.email or "." not in user_data.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format"
        )

    # Check if username already exists
    if user_data.username in fake_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email already registered
    for user in fake_db.values():
        if user["email"] == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
            
    # Save the user to our dummy database
    fake_db[user_data.username] = {
        "username": user_data.username,
        "email": user_data.email,
        "password": user_data.password
    }
    
    return UserSignupResponse(
        message="User registered successfully",
        username=user_data.username,
        email=user_data.email
    )
