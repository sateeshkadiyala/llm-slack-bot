import logging

from dotenv import load_dotenv
from llm_helper import get_answer
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

api = FastAPI()

@api.get("/answer")
async def answer(req: Request, q: str):
    if not q:
        return {}
    else:
        answer = await get_answer(q)
    
        return {
            'answer': answer
        }