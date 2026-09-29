from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# Pre-initialize agents once at module load to avoid graph rebuilding overhead
search_agent = build_search_agent()
reader_agent = build_reader_agent()

def run_research_pipeline(topic:str)->dict :
    state={}
    
    search_result=search_agent.invoke({
        "messages":[("user",f"find recent reliable and detailed information about:{topic}")]
    })
    state["search_result"]=search_result['messages'][-1].content
    
    reader_result=reader_agent.invoke({
        "messages":[(
            "user",
            f"based on following search result about '{topic}',"
            f"pick the most relevant url and scrape the page for detailed information and return the text content:\n\n"
            f"search result:\n{state['search_result'][:800]}"
        )]
    })
    state['reader_result']=reader_result['messages'][-1].content
    
    research_combine=(
        f"search result :\n {state['search_result']}\n\n"
        f"scraped content: \n {state['reader_result']}"
    )    
    
    state['report']=writer_chain.invoke({
        'topic':topic,
        'research':research_combine
    })
    
    state['feedback']=critic_chain.invoke({
        "report":state['report'],
        "topic":topic,
        "research":research_combine
    })
    
    return state


if __name__=="__main__":
    topic=input("\nResearch topic:")
    run_research_pipeline(topic)