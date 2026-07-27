# Workflow

1. User asks a question in the Chat page.
2. `graph/workflow.py` invokes the LangGraph StateGraph.
3. `Supervisor` node routes the query to the right specialist.
4. Specialist agent gathers context via `tools/*` → `services/*` → `api/*`.
5. LLM (if key present) generates a response; otherwise a rule-based fallback is returned.
6. Response added to session memory and rendered.
