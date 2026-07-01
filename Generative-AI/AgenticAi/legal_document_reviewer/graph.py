from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from state import ReviewState

from nodes import *

workflow = StateGraph(ReviewState)

# Nodes
workflow.add_node("load", load_document)

workflow.add_node("summary", summarize)

workflow.add_node("risk", analyze_risk)

workflow.add_node("compliance", compliance)

workflow.add_node("report", report)
 

#Edges
workflow.set_entry_point("load")

workflow.add_edge("load", "summary")

workflow.add_edge("summary", "risk")

workflow.add_edge("risk", "compliance")

#workflow.add_edge("compliance", "report") #Without human review, we can go directly to report

workflow.add_edge("compliance", "report")
workflow.add_edge("report", END)

memory = MemorySaver()

graph = workflow.compile(
    checkpointer=memory
)