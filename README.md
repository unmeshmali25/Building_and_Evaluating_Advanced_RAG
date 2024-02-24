# Building_and_Evaluating_Advanced_RAG
The repository uses llamaindex to build 3 levels of RAG applications on my personal blog. It also uses TrueEra to evaluate each of the RAG methodologies based on context relevance, answer relevance, and groundedness

IMP : This is a follow-along from Deeplearning.AI's short course. But I am using my own keys and data to expand on the implementation. 

PROMPT : 
Where was Unmesh employed in May 2022?

RESPONSE : 
Unmesh was employed at CEEW as a Sustainable Mobility Research Assistant in May 2022.






Debugging 
------------------------------
Error : 
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
(umenv) MACFG33C2C21M:Building and Evaluating Advanced RAG c536898$ pip3 freeze > requirements.txt

Need to buy more credits and try again. 
------------------------------
Response : Unmesh was employed at CEEW as a Sustainable Mobility Research Assistant in May 2022.
My take : This is wrong answer. I don't have any weekly blogs in 2022. However, I was employed at the said organization in May 2021. 
This RAG application needs to be more advanced (will ask same question through window sentence retrieval) and also setup evaluation later. 