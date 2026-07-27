"""
LangGraph Builder
"""

try:
    from langgraph.graph import StateGraph, END

    from graph.state import GraphState
    from graph.nodes import supervisor_node, agent_node
    from graph.human_approval import request_approval
    from graph.conditional_edges import next_step
    from graph.logger import (
        log_query,
        log_completion,
        log_error,
    )


    def build_graph():
        graph = StateGraph(GraphState)

        graph.add_node(
            "supervisor",
            supervisor_node,
        )

        graph.add_node(
            "agent",
            agent_node,
        )

        graph.add_node(
            "human",
            request_approval,
        )

        graph.set_entry_point("supervisor")

        graph.add_edge(
            "supervisor",
            "agent",
        )

        graph.add_conditional_edges(
            "agent",
            next_step,
            {
                "human": "human",
                "agent": END,
                "end": END,
            },
        )

        graph.add_edge(
            "human",
            END,
        )

        return graph.compile()


    GRAPH = build_graph()


    def run(query: str) -> dict:
        try:
            log_query(query)

            state = GRAPH.invoke(
                {
                    "query": query,
                }
            )

            log_completion()

            return {
                "agent": state.get("route"),
                "response": state.get("response"),
            }

        except Exception as ex:
            log_error(ex)
            raise


except Exception:

    from agents.supervisor_agent import run as fallback


    def run(query: str) -> dict:
        return fallback(query)