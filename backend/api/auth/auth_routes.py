from fastapi import Depends, FastAPI, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from utils.schemas import UserCreate 
from sqlalchemy.sql import text

from database import get_db

# Define the authentication configuration
JWT_SECRET_KEY = "your-secret-key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 30

# Define the password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Define the FastAPI router
auth_router = APIRouter()

# Define the authentication functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return username

# Define the authentication routes
@auth_router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate the user here with form_data.username and form_data.password
    # and get their user details. For example, let's assume we have a fake user
    # database containing only the following user.
    fake_user_db = {
        "username": "johndoe",
        "hashed_password": "$2b$12$7Wzww1AeuxgJ9.tPb3mk7uI8fnMgoVYFnbC1E2T1INW8RbFJ7X9ZC",  # password: secret
        "email": "johndoe@example.com",
        "full_name": "John Doe"
    }

    user = fake_user_db.get("username")
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    elif not verify_password(form_data.password, fake_user_db["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    access_token = create_access_token(data={"sub": user}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# Define a protected endpoint
@auth_router.get("/users/me")
async def read_users_me(db = Depends(get_db), username: str = Depends(get_current_user)):
    user = db.execute(text("SELECT * FROM users WHERE username = ?"), (username,)).fetchone()
    return {"username": user["username"], "email": user["email"], "full_name": user["full_name"]}

@auth_router.post("/users")
async def create_user(user: UserCreate, db = Depends(get_db)):
    # Check if the user already exists
    if db.execute(text("SELECT id FROM users WHERE username = ?"), (user.business_name,)).fetchone() is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Insert the user into the database
    db.execute(
        text("INSERT INTO users (username, hashed_password) VALUES (?, ?)"),
        (user.username, hashed_password)
    )
    db.commit()

    return {"message": "User created successfully"}