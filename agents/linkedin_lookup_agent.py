from langchain import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str, openai_api_key: str) -> str:
    llm = ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key
    )
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page. 
    Your answer should contain only a URL."""
    # note that we included the output indicator in the prompt, otherwise the LLM tends to include other natural language words.
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the LinkedIn page URL.",
        )
    ]
    # note that we included the description for the LLM to reason about the tool.

    agent = initialize_agent(
        tools=tools_for_agent,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        llm=llm,
        handle_parsing_errors=True,
    )
    # we set verbose to True to see the reasoning steps of the agent.

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url
