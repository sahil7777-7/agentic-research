from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from rich import print
load_dotenv()

tavily=TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))

@tool
def web_search(query : str)->str:
    """search the web for recent and reliable information on a topic, return titel, urls snippets"""
    result=tavily.search(
        query=query,
        max_results=5,
    )
    
    out=[]
    
    for r in result['results'] :
        out.append(
            f"Title: {r['title']} \nURL: {r['url']} \nsnippet: {r['content'][:300]} \n\n"
        )
    return "\n--------------------------------------------\n".join(out)





@tool
def web_scrape(url : str)->str:
    """scrape the web page for information, return the text content"""
    # 1. Fast extraction via Tavily (avoids bot blocks & timeouts)
    try:
        extract_res = tavily.extract(urls=[url])
        if extract_res and 'results' in extract_res and len(extract_res['results']) > 0:
            content = extract_res['results'][0].get('raw_content', '')
            if content and len(content.strip()) > 50:
                return content[:1200]
    except Exception:
        pass

    # 2. Fast direct fallback with 3.5s timeout
    try:
        response = requests.get(
            url,
            timeout=3.5,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        )
        soup = BeautifulSoup(response.content, 'html.parser')
        for tag in soup(['script', 'style','nav','header','footer']):
             tag.decompose()
        text = soup.get_text(separator=" ", strip=True)[:1000]
        return text if text else "No content extracted from page."
    except Exception as e:
        return f"Error scraping the web page: {e}"
    
