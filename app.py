from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

app = FastAPI()
llm = OpenAI(temperature=0)

class QueryInput(BaseModel):
    intent: str

@app.post("/generate")
def generate_query(input: QueryInput):
    template = PromptTemplate(
        input_variables=["intent"],
        template="Translate the following intent to a GraphQL query: {intent}"
    )
    query = llm(template.format(intent=input.intent))
    return {"graphql": query}
