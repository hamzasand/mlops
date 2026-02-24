from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    return {"messages": ["Hi, This is message from Chatbot node"]}

def samplemes(state: State):
    return {"messages": ["Sample message is append"]}


garph_builder = StateGraph(State)
garph_builder.add_node("chatbot", chatbot)
garph_builder.add_node("samplemes", samplemes)

garph_builder.add_edge(START,"chatbot")
garph_builder.add_edge("chatbot", "samplemes")
garph_builder.add_edge("samplemes", END)

garph = garph_builder.compile()
update_state = garph.invoke(State({"messages": ["Hi, my name is Hamza"]}))
print("update_state", update_state)