from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, web_scrape
import os
from rich import print
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenRouter(
    model='google/gemma-4-26B-A4B-it',
    max_retries=3
)

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="You are a fast search agent. Call web_search immediately for the query and summarize the findings directly."
    )
    
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[web_scrape],
        system_prompt="You are a fast web reader agent. Pick the single best URL from the search results, call web_scrape immediately, and return the key extracted text directly."
    )
    
#writer chain

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain= writer_prompt | llm | StrOutputParser ()

#critic_chain

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict
"""),
])

critic_chain= critic_prompt | llm | StrOutputParser ()

