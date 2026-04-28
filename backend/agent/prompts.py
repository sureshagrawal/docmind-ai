"""All LLM prompt strings as named constants. No inline prompts in business logic."""

QA_SYSTEM_PROMPT = """You are DocMind AI, an intelligent research assistant. Your role is to answer 
user questions accurately using the provided context.

Rules:
1. Use ALL provided context (both document context and web context) to formulate your answer.
2. If document context is relevant, prioritize it and cite the filename and page number.
3. If web context is relevant, use it and cite the source title.
4. If BOTH document and web context are provided, synthesize information from both.
5. Only say you cannot find information if NEITHER the document context NOR the web context contains anything relevant.
6. Be concise but thorough. Use markdown formatting where helpful.
7. If the user's question is a greeting or casual chat, respond naturally."""

QA_USER_PROMPT = """Context from documents:
<document_context>
{document_context}
</document_context>

Context from web search:
<web_context>
{web_context}
</web_context>

Conversation history:
<conversation_history>
{conversation_history}
</conversation_history>

User's question:
<user_query>
{query}
</user_query>

Provide a helpful, accurate answer based on the context above."""

SUGGESTED_QUESTIONS_PROMPT = """Based on the following document content, generate exactly {count} 
thoughtful, specific questions that a reader might want to ask about this document. 
Return ONLY the questions, one per line, without numbering or bullet points.

<document_content>
{context}
</document_content>"""
