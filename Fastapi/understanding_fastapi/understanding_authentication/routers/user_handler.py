
from datetime import timedelta,datetime,timezone
from fastapi import APIRouter,HTTPException,Depends
from models.models import User
from models.models_valdations import user_validate,Token
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer


from database.database import SessionLocal

router = APIRouter()
secret_key ='197ASD565467'
ALGORITHM = 'HS256'

brcrypt_context =CryptContext(schemes=['bcrypt'],deprecated='auto')
oaut2_bearer = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]





#passing user name and comparing 
def auth_user(username:str,password:str,db):
    user =db.query(User).filter(User.username==username).first()
    if not user:
        return False
    if not brcrypt_context.verify(password,user.hash_password):
        return False
    return user

def create_token_for_user_access(username:str,user_id:int,exipers_delta:timedelta):
    encode = {'sub':username,'id':user_id}
    expire = datetime.now(timezone.utc)+exipers_delta
    encode.update({'exp':expire})
    return jwt.encode(encode, secret_key, algorithm=ALGORITHM)

async def get_current_user(token:Annotated[str,Depends(oaut2_bearer)]):
    try:
        payload = jwt.decode(token,secret_key,algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id:int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not valid hhuser')
        return { 'username': username,'id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not dvalid user')







@router.post("/register",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,user: user_validate):
    created_user = User(username=user.username,
                        email=user.email,
                        has_paid=user.has_paid,
                        role=user.role,

                        hash_password=brcrypt_context.hash(user.password))# using it to pass hash password 
    db.add(created_user)
    db.commit()

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    user = auth_user(form_data.username, form_data.password,db )
    if not user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='could not valid user')
    token = create_token_for_user_access(user.username,user.id,timedelta(minutes=60))
    return {
        "access_token": token,
        "token_type": "bearer"
            }

  







