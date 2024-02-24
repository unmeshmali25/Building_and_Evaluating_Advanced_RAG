import os
import json
import utils
import openai
import sys
import llama_index
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document

with open('./openkey.json', 'r') as file:
	data = json.load(file)

os.environ['OPENAI_API_KEY'] = data['openai-api-key']
openai.api_key = utils.get_openai_api_key()

def readInVectorDB():
	documents = SimpleDirectoryReader(
    	input_files=["./unmeshmaliWeeklyBlog.pdf"]
	).load_data()
	return documents
documents = readInVectorDB()

print(type(documents), "/n")
print(documents[0])

document = Document(text="\n\n".join([doc.text for doc in documents]))
from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo", temperature=0.1
)
service_context = ServiceContext.from_defaults(
    llm=llm, embed_model="local:BAAI/bge-small-en-v1.5"
)

index = VectorStoreIndex.from_documents([document], 
                                        service_context=service_context)

query_engine_um = index.as_query_engine()

response = query_engine_um.query(
    "Where was Unmesh employed in May 2022"
)

print(str(response))