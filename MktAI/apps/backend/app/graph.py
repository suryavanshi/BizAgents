"""Simple LangGraph with Research -> Enrich -> Draft Email nodes."""

from langgraph.graph import StateGraph


async def research_step(data: dict) -> dict:
    # TODO: implement research logic
    return {"research": f"research about {data.get('account')}"}


async def enrich_step(data: dict) -> dict:
    # TODO: enrich contact data
    return {"enriched": f"enriched data for {data.get('account')}"}


async def draft_email_step(data: dict) -> dict:
    # TODO: draft email using LLM
    return {"email": f"Email draft for {data.get('account')}"}


def build_graph() -> StateGraph:
    graph = StateGraph()
    graph.add_node("research", research_step)
    graph.add_node("enrich", enrich_step)
    graph.add_node("draft", draft_email_step)

    graph.set_entry_point("research")
    graph.connect("research", "enrich")
    graph.connect("enrich", "draft")
    graph.set_exit_point("draft")

    return graph


async def run_graph(payload: dict) -> dict:
    graph = build_graph()
    state = await graph.apredict(payload)
    return state
